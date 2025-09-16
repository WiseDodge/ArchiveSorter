# ArchiveSorter 📂

**A Python-based automated file archive organizer.**

Keeps your downloads and miscellaneous files neatly organized by sorting files from a source directory into a categorized, nested folder structure.

---

## 🚀 Features

- 🗂️ **Automated File Sorting** — Organizes files by extension into a detailed, nested folder structure like `MEDIA/IMAGES` or `ARCHIVES/ZIPS`.
- 🔄 **Recursive Reorganization** — Automatically scans the entire archive to find and move any misplaced files, ensuring long-term organization.
- 🎵 **Comprehensive File Support** — Intelligently sorts a wide range of files including documents, media, development files, archives, fonts, and gaming files.
- 🔢 **File Count Suffix Toggle** — Optionally appends `(File Count - N)` to folder names for quick reference.
- 📊 **Centralized Metadata Tracking** — Uses a single `metadata.json` file for efficient state tracking.
- **Safe Duplicate Handling** — Prevents data loss by automatically renaming files with conflicting names.

---

## 📂 How It Works

The script scans your `source_dir` and moves files into the elegant nested folder structure inside `dest_root`. It also recursively scans the destination archive to correct any misplaced files based on the current rules, making it self-healing.

---

## ⚙️ Configuration

- **Source Directory:** Set via the `source_dir` variable.
- **Destination Directory:** Set via the `dest_root` variable.
- **File Count Suffix:** Enable or disable with the `ENABLE_FILE_COUNT` boolean.
- **Extension Mapping:** Fully customize the `extension_to_folder` dictionary to match your needs.

---

## 🧰 Usage

1. Make sure Python 3.x is installed.
2. Configure the paths and the `extension_to_folder` mapping in the script.
3. Run the script:
```
python src/ArchiveSorter.py
```
4. Check the archive folders for organized files.