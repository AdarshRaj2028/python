"""
ZIPFILE MODULE - COMPREHENSIVE GUIDE FOR PYTHON COMPRESSION
============================================================

The zipfile module is Python's built-in library for creating, reading, writing, 
and extracting ZIP archive files. It provides low-level control over ZIP operations
and is much more powerful than shutil for ZIP-specific tasks.

KEY CONCEPTS:
- Direct ZIP file manipulation without external dependencies
- Fine-grained control over compression methods and levels
- Ability to add/extract individual files from archives
- Support for encrypted ZIP files and advanced ZIP features
- Memory-efficient streaming operations for large files

WHEN TO USE ZIPFILE:
- Need custom compression settings
- Want progress tracking during compression
- Working with individual files in archives
- Building GUI applications with user feedback
- Memory-constrained environments
- Advanced ZIP features (encryption, ZIP64)

WHEN TO USE SHUTIL INSTEAD:
- Quick directory archiving (one-liner)
- Multiple archive formats (TAR, GZIP, etc.)
- Simple scripting tasks
- Don't need fine control over compression
"""

# BASIC ZIPFILE OPERATIONS
# ========================

import zipfile
import os
import glob

# ESSENTIAL EXAMPLE 1: Basic ZIP Creation
def create_basic_zip():
    """
    Most common use case - creating ZIP with multiple files
    """
    with zipfile.ZipFile('my_archive.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write('file1.txt')                    # Add file as-is
        zipf.write('file2.txt', 'renamed.txt')     # Add with custom name
    
    print("Basic ZIP created successfully")

# ESSENTIAL EXAMPLE 2: Directory to ZIP (replaces shutil.make_archive)
def directory_to_zip(directory_path, zip_filename):
    """
    Archive entire directory with full control
    """
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                archive_name = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, archive_name)
    
    print(f"Directory archived: {zip_filename}")

# ESSENTIAL EXAMPLE 3: Progress Tracking (Critical for GUI)
def create_zip_with_progress(file_list, zip_filename):
    """
    Progress tracking - essential for GUI applications
    """
    total_files = len(file_list)
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i, file_path in enumerate(file_list):
            progress = (i + 1) / total_files * 100
            filename = os.path.basename(file_path)
            zipf.write(file_path, filename)
            
            # This is where you'd update your GUI progress bar
            print(f"Progress: {progress:.1f}% - Added {filename}")
    
    print("ZIP creation complete with progress tracking")

# ESSENTIAL EXAMPLE 4: Reading ZIP Contents
def read_zip_info(zip_filename):
    """
    Inspect ZIP without extracting - useful for showing users contents
    """
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        print(f"Contents of {zip_filename}:")
        for filename in zipf.namelist():
            file_info = zipf.getinfo(filename)
            print(f"  {filename} - {file_info.file_size} bytes")

# ESSENTIAL EXAMPLE 5: Compression Levels
def create_zip_with_compression_control():
    """
    Different compression levels for user choice
    """
    # High compression (slower, smaller file)
    with zipfile.ZipFile('high_compress.zip', 'w', 
                        zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        zipf.write('large_file.txt')
    
    # Fast compression (faster, larger file)
    with zipfile.ZipFile('fast_compress.zip', 'w', 
                        zipfile.ZIP_DEFLATED, compresslevel=1) as zipf:
        zipf.write('large_file.txt')

# ESSENTIAL EXAMPLE 6: Extracting ZIP Files
def extract_zip(zip_filename, extract_path):
    """
    Extract ZIP with basic control - completes the read/write cycle
    Essential for any compression application
    """
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extractall(extract_path)
    print(f"Extracted {zip_filename} to {extract_path}")

# ZIPFILE vs SHUTIL COMPARISON
# =============================

    """
    ZIPFILE MODULE:
    Pros:
    - Fine control over compression (methods, levels)
    - Progress tracking capability
    - Add files to existing archives
    - Memory-efficient operations
    - Read archive contents without extraction
    - Custom file paths in archive
    - ZIP-specific features (encryption, ZIP64)
    - Better for GUI applications
    
    Cons:
    - More code required
    - Only handles ZIP format
    - Manual directory traversal needed
    - More complex for simple tasks
    
    SHUTIL MODULE:
    Pros:
    - One-line archive creation
    - Handles multiple formats (ZIP, TAR, GZIP, etc.)
    - Automatic directory handling
    - Simpler code
    - Cross-platform consistency
    
    Cons:
    - No progress tracking
    - No compression control
    - Can't add to existing archives
    - Less flexible file organization
    - Only basic archiving operations
    
    WHEN TO USE WHAT:
    
    Use ZIPFILE when:
    - Building GUI applications (need progress bars)
    - Need custom compression settings
    - Working with individual files in archives
    - Want memory-efficient operations
    - Need advanced ZIP features
    - Building professional software
    
    Use SHUTIL when:
    - Quick scripting tasks
    - Simple directory compression
    - Need multiple archive formats
    - Don't need fine control
    - Prototyping or one-off tasks
    """

# PRACTICAL EXAMPLES YOU CAN RUN
# ===============================

if __name__ == "__main__":
    # Create test files
    os.makedirs('test_files', exist_ok=True)
    with open('test_files/sample1.txt', 'w') as f:
        f.write('Sample file 1 content')
    with open('test_files/sample2.txt', 'w') as f:
        f.write('Sample file 2 with more content for compression testing')
    
    # Run essential examples
    print("=== ZIPFILE ESSENTIALS DEMO ===")
    
    # Basic ZIP creation
    create_basic_zip()
    
    # Directory archiving
    directory_to_zip('test_files', 'folder_archive.zip')
    
    # Progress tracking
    file_list = ['test_files/sample1.txt', 'test_files/sample2.txt']
    create_zip_with_progress(file_list, 'progress_example.zip')
    
    # Read ZIP contents
    read_zip_info('folder_archive.zip')
    
    # Extract ZIP files
    os.makedirs('extracted_folder', exist_ok=True)
    extract_zip('folder_archive.zip', 'extracted_folder')
    
    print("\nFiles created: my_archive.zip, folder_archive.zip, progress_example.zip")
    print("Extraction completed to: extracted_folder/")

"""
SUMMARY FOR YOUR GUI COMPRESSOR:
================================

For your Python GUI compressor program, zipfile module is the better choice because:

1. PROGRESS TRACKING: You can show users real-time progress during compression
2. USER CONTROL: Users can choose compression levels and methods
3. FLEXIBILITY: Add individual files or entire directories as needed
4. PROFESSIONAL FEATURES: Handle edge cases and provide detailed feedback
5. MEMORY EFFICIENT: Better for large files that might exceed memory
6. COMPLETE WORKFLOW: Create, read, and extract ZIP files with full control

Use the progress tracking example (Example 3) as your foundation - it's perfect
for GUI applications where users need visual feedback during operations.

The key advantage over shutil is that zipfile gives you the control needed
to build professional, user-friendly compression software.
"""
