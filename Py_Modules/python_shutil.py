"""
SHUTIL MODULE REFERENCE GUIDE

****Running this will create certain neccessary files in the current directory for better understanding****

Core Purpose: High-level file and directory operations
Key Strength: Simple, safe, and cross-platform file management
Built on top of os module for more convenient file operations

Learning Path:
Basic file operations (copy, move) → Directory operations (copytree, rmtree) → 
Archive operations → Integration with os and glob

WHAT IS SHUTIL?
shutil (shell utilities) provides high-level file operations similar to shell commands
but with Python-friendly interfaces and better error handling.

-> What is Metadata?

-> Metadata is "data about data." It provides information about a data object, rather than the data itself. 
Examples include file names, creation dates, file sizes, 
and author information for documents, or resolution, color depth, and date taken for images. 
Metadata helps organize, find, and manage data effectively
"""

import shutil
import os
import glob

"""
ESSENTIAL SHUTIL FUNCTIONS:

1. FILE COPYING:
"""
# Always use copy2() unless you specifically need different behavior.
# Create test file
with open('source.txt', 'w') as f:
    f.write('Original content')

# shutil.copy() - Copy file content only
shutil.copy('source.txt', 'copy1.txt')

# shutil.copy2() - Copy file content + metadata (recommended)
shutil.copy2('source.txt', 'copy2.txt')

# shutil.copyfile() - Copy only file content (no permissions)
shutil.copyfile('source.txt', 'copy3.txt')

print("Files copied successfully")
print()

"""
2. FILE MOVING:
"""

# Create test file
with open('temp.txt', 'w') as f:
    f.write('Temporary file')

# shutil.move() - Move/rename file or directory
shutil.move('temp.txt', 'moved.txt')
# shutil.move() removes the original file - it's a true "move" operation, not a copy.
# When using copy2() function, Both 'temp.txt' and 'moved.txt' exist

# Move to different directory
os.makedirs('backup', exist_ok=True)
shutil.move('moved.txt', 'backup/moved.txt')

print("File moved successfully")
print()
"""
3. DIRECTORY OPERATIONS:
"""

# # Create source directory with files
# os.makedirs('source_dir/subdir', exist_ok=True)
# with open('source_dir/file1.txt', 'w') as f:
#     f.write('File 1')
# with open('source_dir/subdir/file2.txt', 'w') as f:
#     f.write('File 2')

# # shutil.copytree() - Copy entire directory tree
# shutil.copytree('source_dir', 'copied_dir')

# shutil.rmtree() - Remove entire directory tree
# shutil.rmtree('copied_dir')  # Uncomment to use(Unsafe to use)

print("Directory operations completed")
print()
"""
4. ARCHIVE OPERATIONS:
"""

# shutil.make_archive() - Create archive
archive_name = shutil.make_archive('my_backup', 'zip', 'source_dir')
# Creates: my_backup.zip (contains all files from source_dir)
print(f"Archive created: {archive_name}")

# shutil.unpack_archive() - Extract archive
shutil.unpack_archive('my_backup.zip', 'extracted')
# Creates: extracted/ folder with all the original files
print("Archive extracted")
print()
"""
5. UTILITY FUNCTIONS:
"""
# This function tells you how much space is available on your disk drive.

# shutil.disk_usage() - Get disk usage
usage = shutil.disk_usage('.')
print(f"Total: {usage.total}\nFree: {usage.free}\nUsed: {usage.used}\n")

def bytes_to_gb(bytes):  # Convert bytes to gigabytes
    """Convert bytes to gigabytes"""
    return bytes / (1024 ** 3)
# To convert bytes to gigabytes (GB), 
# you divide the number of bytes by 1,073,741,824 (which is 1024 cubed, or 2^30)
# For Mb, use: bytes / (1024 ** 2)

usage = shutil.disk_usage('.')  
# usage = shutil.disk_usage('.') gets the disk space statistics (total, used, and free space in bytes) for the current directory's disk drive 
# Provides data in human readable format
print(f"Total: {bytes_to_gb(usage.total):.1f} GB")
print(f"Free: {bytes_to_gb(usage.free):.1f} GB")
print(f"Used: {bytes_to_gb(usage.used):.1f} GB\n")

# shutil.which() - Find executable in PATH
python_path = shutil.which('python')
print(f"Python found at: {python_path}")
print()
"""
PRACTICAL EXAMPLES:

Example 1: Safe File Backup
"""

def backup_file(filename, backup_dir="backups"):
    """Create backup of a file"""
    os.makedirs(backup_dir, exist_ok=True)

    if os.path.exists(filename):
        backup_name = f"backup_{filename}"
        backup_path = os.path.join(backup_dir, backup_name)
        shutil.copy2(filename, backup_path)
        print(f"Backup created: {backup_path}")
    else:
        print(f"File {filename} not found")

# Usage
# backup_file('important.txt')

"""
Example 2: Batch File Operations with Glob
"""

def backup_all_txt_files():
    """Backup all .txt files"""
    os.makedirs('txt_backups', exist_ok=True)
    
    txt_files = glob.glob("*.txt")
    for file in txt_files:
        backup_path = os.path.join('txt_backups', file)
        shutil.copy2(file, backup_path)
        print(f"Backed up: {file}")

# Usage
# backup_all_txt_files()

"""
Example 3: Safe Directory Copy
"""

def safe_copy_directory(source, destination):
    """Copy directory with error handling"""
    try:
        if os.path.exists(destination):
            print(f"Destination {destination} already exists")
            return False
        
        shutil.copytree(source, destination)
        print(f"Copied {source} to {destination}")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

# Usage
# safe_copy_directory('my_project', 'my_project_backup')

"""
Example 4: Clean Trash Function (Alternative to os.remove)
"""

def safe_delete(filename, trash_dir="trash"):
    """Move file to trash instead of permanent deletion"""
    os.makedirs(trash_dir, exist_ok=True)
    
    if os.path.exists(filename):
        # Get just the filename, not full path
        base_filename = os.path.basename(filename)
        trash_path = os.path.join(trash_dir, base_filename)
        
        # Handle duplicates
        counter = 1
        original_trash_path = trash_path
        while os.path.exists(trash_path):
            name, ext = os.path.splitext(original_trash_path)
            trash_path = f"{name}_{counter}{ext}"
            counter += 1
        
        shutil.move(filename, trash_path)
        print(f"Moved {filename} to trash")
    else:
        print(f"File {filename} not found")

# Usage
# safe_delete('unwanted_file.txt')

"""
SHUTIL vs OS MODULE:

Operation           | os module              | shutil module
File Copy          | Manual read/write      | copy(), copy2()
File Move          | rename() (same disk)   | move() (cross-disk)
Directory Copy     | Manual recursion       | copytree()
Directory Remove   | rmdir() (empty only)   | rmtree() (recursive)
Metadata           | Manual preservation    | Automatic with copy2()
"""

"""
COMMON PATTERNS:

1. Always use copy2() instead of copy() for metadata preservation
2. Check if source exists before operations
3. Create destination directories with os.makedirs(exist_ok=True)
4. Use try-except for robust error handling
5. Use os.path.basename() to extract filenames from full paths
"""

def robust_copy(source, destination):
    """Robust file copy with error handling"""
    try:
        # Ensure destination directory exists
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)
        
        shutil.copy2(source, destination)
        print(f"✅ Copied: {source} -> {destination}")
        return True
        
    except FileNotFoundError:
        print(f"❌ Source file not found: {source}")
    except PermissionError:
        print(f"❌ Permission denied")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return False

"""
QUICK REFERENCE:

Function            | Purpose                    | Preserves Metadata
copy()             | Copy file                  | No
copy2()            | Copy file + metadata       | Yes (recommended)
copyfile()         | Copy content only          | No
move()             | Move/rename                | Yes
copytree()         | Copy directory tree        | Yes
rmtree()           | Remove directory tree      | N/A
make_archive()     | Create zip/tar archive     | Yes
unpack_archive()   | Extract archive            | Yes
disk_usage()       | Get disk space info        | N/A
which()            | Find executable path       | N/A

MEMORY AID:
- copy2() = copy() + metadata (always prefer this)
- move() works across filesystems (unlike os.rename())
- copytree() fails if destination exists
- rmtree() permanently deletes (use safe_delete() instead)
- Always handle exceptions for production code

CONCEPT SUMMARY:
Core Purpose: High-level file operations
Key Functions: copy2(), move(), copytree(), rmtree()
Best Practice: Always use copy2() and handle exceptions
Integration: Works well with os.path and glob modules
"""

# Simple cleanup function
def cleanup_examples():
    """Clean up example files"""
    files = ['source.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt', 'my_backup.zip']
    dirs = ['backup', 'source_dir', 'copied_dir', 'extracted', 'trash', 'txt_backups']
    
    for file in files:
        if os.path.exists(file):
            os.remove(file)
    
    for dir in dirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)
    
    print("Cleanup completed")

# cleanup_examples()  # Uncomment to clean up
