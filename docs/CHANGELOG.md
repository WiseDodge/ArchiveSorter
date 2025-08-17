# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **Core File Sorting Engine**: Organizes files from a source directory into a destination archive based on `extension_to_folder` mappings.
- **Dynamic Folder Creation**: Automatically creates destination folders for new file types, including subfolders under `MISCELLANEOUS` for unknown extensions.
- **Safe Duplicate Filename Handling**: Renames files with conflicting names in the destination to avoid overwriting.

### Changed
- **Enhanced File Moving Logic**: The script now discovers existing folders before moving files to avoid creating duplicates.

### Upcoming Features & Improvements
- **Advanced Duplicate Detection**
- **Metadata Enrichment**
- **Incremental Reorganization**
- **Date-Based Sorting**
- **Improved Usability and Documentation**