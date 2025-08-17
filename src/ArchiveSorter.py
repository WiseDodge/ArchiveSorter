import os
import shutil

source_dir = r'D:\Downloads'
dest_root = r'D:\CODING\ARCHIVES'
misc_folder = 'MISCELLANEOUS'

# Your custom mappings.
extension_to_folder = {
    # Images (excluding GIFS)
    'jpg': 'IMAGES',
    'jpeg': 'IMAGES',
    'png': 'IMAGES',
    'avif': 'IMAGES',
    'webp': 'IMAGES',
    'bmp': 'IMAGES',
    'tiff': 'IMAGES',
    'jfif': 'IMAGES',

    'gif': 'GIFS',

    # Videos
    'mp4': 'VIDEOS',
    'mov': 'VIDEOS',
    'mkv': 'VIDEOS',
    'avi': 'VIDEOS',

    # Scripts separately
    'js': 'JS',
    'json': 'JSON',
    'css': 'CSS',
    'html': 'HTML',

    # Others
    'log': 'LOG',
    'pdf': 'PDFS',
    'py': 'PYTHON',
    'txt': 'TXT',
    'zip': 'ZIPS',
    'sk': 'SKRIPT',
    # Add more mappings as needed
}

def discover_existing_folders(dest_root, misc_folder):
    existing_folders = {folder.upper(): os.path.join(dest_root, folder)
                        for folder in os.listdir(dest_root)
                        if os.path.isdir(os.path.join(dest_root, folder)) and folder.upper() != misc_folder}
    # Containing Miscellaneous subfolders
    misc_path = os.path.join(dest_root, misc_folder)
    if os.path.isdir(misc_path):
        for folder in os.listdir(misc_path):
            path = os.path.join(misc_path, folder)
            if os.path.isdir(path):
                existing_folders[f"{misc_folder}\\{folder}".upper()] = path
    return existing_folders

def move_files_by_extension(src, dst):
    existing_folders = discover_existing_folders(dst, misc_folder)
    for root, dirs, files in os.walk(src):    
        for file in files:
            ext = os.path.splitext(file)[1].lower().lstrip('.')
            
            # 1. Choosing custom mappings
            if ext in extension_to_folder:
                folder_name = extension_to_folder[ext]
                dest_folder = os.path.join(dst, folder_name)
                
            # 2. Check if folder already exists
            elif f"{misc_folder}\\{ext.upper()}" in existing_folders:
                dest_folder = existing_folders[f"{misc_folder}\\{ext.upper()}"]
                
            # 3. Default to Miscellaneous subfolder (or NO_EXTENSION)
            elif ext:
                dest_folder = os.path.join(dst, misc_folder, ext.upper())
            else:
                dest_folder = os.path.join(dst, misc_folder, 'NO_EXTENSION')
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
move_files_by_extension(source_dir, dest_root)
print("File transfer complete. Check your ARCHIVES directory to verify.")