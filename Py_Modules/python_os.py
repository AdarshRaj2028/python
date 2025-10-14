r"""
======================================================================
📘 PYTHON OS MODULE: CONCEPTS, USAGE & BEST PRACTICES
======================================================================

--------------------------------------------------------------------------------
🔎 OVERVIEW
--------------------------------------------------------------------------------
* The `os` module provides a way to interact with the operating system using Python.
* Common tasks: file/folder management, environment variables, path manipulation, process management.

--------------------------------------------------------------------------------
📚 ESSENTIAL FUNCTIONS IN THE OS MODULE
--------------------------------------------------------------------------------

--- WORKING DIRECTORY MANAGEMENT ---
- os.getcwd()
    Get the current working directory (returns a string).
- os.chdir(path)
    Change the current working directory to the specified path.
- os.listdir(path='.')
    Returns list of files & directories in the specified path.

--- FILE AND DIRECTORY MANAGEMENT ---
- os.mkdir(path)
    Create a new directory (single level).
- os.makedirs(path)
    Create new directory/directories (can create nested folders at once).
- os.rmdir(path)
    Remove (delete) a directory (must be empty).
- os.removedirs(path)
    Remove nested directories (if each is empty).
- os.remove(path)
    Remove (delete) a file.

- os.rename(src, dst)
    Rename a file or directory from src to dst.
- os.replace(src, dst)
    Same as rename, but will overwrite dst if exists.

- os.scandir(path='.')
    Returns an iterator of os.DirEntry objects, more efficient than os.listdir for large directories. 
    Each DirEntry has attributes like .name, .path, .is_file(), .is_dir().

--- PATH OPERATIONS (os.path submodule) ---
- os.path.join(path1, path2, ...)
    Join one or more path components using separator for current OS.
- os.path.exists(path)
    Test if path exists (file or directory, returns True/False).
- os.path.isfile(path)
    Checks if a path is a regular file.
- os.path.isdir(path)
    Checks if a path is a directory.
- os.path.getsize(path)
    Return size of path in bytes.
- os.path.abspath(path)
    Get absolute path from a given relative path.
- os.path.basename(path)
    Get the last component of the path.
- os.path.dirname(path)
    Get the directory name from the path.
- os.path.splitext(path)
    Split pathname into (root, extension).

--- ENVIRONMENT VARIABLES ---
- os.environ
    A mapping object to access/set environment variables.
    Use os.environ['VARNAME'] or os.environ.get('VARNAME').

--- RUNNING SYSTEM COMMANDS ---
- os.system(command)
    Run the (string) command in a subshell. Returns exit status code (integer).
- os.popen(command)
    Opens a pipe to or from command. Returns a file-like object (useful to read command output).
- subprocess module
    Recommended for new code when interacting with system commands (better control than os.system).

--- WALKING DIRECTORIES ---
- os.walk(top)
    Generator yielding directory tree (root, dirs, files).

--- MISCELLANEOUS ---
- os.stat(path)
    Get metadata/statistics about a file/path (size, time, permissions).
- os.sep
    The path separator for current OS ('/' on Unix, '\\' on Windows).
- os.name
    OS dependent name: 'posix', 'nt', etc.

--------------------------------------------------------------------------------
🏠 USER DATA / APP CONFIG FOLDERS (e.g., for Desktop Applications)
--------------------------------------------------------------------------------
- When developing apps (especially ones converted to .exe with PyInstaller or similar),
  avoid saving user data in the working directory. It may be read-only, inside the executable bundle,
  or different than you expect after installation/deployment.

- Instead, use the user's HOME directory (cross-platform) to store app state and user files.

- os.path.expanduser("~")
    Gets the path to the current user's home directory (e.g., 'C:\\Users\\YourName' on Windows, '/home/yourname' on Linux).
- os.makedirs(path, exist_ok=True)
    Ensures subdirectories exist (creates directory and parents as needed; doesn't error if already present).

- Combine to create a per-user, hidden subfolder for your app (e.g., ~/.your_app or C:\Users\You\.your_app).

- This approach *guarantees* that your data files will be accessible and persistent
  regardless of where the EXE is running from, and is best practice for config/data files.

--------------------------------------------------------------------------------
⚠️ TIPS & GOTCHAS
--------------------------------------------------------------------------------

- Paths are different on Windows vs Linux/macOS; prefer os.path functions for compatibility.
- Use os.path.expanduser("~") or os.environ (APPDATA on Windows) for user-scoped files/folders.
- For production/packaged/distributed apps, NEVER write beside the EXE!
- See also 'appdirs' third-party module for professional cross-platform app folder management.
- Use os.makedirs for deep folder creation—os.mkdir will only create one level!
- For deleting files safely, always check with os.path.exists and os.path.isfile.
- On modern Python (3.4+), consider pathlib for an object-oriented, more pythonic approach to file paths.
- Not all functions are available on all platforms (Windows/Linux). Always check docs if writing cross-platform code.
- For reading large directory listings, prefer os.scandir() over os.listdir() for performance.

===============================================================================
"""

# =============== RUNNABLE USAGE EXAMPLES BELOW =================

import os

# 1. Storing per-user app files: Example (TO-DO APPLICATION)
#    This ensures the data persists for each user and is NOT lost or inaccessible when distributed as an EXE.

APPDATA_DIR = os.path.join(os.path.expanduser("~"), ".todo_app")  # Hidden on Unix, visible folder on Windows. APPDATA on Windows, and it's a constant.
os.makedirs(APPDATA_DIR, exist_ok=True)   # Make sure it and parent folders exist (does nothing if exists)

# Expanduser will create the file in C:\Users\username\.todo_app which will contain the file, and contents written below

FILEPATH_TODO = os.path.join(APPDATA_DIR, "todo_list.txt")
FILEPATH_COMPLETED_TODO = os.path.join(APPDATA_DIR, "completed_todo_list.txt")

# Demo: write and read a todo item
with open(FILEPATH_TODO, 'w') as f:
    f.write("Sample TODO item!\n")
print("Wrote TODO to:", FILEPATH_TODO)

with open(FILEPATH_TODO, 'r') as f:
    print("Contents of TODO file:", f.read())

print()

# 2. Usual directory/file examples...
cwd = os.getcwd()
print("Current working directory:", cwd)

print("List of files and folders in CWD:", os.listdir('.'))

# 3. Get and print current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# 4. List the contents of the current directory
print("List of files and folders in CWD:", os.listdir('.'))

# 5. Create and remove a new directory (safe demo)
test_dir = "my_test_folder"
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"Directory '{test_dir}' created.")

if os.path.exists(test_dir):
    os.rmdir(test_dir)
    print(f"Directory '{test_dir}' removed.")

# 6. Using os.makedirs() and os.removedirs() for nested folders
nested_dir = "parent_folder/child_folder/grandchild"
if not os.path.exists(nested_dir):
    os.makedirs(nested_dir)
    print(f"Nested directories '{nested_dir}' created.")

if os.path.exists(nested_dir):
    os.removedirs(nested_dir)
    print(f"Nested directories '{nested_dir}' removed.")

# 7. Path joining and properties
file_name = "example.txt"
full_path = os.path.join(cwd, file_name)
print("Joined path:", full_path)
print("Is this an existing file?", os.path.isfile(full_path))
print("Is this an existing directory?", os.path.isdir(cwd))
print("Absolute path:", os.path.abspath(file_name))
print("Basename:", os.path.basename(full_path))
print("Dirname:", os.path.dirname(full_path))
print("Splitext:", os.path.splitext(file_name))

# 8. Rename and remove a file (create a temp file first)
with open("temp_test.txt", "w") as f:
    f.write("sample data")
if os.path.exists("temp_test.txt"):
    os.rename("temp_test.txt", "temp_test_renamed.txt")
    print("File renamed to 'temp_test_renamed.txt'")
    os.remove("temp_test_renamed.txt")
    print("Temp test file removed.")

# 9. Environment variables
home = os.environ.get('HOME') or os.environ.get('USERPROFILE')
print("Home directory from environment:", home)

# 10. Run a simple system command (cross-platform, show Python version)
cmd = "python --version" if os.name != 'nt' else "py --version"
exit_code = os.system(cmd)
print("System (python --version) exit code:", exit_code)

# 11. Walk through the directory tree (show top-level, up to 1st folder only)
print("Walking current directory tree:")
for root, dirs, files in os.walk('.'):
    print("Root:", root)
    print("Dirs:", dirs)
    print("Files:", files)
    break   # Just one level for demo

# 12. Get metadata of this script file (size, etc.)
this_file = __file__ if '__file__' in globals() else 'os_module_concept.py'
if os.path.exists(this_file):
    stat = os.stat(this_file)
    print("File size:", stat.st_size, "bytes")
    print("Last modified:", stat.st_mtime)

# 13. Print path separator and OS name
print("Path separator for this OS:", os.sep)
print("OS name:", os.name)

# 14. Using os.scandir() to efficiently iterate files/directories in current directory
print("Listing with os.scandir():")
with os.scandir('.') as entries:
    for entry in entries:
        entry_type = "Directory" if entry.is_dir() else "File"
        print(f"  [{entry_type}] {entry.name}")

# =========== End of OS module concept file ===========

