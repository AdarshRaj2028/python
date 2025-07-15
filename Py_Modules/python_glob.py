"""
GLOB MODULE COMPLETE REFERENCE GUIDE

****Running this will create certain neccessary files in the current directory for better understanding****

Core Purpose & Key Strength:
- File pattern matching using shell-style wildcards
- Simple, intuitive syntax for complex file operations
- Cross-platform compatibility
- Built into Python standard library

Learning Path:
Start with basic wildcards (*, ?) → Advanced patterns ([], **) → Iterator usage → Integration with os.path

ESSENTIAL PATTERNS TO MASTER:

1. Basic Wildcards:
"""

import glob 

# *.ext - All files with extension
txt_files = glob.glob("*.txt")
print("All .txt files:", txt_files)

# test_files = ['data.txt', 'data.csv', 'database.db', 'data_backup.zip', 'info.txt']
# for file in test_files:
#     with open(file, 'w') as f:
#         f.write('test content')

# prefix* - All files starting with prefix
data_files = glob.glob("data*")
print("Files starting with 'data':", data_files)
# Examples: 'data.txt', 'data.csv', 'database.db', 'data_backup.zip'

# ? - Single character wildcard
single_char = glob.glob("?.py")
print("Single character .py files:", single_char)
# Examples: 'a.py', 'b.py', 'c.py'

# Multiple characters
three_chars = glob.glob("???.py")
print("Three character .py files:", three_chars)
# 'app.py', 'run.py'
# Note: Only files with EXACTLY 3 characters before .py
print()

"""
2. Character Classes ([]):
"""

# Create test files
numbered_files = ['file1.txt', 'file2.txt', 'file9.txt', 'fileA.txt']
for file in numbered_files:
    with open(file, 'w') as f:
        f.write('test')

# file[0-9].ext - Character class matching
numbered = glob.glob("file[1-5].txt")
print("Files 1-5:", numbered)  # ['file1.txt', 'file2.txt']

# Specific characters
specific = glob.glob("file[129].txt")
print("Files with 1, 2, or 9:", specific)  # ['file1.txt', 'file2.txt', 'file9.txt']

# Any single character
any_char = glob.glob("file?.txt")
print("Files with any character:", any_char)  # All files matching pattern
print()

"""
3. Recursive Search (**):
"""

import os

# Create directory structure first
os.makedirs('project/src', exist_ok=True)
os.makedirs('project/tests', exist_ok=True)

# Create test files
with open('project/main.py', 'w') as f: f.write('print("main")')
with open('project/src/utils.py', 'w') as f: f.write('print("utils")')
with open('project/tests/test_main.py', 'w') as f: f.write('print("tests")')

# **/*.ext - Recursive search (REMEMBER: recursive=True)
all_py = glob.glob("project/**/*.py", recursive=True)
print("All Python files:", all_py)
print()
"""
KEY METHODS COMPARISON:

glob.glob() vs glob.iglob():
"""

# glob() - Returns list (loads everything into memory)
file_list = glob.glob("*.txt")
print("glob() returns:", type(file_list), file_list)

# iglob() - Returns iterator (memory efficient for large directories)
file_iterator = glob.iglob("*.txt")
print("iglob() returns:", type(file_iterator))

# Use iterator in loop
for file in glob.iglob("*.txt"):
    print(f"Found: {file}")
print()
"""
glob.escape():
"""

# Escape special characters in filenames
with open("file[1].txt", 'w') as f: f.write('test content')
escaped = glob.escape("file[1].txt")  # Treats brackets literally
files = glob.glob(escaped)
print("Escaped files:", files)
print()
r"""
CROSS-PLATFORM PATH HANDLING:

Path Separators Problem:
- Windows: Uses backslash \ (e.g., C:\Users\Documents\file.txt)
- Unix/Linux/macOS: Uses forward slash / (e.g., /home/user/documents/file.txt)

Solution: Always Use os.path.join():
"""

import os
import glob

# ❌ Wrong way (not portable)
# windows_pattern = "project\\src\\*.py"  # Only works on Windows
# unix_pattern = "project/src/*.py"       # Only works on Unix/Linux/macOS

# ✅ Right way (portable across all OS)
portable_pattern = os.path.join("project", "src", "*.py")
files = glob.glob(portable_pattern)

# Building paths from current directory
current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'funny_dir', 'data', '*.csv')  
# Portable, I.E. we can add the directory we want to reach after current directory
print("Portable file path:", file_path)
print()
"""
COMMON GOTCHAS & SOLUTIONS:

1. Hidden Files:
"""
# Regular glob doesn't find hidden files by default
with open('.hidden.txt', 'w') as f:
    f.write('hidden content')

regular = glob.glob("*.txt")
print("Regular search:", regular)  # Won't include .hidden.txt

# To find hidden files, be explicit
hidden = glob.glob(".*txt")
print("Hidden files:", hidden)  # ['.hidden.txt']

"""
2. Recursive Patterns:
"""

# ❌ Wrong - Missing recursive=True
files = glob.glob("**/*.py")  # Won't work recursively

# ✅ Correct - Include recursive=True
files = glob.glob("**/*.py", recursive=True)
"""
3. Memory Efficiency:
"""

# For large directories, prefer iglob() over glob()
# ❌ Memory intensive for large results
all_files = glob.glob("**/*", recursive=True)

# ✅ Memory efficient
for file in glob.iglob("**/*", recursive=True):
    # process_file(file)
    pass

"""
SAFE FILE OPERATIONS:

Alternative to os.remove() - Trash System:
"""

import shutil
import os

# Create trash directory
trash_dir = "trash"
os.makedirs(trash_dir, exist_ok=True)

def safe_delete(filename):
    """Move file to trash instead of permanent deletion"""
    if os.path.exists(filename):
        base_filename = os.path.basename(filename)
# The os.path.basename(filename) function extracts the file name (or directory name) from a complete file path,
# removing all the directory path information.
        trash_path = os.path.join(trash_dir, base_filename)
        shutil.move(filename, trash_path)
        print(f"Moved {filename} to trash")
    else:
        print(f"File {filename} not found")

with open("Py_Modules/exp.py", 'w') as f: f.write('print("exp")')

dir = os.path.join(current_dir,'Py_Modules', 'exp.py')
safe_delete(dir)

# Usage - File moved to trash, not permanently deleted
# safe_delete("myfile.txt")

"""
Backup Before Delete:
"""

from datetime import datetime

def backup_and_delete(filename):
    """Create backup before deleting"""
    if os.path.exists(filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{filename}.backup_{timestamp}"
        shutil.copy2(filename, backup_name)
        print(f"Backup created: {backup_name}")
        os.remove(filename)

"""
CLEANUP SCRIPT TEMPLATE:
"""

import glob
import os
import shutil

def cleanup_files():
    """Safe cleanup with trash system"""
    # Patterns to clean
    cleanup_patterns = [
        "*.tmp", "temp_*", "*.log",
        "file*.txt", ".hidden.txt"
    ]
    
    # Create trash directory
    trash_dir = "cleanup_trash"
    os.makedirs(trash_dir, exist_ok=True)
    
    for pattern in cleanup_patterns:
        files = glob.glob(pattern)
        for file in files:
            try:
                # Move to trash instead of permanent deletion
                trash_path = os.path.join(trash_dir, os.path.basename(file))
                shutil.move(file, trash_path)
                print(f"Moved to trash: {file}")
            except Exception as e:
                print(f"Error moving {file}: {e}")

# cleanup_files()  # Uncomment to use

"""
ADVANCED INTEGRATION:

With pathlib (Modern Python):
"""

from pathlib import Path
import glob

# Using pathlib for path construction
data_dir = Path("data")
pattern = str(data_dir / "*.csv")
files = glob.glob(pattern)

# Or use pathlib's own glob
files = list(data_dir.glob("*.csv"))
print()
"""
With os.path for Robust Operations:
"""

import os
import glob

def find_files_safely(directory, pattern):
    """Safely find files with error handling"""
    if not os.path.exists(directory):
        print(f"Directory {directory} doesn't exist")
        return []
    
    search_pattern = os.path.join(directory, pattern)
    try:
        return glob.glob(search_pattern)
    except Exception as e:
        print(f"Error searching for {search_pattern}: {e}")
        return []

"""
PRACTICE PROJECTS:

1. File Organizer Script:
   - Sort files by extension into folders
   - Handle duplicates safely

2. Batch File Renamer:
   - Rename multiple files with patterns
   - Add timestamps or sequential numbers

3. Project Backup Utility:
   - Backup specific file types
   - Exclude temporary files

4. Log File Analyzer:
   - Process log files by date patterns
   - Generate reports from multiple logs

QUICK REFERENCE TABLE:

Pattern         | Matches                    | Example
*.txt          | All .txt files             | data.txt, info.txt
file?          | file + 1 character         | file1, fileA
file[0-9]      | file + single digit        | file1, file5
file[a-z]      | file + lowercase letter    | filea, filez
**/*.py        | All .py files recursively  | src/main.py, tests/test.py
data*          | Files starting with 'data' | data.txt, database.db

MEMORY AID:

"GRIP" - Glob Revision Important Points:
- G: Get current directory with os.getcwd()
- R: Recursive needs recursive=True
- I: Iterator (iglob) for large directories
- P: Portable paths with os.path.join()

Remember: Glob finds existing files only - create test files first for practice!

CONCEPT SUMMARY FOR REVISION:

Core Purpose: File pattern matching using shell-style wildcards
Key Strength: Simple, intuitive syntax for complex file operations
Learning Path: Start with basic wildcards (*,?) → Advanced patterns ([],**) → Iterator usage

Essential Patterns to Master:
1. *.ext - All files with extension
2. prefix* - All files starting with prefix  
3. **/*.ext - Recursive search in subdirectories
4. file[0-9].ext - Character class matching

Common Gotchas:
- Remember recursive=True for ** patterns
- Glob doesn't match hidden files by default
- Path separators vary by OS (use os.path.join for portability)
- Large directories: prefer iglob() over glob() for memory efficiency

Next Steps for Advanced Usage:
- Combine with os.path for robust file operations
- Use with pathlib for modern Python file handling
- Integrate with regular expressions for complex patterns
- Learn fnmatch module for more pattern matching options
"""
