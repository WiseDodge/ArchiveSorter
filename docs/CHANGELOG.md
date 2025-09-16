# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-09-16

This version marks the first stable release of ArchiveSorter, featuring a robust organizational engine, a companion file consolidator, and numerous refinements for stability and portability.

### Added
- **Elegant Nested Folder Structure**: Implemented a comprehensive, multi-level folder hierarchy for superior organization (e.g., `MEDIA/IMAGES`, `ARCHIVES/ZIPS`).
- **Recursive Internal Reorganization**: Added a self-correcting feature that recursively scans the entire destination archive to detect and move misplaced files.
- **Companion PowerShell Script (`FileConsolidator.ps1`)**: Added a powerful utility to flatten the entire archive back into a single folder, with an integrated cleanup phase to remove the now-empty source directories.
- **Comprehensive File Type Support**: Massively expanded the `extension_to_folder` mapping to cover documents, media, development files, archives, fonts, and gaming files based on user-specific needs.
- **File Count Suffix Toggle**: Introduced a global boolean `ENABLE_FILE_COUNT` to control the `(File Count - N)` suffix.

### Changed
- **Improved Portability**: Refactored both the Python and PowerShell scripts to use optional command-line arguments with default values, removing hardcoded paths to make them usable on any machine.
- **Project Goal**: Evolved from a simple sorter to a comprehensive archive management tool with a focus on an elegant, maintainable folder structure.
- **Code Refinements**: Removed all unused variables and refined internal logic in both scripts for better readability and efficiency.

### Fixed
- **Python Encoding Errors**: Made all `print` statements and error handlers in `ArchiveSorter.py` robust against filenames with special Unicode characters, preventing crashes.
- **PowerShell Wildcard Errors**: Updated `FileConsolidator.ps1` to use `-LiteralPath` to correctly handle filenames containing special characters like `[` and `]`.
- **PowerShell File Discovery**: Added the `-Force` parameter to the PowerShell script to ensure it correctly finds and moves hidden and system files.
- **Windows Naming Errors**: Updated the folder suffix format to be filesystem-compatible.

---

## [PLANNED]

### Upcoming Features & Improvements
- **Advanced Duplicate Detection**: Utilize SHA-256 hashing to detect exact duplicate files.
- **Metadata Enrichment**: Extend `metadata.json` to store per-file hashes and timestamps for incremental operations.
- **Date-Based Sorting**: Add functionality to organize files by year and month.