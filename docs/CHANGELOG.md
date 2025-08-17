# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **Core File Sorting Engine**: Organizes files from a source directory into a destination archive based on the `extension_to_folder` mappings.
- **Dynamic Folder Creation**: Automatically creates destination folders for the corresponding new file types, including the subfolders under `MISCELLANEOUS` for undefined/unknown extensions.
- **Safe Duplication Filename Handling**: Renames files that have conflicting names in the destination to avoid overwriting.

### Upcoming Features & Improvements
- **Advanced Duplicate Detection**
- **Metadata Enrichment**
- **Incremental Reorganization**
- **Date-Based Sorting**
- **Improved Usability and Documentation**