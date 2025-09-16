# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-07-31

This version marks a major milestone establishing the foundation of ArchiveSorter, including a robust organizational engine, metadata tracking, and self-correcting archive maintenance.

### Added
- **Core File Sorting Engine**: Organizes files from a source directory into a destination archive based on customizable `extension_to_folder` mappings.
- **Recursive Internal Reorganization**: Added a self-correcting feature that recursively scans the entire destination archive (`dest_root`) to detect and move misplaced files.
- **Audio File Mapping**: Explicit mapping for common audio formats such as `.mp3`, `.wav`, `.flac`, etc., routing these files into a dedicated `AUDIOS` folder.
- **File Count Suffix Toggle**: Introduced a global boolean `ENABLE_FILE_COUNT` to control the inclusion of the `(File Count - N)` suffix in folder names.
- **Centralized Metadata Management**: Refactored metadata handling from per-folder JSON files to a single centralized `.filecount_metadata/metadata.json`.
- **Safe Duplicate Filename Handling**: Files with conflicting names in the destination are renamed to avoid overwriting.
- **Dynamic Folder Creation**: Destination folders are created automatically as new file types are encountered.

### Changed
- **Metadata Storage Evolution**: Consolidated per-folder JSON files into one centralized `metadata.json` for clarity and reliability.

### Fixed
- **Windows Naming Errors**: Updated the folder suffix format from `[File Count: N]` to `(File Count - N)` for filesystem compatibility.

---

## [PLANNED]

### Upcoming Features & Improvements
- **Advanced Duplicate Detection**: Utilize SHA-256 hashing to detect exact duplicate files.
- **Metadata Enrichment**: Extend the centralized `metadata.json` to store per-file hashes, modification timestamps, and rename history.
- **Incremental Reorganization**: Optimize subsequent runs by processing only folders that have changed.
- **Date-Based Sorting**: Add functionality to organize files by year and month.
- **Improved Usability and Documentation**: Create a detailed README with configuration examples and usage instructions.