"""
ZIPFILE MODULE - COMPREHENSIVE GUIDE FOR PYTHON COMPRESSION
============================================================

***Running this code will create files and directories for better understanding***

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

# ZIPFILE METHODS AND CONSTANTS EXPLAINED
# =======================================

"""
COMPRESSION METHODS:
- zipfile.ZIP_STORED    : No compression, just stores files as-is (fastest, largest size)
- zipfile.ZIP_DEFLATED  : Standard compression using zlib (good balance of speed/size)
- zipfile.ZIP_BZIP2     : High compression using bzip2 (slower, smaller files)
- zipfile.ZIP_LZMA      : Highest compression using LZMA (slowest, smallest files)

ZIPFILE MODES:
- 'r'  : Read existing ZIP file
- 'w'  : Write new ZIP file (overwrites if exists)
- 'a'  : Append to existing ZIP file
- 'x'  : Create new ZIP file, fail if already exists

COMPRESSION LEVELS (for ZIP_DEFLATED):
- compresslevel=0  : No compression (same as ZIP_STORED)
- compresslevel=1  : Fastest compression, larger files
- compresslevel=6  : Default balanced compression
- compresslevel=9  : Maximum compression, slower processing

KEY ZIPFILE METHODS:
- ZipFile()         : Creates/opens ZIP file object
- write()           : Adds individual file to ZIP archive
- writestr()        : Adds string data as file to ZIP archive
- extractall()      : Extracts all files from ZIP to directory
- extract()         : Extracts single file from ZIP
- namelist()        : Returns list of all file names in ZIP
- getinfo()         : Gets detailed info about specific file in ZIP
- close()           : Closes ZIP file (auto-done with 'with' statement)
"""

# ESSENTIAL EXAMPLE 1: Basic ZIP Creation
def create_basic_zip():
    """
    Most common use case - creating ZIP with multiple files
    """
    # zipfile.ZipFile(filename, mode, compression_method)
    # 'w' = write mode (create new ZIP, overwrite if exists)
    # ZIP_DEFLATED = standard compression method (zlib algorithm)
    with zipfile.ZipFile('my_archive.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        # zipf.write(source_file, archive_name)
        zipf.write('file1.txt')                    # Add file as-is (keeps original name)
        zipf.write('file2.txt', 'renamed.txt')     # Add with custom name in archive
    
    print("Basic ZIP created successfully")
    print()

# ESSENTIAL EXAMPLE 2: Directory to ZIP (replaces shutil.make_archive)
def directory_to_zip(directory_path, zip_filename):
    """
    Archive entire directory with full control
    """
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        r"""
        os.walk() EXPLANATION:
        
        root - Current Directory Path
            Type: String
            Contains: The full path to the current directory being processed
            Example: '/home/user/documents', 'C:\\Users\\Documents'

        dirs - Subdirectory Names
            Type: List of strings
            Contains: Names of all subdirectories in the current root directory
            Example: ['folder1', 'images', 'backup']

        files - File Names
            Type: List of strings
            Contains: Names of all files in the current root directory
            Example: ['document.txt', 'photo.jpg', 'data.csv']

        The dirs variable comes from os.walk() which returns (root, dirs, files). Even though we only use files, 
        Python requires us to unpack all three values. 
        The dirs variable contains subdirectory names at each level, but since we're only processing files, it sits unused.
        """
        # os.walk() recursively traverses directory tree
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # os.path.join() creates full file path
                file_path = os.path.join(root, file)
                # os.path.relpath() creates relative path for archive structure
                archive_name = os.path.relpath(file_path, directory_path)
                # Add file to ZIP with preserved directory structure
                zipf.write(file_path, archive_name)
    
    print(f"Directory archived: {zip_filename}")
    print()

# ESSENTIAL EXAMPLE 3: Progress Tracking (Critical for GUI)
def create_zip_with_progress(file_list, zip_filename):
    """
    Progress tracking - essential for GUI applications
    """
    total_files = len(file_list)
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # enumerate() provides index and value for progress calculation
        for i, file_path in enumerate(file_list):
            progress = (i + 1) / total_files * 100  # Calculate percentage
            # os.path.basename() extracts just filename from full path
            filename = os.path.basename(file_path)
            zipf.write(file_path, filename)
            
            # This is where you'd update your GUI progress bar
            print(f"Progress: {progress:.1f}% - Added {filename}")
    
    print("ZIP creation complete with progress tracking")
    print()

# ESSENTIAL EXAMPLE 4: Reading ZIP Contents
def read_zip_info(zip_filename):
    """
    Inspect ZIP without extracting - useful for showing users contents
    """
    # 'r' mode opens ZIP for reading only
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        print(f"Contents of {zip_filename}:")
        # zipf.namelist() returns list of all file names in ZIP
        for filename in zipf.namelist():
            # zipf.getinfo() returns ZipInfo object with file details
            file_info = zipf.getinfo(filename)
            # file_info.file_size = original uncompressed size
            print(f"  {filename} - {file_info.file_size} bytes")
            print()

# ESSENTIAL EXAMPLE 5: Compression Levels
def create_zip_with_compression_control():
    """
    Different compression levels for user choice
    """
    # compresslevel=9: Maximum compression (slowest, smallest file)
    # Range: 0 (no compression) to 9 (maximum compression)
    with zipfile.ZipFile('high_compress.zip', 'w', 
                        zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        zipf.write('large_file.txt')
    
    # compresslevel=1: Fastest compression (faster, larger file)
    with zipfile.ZipFile('fast_compress.zip', 'w', 
                        zipfile.ZIP_DEFLATED, compresslevel=1) as zipf:
        zipf.write('large_file.txt')

    print("ZIP files created with different compression levels")
    print()

# ESSENTIAL EXAMPLE 6: Extracting ZIP Files
def extract_zip(zip_filename, extract_path):
    """
    Extract ZIP with basic control - completes the read/write cycle
    Essential for any compression application
    """
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        # zipf.extractall() extracts all files to specified directory
        # Preserves directory structure from original ZIP
        zipf.extractall(extract_path)
    print(f"Extracted {zip_filename} to {extract_path}")
    print()

# BONUS EXAMPLE: Advanced Compression Methods
def demonstrate_compression_methods():
    """
    Shows different compression algorithms available
    """
    # ZIP_STORED: No compression (fastest)
    with zipfile.ZipFile('stored.zip', 'w', zipfile.ZIP_STORED) as zipf:
        zipf.write('test_file.txt')
    
    # ZIP_DEFLATED: Standard compression (balanced)
    with zipfile.ZipFile('deflated.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write('test_file.txt')
    
    # ZIP_BZIP2: High compression (slower, smaller)
    with zipfile.ZipFile('bzip2.zip', 'w', zipfile.ZIP_BZIP2) as zipf:
        zipf.write('test_file.txt')
    
    # ZIP_LZMA: Maximum compression (slowest, smallest)
    with zipfile.ZipFile('lzma.zip', 'w', zipfile.ZIP_LZMA) as zipf:
        zipf.write('test_file.txt')

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

# CREATE TEST FILES FIRST - This fixes the error!
    print("Creating test files...")
    
    # Create individual test files for basic ZIP example
    with open('file1.txt', 'w') as f:
        f.write('This is the content of file1.txt for testing basic ZIP creation.')
    
    with open('file2.txt', 'w') as f:
        f.write('This is file2.txt content. It will be renamed in the archive.')

    # os.makedirs() creates directory, exist_ok=True prevents error if exists
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

ESSENTIAL ZIPFILE METHODS FOR GUI:
- ZipFile(filename, 'w', ZIP_DEFLATED, compresslevel=6) : Create ZIP with compression
- zipf.write(file_path, archive_name) : Add file to ZIP
- zipf.namelist() : Get list of files in ZIP
- zipf.getinfo(filename) : Get file details
- zipf.extractall(path) : Extract all files

Use the progress tracking example (Example 3) as your foundation - it's perfect
for GUI applications where users need visual feedback during operations.

The key advantage over shutil is that zipfile gives you the control needed
to build professional, user-friendly compression software.
"""
