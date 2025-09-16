# ArchiveSorter 📂

**A Python-based automated file archive organizer.**

Keeps your downloads and miscellaneous files neatly organized by sorting files from a source directory into categorized folders based on the file type.

---

## 🚀 Features

- 🗂️ **Automated File Sorting** — Organizes files by their extension into dedicated folders like `IMAGES`, `VIDEOS`, `AUDIOS`, etc.
- 🔄 **Recursive Reorganization** — Detects and relocates misplaced files inside the archive for future-proof cleanups.
- 🎵 **Audio File Support** — Sorts common audio files (mp3, wav, flac, etc.) into an `AUDIOS` folder.
- 📁 **Dynamic Folder Creation** — Creates destination folders automatically for new file types.
- 🔢 **File Count Suffix Toggle** — Optionally appends `(File Count - N)` to folder names; can be turned on or off via the `ENABLE_FILE_COUNT` variable.
- 📊 **Centralized Metadata Tracking** — Maintains file counts in a `.filecount_metadata/metadata.json` for efficient operations.
- **Safe Duplicate Filename Handling** — Renames files with conflicting names to avoid overwriting.

---

## 📂 How It Works

The script scans your `source_dir` and moves files into specific archive folders inside `dest_root`. It also recursively scans the entire destination archive to correct any misplaced files based on the current rules.

---

## ⚙️ Configuration

- **Source Directory:** Set via the `source_dir` variable.
- **Destination Directory:** Set via the `dest_root` variable.
- **File Count Suffix:** Enable or disable with the `ENABLE_FILE_COUNT` boolean.
- **Extension Mapping:** Customize the `extension_to_folder` dictionary inside the script.

---

## 🧰 Usage

1. Make sure Python 3.x is installed.
2. Configure the paths and toggle within the script.
3. Run the script:
```
python src/ArchiveSorter.py
```
4. Check the archive folders for organized files.