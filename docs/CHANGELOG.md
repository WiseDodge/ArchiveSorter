# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-09-16

This version marks the first stable release of ArchiveSorter, featuring a robust organizational engine, metadata tracking, a self-correcting archive, and a highly detailed, elegant folder structure.

### Added
- **Elegant Nested Folder Structure**: Implemented a comprehensive, multi-level folder hierarchy for superior organization (e.g., `MEDIA/IMAGES`, `ARCHIVES/ZIPS`).
- **Recursive Internal Reorganization**: Added a self-correcting feature that recursively scans the entire destination archive to detect and move misplaced files.
- **Comprehensive File Type Support**: Massively expanded the `extension_to_folder` mapping to cover documents, media, development files, archives, fonts, and gaming files.
- **File Count Suffix Toggle**: Introduced a global boolean `ENABLE_FILE_COUNT` to control the `(File Count - N)` suffix.
- **Centralized Metadata Management**: Uses a single `metadata.json` for efficient state tracking.

### Changed
- **Project Goal**: Evolved from a simple sorter to a comprehensive archive management tool with a focus on an elegant, maintainable folder structure.
- **Code Refinements**: Removed all unused variables and refined internal logic for better readability and efficiency.

### Fixed
- **Windows Naming Errors**: Updated the folder suffix format to be filesystem-compatible.
- **Nested Path Handling**: Corrected logic in all functions to properly create and recognize nested folder paths.

---

## [PLANNED]

### Upcoming Features & Improvements
- **Advanced Duplicate Detection**: Utilize SHA-256 hashing to detect exact duplicate files.
- **Metadata Enrichment**: Extend the `metadata.json` to store per-file hashes and timestamps for incremental operations.
- **Incremental Reorganization**: Optimize subsequent runs by processing only folders that have changed.
- **Date-Based Sorting**: Add functionality to organize files by year and month.