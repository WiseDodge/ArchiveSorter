# ArchiveSorter 📂

**A Python-based automated file archive organizer.**

Keeps your downloads and miscellaneous files neatly organized by sorting files from a source directory into categorized folders based on the file type.

---

## 🚀 Features

- 🗂️ **Automated File Sorting** — Organizes files by their extension into dedicated folders like `IMAGES`, `VIDEOS`, etc.
- **Dynamic Folder Creation** — Creates destination folders automatically for new file types.
- 🔢 **File Count Suffix** — Appends `(File Count - N)` to folder names to track contents.
- 📊 **Metadata Tracking** — Maintains file counts in a `.filecount_metadata` folder for efficient updates.
- **Safe Duplicate Filename Handling** — Renames files with conflicting names to avoid overwriting.

---

## 📂 How It Works

The script scans your `source_dir` and moves files into specific archive folders inside `dest_root`. Files with unknown or no extensions go into a `MISCELLANEOUS` folder. It then updates folder names to reflect their current file counts.

---

## ⚙️ Configuration

- **Source Directory:** Set via the `source_dir` variable.
- **Destination Directory:** Set via the `dest_root` variable.
- **Extension Mapping:** Customize the `extension_to_folder` dictionary inside the script.

---

## 🧰 Usage

1. Make sure Python 3.x is installed.
2. Configure the paths within the script.
3. Run the script: 
```
python src/ArchiveSorter.py
```
4. Check the archive folders for organized files.