import os
import shutil
import re
import json
import sys

# Configure your source and destination here
source_dir = r'D:\Downloads'
dest_root = r'D:\CODING\ARCHIVES'
misc_folder = 'MISCELLANEOUS'

# Central metadata file path
metadata_folder = os.path.join(os.getcwd(), '.filecount_metadata')
os.makedirs(metadata_folder, exist_ok=True)
metadata_file_path = os.path.join(metadata_folder, 'metadata.json')

# Load metadata dictionary {folder_path (abs): count}
def load_metadata():
    if os.path.isfile(metadata_file_path):
        try:
            with open(metadata_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

# Save metadata dictionary {folder_path (abs): count}
def save_metadata(data):
    with open(metadata_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# Regex to strip the (File Count - N) suffix from folder names
FILE_COUNT_SUFFIX_RE = re.compile(r'^(.*?)(\s*\(File Count - \d+\))?$', re.IGNORECASE)

def strip_file_count_suffix(folder_name):
    match = FILE_COUNT_SUFFIX_RE.match(folder_name)
    if match:
        return match.group(1).strip()
    return folder_name

def discover_existing_folders(dest_root, misc_folder):
    """
    Returns a dictionary mapping of normalized folder keys (w/ uppercase no count suffix) to actual folder paths including the misc subfolders.
    Keys for misc subfolders are in the format "MISCELLANEOUS\EXTENSION".
    """
    existing_folders = {}
    for folder in os.listdir(dest_root):
        full_path = os.path.join(dest_root, folder)
        if os.path.isdir(full_path) and strip_file_count_suffix(folder).upper() != misc_folder:
            normalized = strip_file_count_suffix(folder).upper()
            existing_folders[normalized] = full_path

    misc_path = os.path.join(dest_root, misc_folder)
    if os.path.isdir(misc_path):
        for folder in os.listdir(misc_path):
            full_path = os.path.join(misc_path, folder)
            if os.path.isdir(full_path):
                normalized = f"{misc_folder}\\{strip_file_count_suffix(folder).upper()}"
                existing_folders[normalized] = full_path
    return existing_folders

def update_folder_name_with_file_count(folder_path, metadata, script_dir, cwd):
    """
    Renames folder to include [File Count: n] only when the count changes (reference metadata). Also skips renaming script or the current working directory.
    """
    folder_path_abs = os.path.abspath(folder_path)

    # Skip renaming the folder where the script/current working directory is located
    if folder_path_abs == script_dir or folder_path_abs == cwd:
        print(f"Skipping renaming protected directory: {folder_path_abs}")
        return

    folder_parent, folder_name = os.path.split(folder_path)
    base_name = strip_file_count_suffix(folder_name)

    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        current_count = len(files)
    except FileNotFoundError:
        return

    previous_count = metadata.get(folder_path_abs)

    if previous_count == current_count:
        return
    
    new_folder_name = f"{base_name} (File Count - {current_count})"
    if folder_name != new_folder_name:
        new_folder_path = os.path.join(folder_parent, new_folder_name)
        if not os.path.exists(new_folder_path):
            try:
                os.rename(folder_path, new_folder_path)
                print(f"Renamed folder: '{folder_name}' -> '{new_folder_name}'")
                metadata[new_folder_path] = current_count
                metadata.pop(folder_path_abs, None)
            except PermissionError as e:
                print(f"PermissionError renaming folder '{folder_name}': {e}")
                # If renaming fails, just update the metadata
                metadata[folder_path_abs] = current_count
        else:
            # If the new folder name already exists, just update the metadata
            metadata[folder_path_abs] = current_count
    else:
        # If the name is the same, just update the metadata
        metadata[folder_path_abs] = current_count

def move_files_by_extension(src, dst):
    existing_folders = discover_existing_folders(dst, misc_folder)
    script_dir = os.path.abspath(os.path.dirname(__file__))
    cwd = os.path.abspath(os.getcwd())
    metadata = load_metadata()
    for root, dirs, files in os.walk(src):
        for file in files:
            ext = os.path.splitext(file)[1].lower().lstrip('.')
            
            if ext in extension_to_folder:
                folder_name = extension_to_folder[ext]
                key = folder_name.upper()
                dest_folder = existing_folders.get(key, os.path.join(dst, folder_name))
            elif ext:
                misc_key = f"{misc_folder}\\{ext.upper()}"
                dest_folder = existing_folders.get(misc_key, os.path.join(dst, misc_folder, ext.upper()))
            else:
                noextension_key = f"{misc_folder}\\NO_EXTENSION"
                dest_folder = existing_folders.get(noextension_key, os.path.join(dst, misc_folder, 'NO_EXTENSION'))
            os.makedirs(dest_folder, exist_ok=True)

            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_folder, file)
            base, extension = os.path.splitext(file)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{extension}")
                counter += 1
            shutil.move(src_path, dest_path)
            print(f"Moved: {src_path} --> {dest_path}")
        break # Should process top-level files only
    
    # Once the files are moved, update the file counts for all existing folders
    for folder in os.listdir(dst):
        full_folder_path = os.path.join(dst, folder)
        if os.path.isdir(full_folder_path) and strip_file_count_suffix(folder).upper() != misc_folder:
            update_folder_name_with_file_count(full_folder_path, metadata, script_dir, cwd)

    misc_path = os.path.join(dst, misc_folder)
    if os.path.isdir(misc_path):
        for folder in os.listdir(misc_path):
            full_folder_path = os.path.join(misc_path, folder)
            if os.path.isdir(full_folder_path):
                update_folder_name_with_file_count(full_folder_path, metadata, script_dir, cwd)
    save_metadata(metadata)

if __name__ == '__main__':
    # Mapping of extensions to desired folder names (keep your full mapping here)
    extension_to_folder = {
        'jpg': 'IMAGES', 'jpeg': 'IMAGES', 'png': 'IMAGES', 'avif': 'IMAGES', 'webp': 'IMAGES',
        'bmp': 'IMAGES', 'tiff': 'IMAGES', 'jfif': 'IMAGES',
        'gif': 'GIFS',
        'mp4': 'VIDEOS', 'mov': 'VIDEOS', 'mkv': 'VIDEOS', 'avi': 'VIDEOS',
        'js': 'JS', 'json': 'JSON', 'css': 'CSS', 'html': 'HTML',
        'log': 'LOG', 'pdf': 'PDFS', 'py': 'PYTHON', 'txt': 'TXT', 'zip': 'ZIPS', 'sk': 'SKRIPT',
        # Add more if needed
    }
    try:
        move_files_by_extension(source_dir, dest_root)
        print("File transfer complete. Check your ARCHIVES directory to verify.")
    except Exception as e:
        print(f"Error while processing: {e}")
        sys.exit(1)