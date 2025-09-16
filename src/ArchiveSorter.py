import os
import shutil
import re
import json
import sys

# Configure your source and destination here
source_dir = r'D:\Downloads'
dest_root = r'D:\CODING\ARCHIVES\DATABASE'
misc_folder = 'MISCELLANEOUS'

ENABLE_FILE_COUNT = False # Set to True to enable file count suffixing

# Central metadata file path
metadata_folder = os.path.join(os.getcwd(), '.filecount_metadata')
os.makedirs(metadata_folder, exist_ok=True)
metadata_file_path = os.path.join(metadata_folder, 'metadata.json')

# Regex to strip the (File Count - N) suffix from folder names
FILE_COUNT_SUFFIX_RE = re.compile(r'^(.*?)(\s*\(File Count - \d+\))?$', re.IGNORECASE)

def strip_file_count_suffix(folder_name):
    match = FILE_COUNT_SUFFIX_RE.match(folder_name)
    if match:
        return match.group(1).strip()
    return folder_name

def load_metadata():
    if os.path.isfile(metadata_file_path):
        try:
            with open(metadata_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_metadata(data):
    with open(metadata_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def discover_existing_folders(dest_root, misc_folder):
    existing_folders = {}
    for item in os.listdir(dest_root):
        full_path = os.path.join(dest_root, item)
        if os.path.isdir(full_path):
            for root, dirs, _ in os.walk(full_path):
                for d in dirs:
                    nested_path = os.path.join(root, d)
                    relative_path = os.path.relpath(nested_path, dest_root)
                    normalized_key = relative_path.replace(os.sep, '/').upper()
                    existing_folders[normalized_key] = nested_path
            if strip_file_count_suffix(item).upper() != misc_folder:
                normalized = strip_file_count_suffix(item).upper()
                if normalized not in existing_folders:
                     existing_folders[normalized] = full_path

    misc_path = os.path.join(dest_root, misc_folder)
    if os.path.isdir(misc_path):
        for folder in os.listdir(misc_path):
            full_path = os.path.join(misc_path, folder)
            if os.path.isdir(full_path):
                normalized = f"{misc_folder}/{strip_file_count_suffix(folder).upper()}"
                existing_folders[normalized] = full_path
    return existing_folders

def update_folder_name_with_file_count(folder_path, metadata, script_dir, cwd):
    folder_path_abs = os.path.abspath(folder_path)

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

    if ENABLE_FILE_COUNT:
        new_folder_name = f"{base_name} (File Count - {current_count})"
    else:
        new_folder_name = base_name

    if (ENABLE_FILE_COUNT and (previous_count != current_count or folder_name != new_folder_name)) or \
       (not ENABLE_FILE_COUNT and folder_name != new_folder_name):

        new_folder_path = os.path.join(folder_parent, new_folder_name)
        if not os.path.exists(new_folder_path):
            try:
                os.rename(folder_path, new_folder_path)
                print(f"Renamed folder: '{folder_name}' -> '{new_folder_name}'")

                if ENABLE_FILE_COUNT:
                    metadata[new_folder_path] = current_count
                    metadata.pop(folder_path_abs, None)
                else:
                    metadata.pop(folder_path_abs, None)
            except PermissionError as e:
                print(f"PermissionError renaming folder '{folder_name}': {e}")
                if ENABLE_FILE_COUNT:
                    metadata[folder_path_abs] = current_count
        else:
            if ENABLE_FILE_COUNT:
                metadata[folder_path_abs] = current_count
    else:
        if ENABLE_FILE_COUNT:
            metadata[folder_path_abs] = current_count
        else:
            metadata.pop(folder_path_abs, None)

def move_files_by_extension(src, dst):
    existing_folders = discover_existing_folders(dst, misc_folder)
    script_dir = os.path.abspath(os.path.dirname(__file__))
    cwd = os.path.abspath(os.getcwd())

    metadata = load_metadata()

    for root, _, files in os.walk(src):
        for file in files:
            ext = os.path.splitext(file)[1].lower().lstrip('.')

            if ext in extension_to_folder:
                folder_name = extension_to_folder[ext]
                key = folder_name.upper()
                dest_folder = existing_folders.get(key, os.path.join(dst, *folder_name.split('/')))
            elif ext:
                misc_key = f"{misc_folder}/{ext.upper()}"
                dest_folder = existing_folders.get(misc_key, os.path.join(dst, misc_folder, ext.upper()))
            else:
                noext_key = f"{misc_folder}/NO_EXTENSION"
                dest_folder = existing_folders.get(noext_key, os.path.join(dst, misc_folder, 'NO_EXTENSION'))

            os.makedirs(dest_folder, exist_ok=True)

            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_folder, file)

            base, extension = os.path.splitext(file)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{extension}")
                counter += 1

            shutil.move(src_path, dest_path)
            try:
                print(f"Moved: {src_path} --> {dest_path}")
            except UnicodeEncodeError:
                print(f"Moved file with special characters: {src_path.encode('utf-8', 'replace').decode()} --> {dest_path.encode('utf-8', 'replace').decode()}")
        break

    reorganize_internal_files(dst, misc_folder)

    all_dirs = set()
    for root, dirs, _ in os.walk(dst):
        for d in dirs:
            all_dirs.add(os.path.join(root, d))

    for folder_path in all_dirs:
        if strip_file_count_suffix(os.path.basename(folder_path)).upper() != misc_folder:
            update_folder_name_with_file_count(folder_path, metadata, script_dir, cwd)

    save_metadata(metadata)

def reorganize_internal_files(dst_root, misc_folder, existing_folders=None):
    """
    Recursively scan inside `dst_root` to find misplaced files and move them.
    """
    if existing_folders is None:
        existing_folders = discover_existing_folders(dst_root, misc_folder)

    for root, _, files in os.walk(dst_root):
        if 'metadata.json' in files and root != os.path.join(os.getcwd(), '.filecount_metadata'):
            continue

        for file in files:
            if file == 'metadata.json':
                continue

            ext = os.path.splitext(file)[1].lower().lstrip('.')

            folder_name_key = None
            if ext in extension_to_folder:
                folder_name = extension_to_folder[ext]
                folder_name_key = folder_name.upper()
                correct_folder_path = existing_folders.get(folder_name_key, os.path.join(dst_root, *folder_name.split('/')))
            elif ext:
                folder_name_key = f"{misc_folder}/{ext.upper()}"
                correct_folder_path = existing_folders.get(folder_name_key, os.path.join(dst_root, misc_folder, ext.upper()))
            else:
                folder_name_key = f"{misc_folder}/NO_EXTENSION"
                correct_folder_path = existing_folders.get(folder_name_key, os.path.join(dst_root, misc_folder, 'NO_EXTENSION'))

            os.makedirs(correct_folder_path, exist_ok=True)
            if not existing_folders.get(folder_name_key):
                existing_folders[folder_name_key] = correct_folder_path

            current_file_path = os.path.join(root, file)

            if os.path.abspath(root) != os.path.abspath(correct_folder_path):
                dest_path = os.path.join(correct_folder_path, file)
                base, extension = os.path.splitext(file)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(correct_folder_path, f"{base}_{counter}{extension}")
                    counter += 1
                shutil.move(current_file_path, dest_path)
                try:
                    print(f"Reorganized internal file: {current_file_path} --> {dest_path}")
                except UnicodeEncodeError:
                    print(f"Reorganized file with special characters: {current_file_path.encode('utf-8', 'replace').decode()} --> {dest_path.encode('utf-8', 'replace').decode()}")

if __name__ == '__main__':
    # Structured extension mappings
    extension_to_folder = {
        # -- MEDIA --
        'jpg': 'MEDIA/IMAGES', 'jpeg': 'MEDIA/IMAGES', 'png': 'MEDIA/IMAGES', 'pdn': 'MEDIA/IMAGES',
        'avif': 'MEDIA/IMAGES', 'webp': 'MEDIA/IMAGES', 'bmp': 'MEDIA/IMAGES',
        'tiff': 'MEDIA/IMAGES', 'jfif': 'MEDIA/IMAGES', 'svg': 'MEDIA/IMAGES', 'ico': 'MEDIA/IMAGES',
        'gif': 'MEDIA/GIFS',
        'mp4': 'MEDIA/VIDEOS', 'mov': 'MEDIA/VIDEOS', 'mkv': 'MEDIA/VIDEOS', 'avi': 'MEDIA/VIDEOS', 'webm': 'MEDIA/VIDEOS',
        'mp3': 'MEDIA/AUDIO/MP3', 'wav': 'MEDIA/AUDIO/WAV', 'flac': 'MEDIA/AUDIO/FLAC', 'oga': 'MEDIA/AUDIO/OGA',
        'aac': 'MEDIA/AUDIO/AAC', 'ogg': 'MEDIA/AUDIO/OGG', 'm4a': 'MEDIA/AUDIO/M4A',
        'srt': 'MEDIA/SUBTITLES',
        'obj': 'MEDIA/3D_MODELS',

        # -- DOCUMENTS & TEXT --
        'pdf': 'DOCUMENTS/PDFS',
        'docx': 'DOCUMENTS/WORD', 'doc': 'DOCUMENTS/WORD',
        'xlsx': 'DOCUMENTS/EXCEL', 'xls': 'DOCUMENTS/EXCEL', 'csv': 'DOCUMENTS/EXCEL', 'xlsm': 'DOCUMENTS/EXCEL',
        'pptx': 'DOCUMENTS/POWERPOINT', 'ppt': 'DOCUMENTS/POWERPOINT',
        'txt': 'DOCUMENTS/TEXT', 'md': 'DOCUMENTS/MARKDOWN',

        # -- FONTS --
        'otf': 'FONTS', 'ttf': 'FONTS', 'woff': 'FONTS',

        # -- DEVELOPMENT & CODE --
        'py': 'DEVELOPMENT/PYTHON', 'cs': 'DEVELOPMENT/CSHARP',
        'js': 'DEVELOPMENT/JAVASCRIPT', 'json': 'DEVELOPMENT/JSON',
        'css': 'DEVELOPMENT/CSS', 'html': 'DEVELOPMENT/HTML', 'htm': 'DEVELOPMENT/HTML',
        'sk': 'DEVELOPMENT/SKRIPT',
        'yml': 'DEVELOPMENT/YAML', 'yaml': 'DEVELOPMENT/YAML', 'xml': 'DEVELOPMENT/XML',
        'ps1': 'DEVELOPMENT/SCRIPTS', 'sh': 'DEVELOPMENT/SCRIPTS', 'bat': 'DEVELOPMENT/SCRIPTS', 'cmd': 'DEVELOPMENT/SCRIPTS',
        'pyc': 'DEVELOPMENT/COMPILED', 'class': 'DEVELOPMENT/COMPILED',
        'log': 'DEVELOPMENT/LOGS',
        'cfg': 'DEVELOPMENT/CONFIG', 'ini': 'DEVELOPMENT/CONFIG', 'env': 'DEVELOPMENT/CONFIG',
        'toml': 'DEVELOPMENT/CONFIG', 'properties': 'DEVELOPMENT/CONFIG',

        # -- ARCHIVES & SYSTEM --
        'zip': 'ARCHIVES/ZIPS', 'rar': 'ARCHIVES/ZIPS', '7z': 'ARCHIVES/ZIPS',
        'tar': 'ARCHIVES/ZIPS', 'gz': 'ARCHIVES/ZIPS', 'xz': 'ARCHIVES/ZIPS', 'jar': 'ARCHIVES/ZIPS',
        'exe': 'ARCHIVES/PROGRAMS', 'msi': 'ARCHIVES/PROGRAMS', 'apk': 'ARCHIVES/PROGRAMS',
        'iso': 'ARCHIVES/DISK_IMAGES', 'img': 'ARCHIVES/DISK_IMAGES',
        'ovpn': 'ARCHIVES/VPN', 'conf': 'ARCHIVES/VPN',
        'reg': 'ARCHIVES/REGISTRY', 'pol': 'ARCHIVES/REGISTRY', 'inf': 'ARCHIVES/REGISTRY',
        'bin': 'ARCHIVES/BINARY',
        'dll': 'ARCHIVES/LIBRARIES',

        # -- GAMING --
        'mrpack': 'GAMING/MINECRAFT/MODPACKS',
        'mcpack': 'GAMING/MINECRAFT/RESOURCE_PACKS', 'mcmeta': 'GAMING/MINECRAFT/RESOURCE_PACKS',
        'litematic': 'GAMING/MINECRAFT/SCHEMATICS', 'schem': 'GAMING/MINECRAFT/SCHEMATICS',
        'dat': 'GAMING/MINECRAFT/WORLD_DATA', 'nbt': 'GAMING/MINECRAFT/WORLD_DATA',
        'mca': 'GAMING/MINECRAFT/WORLD_DATA', 'dat_old': 'GAMING/MINECRAFT/WORLD_DATA',
        'snbt': 'GAMING/MINECRAFT/WORLD_DATA',
        'mcfunction': 'GAMING/MINECRAFT/SCRIPTS',
        'bo3': 'GAMING/COD',
        'osk': 'GAMING/OSU',
      }
    try:
        move_files_by_extension(source_dir, dest_root)
        print("File transfer complete. Your archive has been elegantly reorganized.")
    except Exception as e:
        try:
            print(f"Error while processing: {e}")
        except UnicodeEncodeError:
            print(f"An error occurred with a file containing special characters that could not be displayed in the console.")
        sys.exit(1)