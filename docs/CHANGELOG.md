# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **Core File Sorting Engine**: Organizes files from a source directory into a destination archive based on `extension_to_folder` mappings.
- **Recursive Internal Reorganization**: Added a self-correcting feature that recursively scans the entire destination archive to detect and move misplaced files.
- **Dynamic Folder Creation**: Automatically creates destination folders for new file types, including subfolders under `MISCELLANEOUS` for unknown extensions.
- **File Count Suffix Toggle**: Introduced a global boolean `ENABLE_FILE_COUNT` to control the inclusion of the `(File Count - N)` suffix in folder names.
- **Metadata Management**: Creates per-folder JSON files to track file counts and determine when to rename folders.
- **Safe Duplicate Filename Handling**: Renames files with conflicting names in the destination to avoid overwriting.

### Changed
- **Enhanced File Moving Logic**: The script now discovers existing folders before moving files to avoid creating duplicates.
- **Metadata Storage Evolution**: Migrated from per-folder JSON files to a single centralized metadata file for efficiency.

### Fixed
- **Windows Naming Errors**: Updated folder suffix format from `[File Count: N]` to `(File Count - N)` to prevent filesystem errors.

### Upcoming Features & Improvements
- **Advanced Duplicate Detection**
- **Metadata Enrichment**
- **Incremental Reorganization**
- **Date-Based Sorting**
- **Improved Usability and Documentation**