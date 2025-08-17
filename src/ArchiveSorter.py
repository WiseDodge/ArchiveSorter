import os
import shutil

source_dir = r'D:\Downloads'
dest_root = r'D:\CODING\ARCHIVES'

# Your custom folder mapping by extensions (lowercase keys)
extension_to_folder = {
    # Images merged into one folder except gif separately
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
}

misc_folder = 'MISCELLANEOUS'

for root, dirs, files in os.walk(source_dir):
    for file in files:
        ext = os.path.splitext(file)[1].lower().lstrip('.')
        if not ext:
            # Files without extension go into miscellaneous root folder
            dest_folder = os.path.join(dest_root, misc_folder, 'NO_EXTENSION')
        else:
            # Known extensions use mapped folders
            if ext in extension_to_folder:
                dest_folder = os.path.join(dest_root, extension_to_folder[ext])
            else:
                # Unknown extensions go into a subfolder within miscellaneous
                dest_folder = os.path.join(dest_root, misc_folder, ext.upper())

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
    break  # Only top-level files processed

print("File transfer complete. Check your ARCHIVES directory to verify.")