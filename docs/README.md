# ArchiveSorter 📂
![GitHub last commit](https://img.shields.io/github/last-commit/WiseDodge/ArchiveSorter)

**A file management system for turning digital chaos into a clean, organized archive.**

ArchiveSorter uses a powerful Python script to systematically sort files into a detailed, nested structure, making it effortless to locate what you need. For added flexibility, companion scripts are included to flatten the entire archive for bulk tasks or analyze your file types to help you refine your organization.

---
## ✨ Showcase

**1. Organize with `ArchiveSorter.py`**

Automatically sorts a messy folder into an elegant, nested structure so you can find files easily.

![ArchiveSorter Demo](https://raw.githubusercontent.com/WiseDodge/ArchiveSorter/main/docs/assets/ArchiveSorter-Demo.gif)

**2. Consolidate with `FileConsolidator.ps1`**

Safely reverses the process, moving all files from the nested archive back into a single, flat folder for tasks like bulk transfers.

![FileConsolidator Demo](https://raw.githubusercontent.com/WiseDodge/ArchiveSorter/main/docs/assets/FileConsolidator-Demo.gif)

---

## 🚀 Features

- 🗂️ **Elegant File Sorting** — Organizes files by extension into a detailed, nested folder structure like `MEDIA/IMAGES` or `ARCHIVES/ZIPS`.
- 🔄 **Recursive Reorganization** — Automatically scans the entire archive to find and move any misplaced files, ensuring long-term organization.
- ⚡ **Instant Consolidation** — A companion PowerShell script (`FileConsolidator.ps1`) can instantly and safely flatten the entire archive back into a single folder and clean up empty directories.
- 🔍 **File Analysis** — A utility script (`ExtensionDump.py`) quickly scans a directory and reports a count of every file extension, helping you discover what needs organizing.
- 🛡️ **Safe & Reversible** — All scripts are non-destructive. Duplicate files are renamed to prevent overwriting, and the entire process is fully reversible.
- ⚙️ **Portable & Configurable** — Scripts use optional command-line arguments with default paths, making them convenient for personal use and easily shareable.

---

## 🛠️ The Scripts

This project contains three main scripts located in the `src/` directory:

1.  **`ArchiveSorter.py`**: The main Python script. It scans a source directory and moves files into the elegant nested folder structure. It also performs a "self-healing" scan to correct any misplaced files within the archive.
2.  **`FileConsolidator.ps1`**: A PowerShell script that does the reverse. It recursively scans the organized archive, moves every file back into a single destination folder, and then safely cleans up the now-empty subdirectories.
3.  **`ExtensionDump.py`**: A simple Python utility that scans a directory and prints a list of all file extensions and how many of each were found. This is useful for discovering new file types to add to the `ArchiveSorter` configuration.

---

## 📂 Default Folder Structure

By default, `ArchiveSorter.py` will organize your files into the following elegant structure:

```

\<Destination\>/
├───ARCHIVES/
│   ├───BINARY/
│   ├───DISK_IMAGES/
│   ├───LIBRARIES/
│   ├───PROGRAMS/
│   ├───REGISTRY/
│   ├───VPN/
│   └───ZIPS/
│
├───DEVELOPMENT/
│   ├───COMPILED/
│   ├───CONFIG/
│   ├───CSHARP/
│   ├───CSS/
│   ├───HTML/
│   ├───JAVASCRIPT/
│   ├───JSON/
│   ├───LOGS/
│   ├───PYTHON/
│   ├───SCRIPTS/
│   ├───SKRIPT/
│   ├───XML/
│   └───YAML/
│
├───DOCUMENTS/
│   ├───EXCEL/
│   ├───MARKDOWN/
│   ├───PDFS/
│   ├───POWERPOINT/
│   ├───TEXT/
│   └───WORD/
│
├───FONTS/
│
├───GAMING/
│   ├───COD/
│   ├───MINECRAFT/
│   │   ├───MODPACKS/
│   │   ├───RESOURCE_PACKS/
│   │   ├───SCHEMATICS/
│   │   ├───SCRIPTS/
│   │   └───WORLD_DATA/
│   └───OSU/
│
├───MEDIA/
│   ├───3D\_MODELS/
│   ├───AUDIO/
│   │   ├───AAC/
│   │   ├───FLAC/
│   │   ├───M4A/
│   │   ├───MP3/
│   │   ├───OGA/
│   │   ├───OGG/
│   │   └───WAV/
│   ├───GIFS/
│   ├───IMAGES/
│   ├───SUBTITLES/
│   └───VIDEOS/
│
└───MISCELLANEOUS/

````

---

## 🧰 Usage

### 1. Analyzing Your Files (`ExtensionDump.py`)
Run this first to see what file types you have.
```bash
python src/ExtensionDump.py
````

### 2\. Organizing Your Files (`ArchiveSorter.py`)

Configure the `extension_to_folder` dictionary in the script, then run it from the terminal.

**Example:**

```bash
# Use default paths (e.g., D:\Downloads -> D:\...\DATABASE)
python src/ArchiveSorter.py

# Specify custom paths
python src/ArchiveSorter.py --source "C:\MyMessyFolder" --destination "D:\MyNeatArchive"
```

### 3\. Consolidating Your Archive (`FileConsolidator.ps1`)

Run the script from a PowerShell terminal to flatten your archive.

**Example:**

```powershell
# Use default paths (e.g., D:\...\DATABASE -> D:\Downloads)
.\src\FileConsolidator.ps1

# Specify custom paths
.\src\FileConsolidator.ps1 -Source "D:\MyNeatArchive" -Destination "C:\Temp\AllFiles"
```
