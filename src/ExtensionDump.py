import os
from collections import Counter

def count_file_extensions(directory):
    extensions = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext:
                extensions.append(ext[1:])  # Removes the '.' from the extension
    extension_counts = Counter(extensions)
    return extension_counts

directory_path = r'D:\Downloads'
results = count_file_extensions(directory_path)

for ext, count in results.items():
    print(f"{ext.upper()}: {count}")