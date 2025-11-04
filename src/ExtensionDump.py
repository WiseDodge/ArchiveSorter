import os
from collections import Counter

def get_extension(filename):
    compound_exts = ['.tar.gz', '.tar.xz', '.tar.bz2']
    filename_lower = filename.lower()
    for ext in compound_exts:
        if filename_lower.endswith(ext):
            return ext[1:]
    return os.path.splitext(filename_lower)[1][1:]

def count_file_extensions(directory):
    extensions = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = get_extension(file)
            if ext:
                extensions.append(ext)
    extension_counts = Counter(extensions)
    return extension_counts

directory_path = r'D:\Downloads'
results = count_file_extensions(directory_path)

for ext, count in results.items():
    print(f"{ext.upper()}: {count}")