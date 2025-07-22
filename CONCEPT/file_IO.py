r"""
=============================================================================
PYTHON FILE HANDLING - COMPREHENSIVE GUIDE
=============================================================================

***Running this will create certain neccessary files in the current directory for better understanding***

WHAT IS FILE HANDLING?
----------------------
File handling refers to the process of accessing and manipulating files on a computer system.

WHAT ARE FILES?
--------------
Files are logical units of related information stored at named locations on disk.
They provide permanent storage in non-volatile memory (hard disk, SSD) unlike 
RAM which is volatile and loses data when power is off.

FILE OPERATION SEQUENCE:
-----------------------
1. Open a file
2. Read or Write (perform operation)  
3. Close the file

FILE TYPES:
----------
1. Text Files: .txt, .docs, .log, .py, .html etc.
2. Binary Files: .mp4, .mov, .png, .jpeg, .exe etc.

=============================================================================
FILE MODES AND OPERATIONS
=============================================================================

FILE MODES TABLE:
----------------
┌─────────┬───────────────────────────────────────────────────────┐
│ Mode    │ Description                                           │
├─────────┼───────────────────────────────────────────────────────┤
│ 'r'     │ Open for reading (default)                            │
│ 'w'     │ Open for writing, truncating the file first(Overwrite)│
│ 'x'     │ Create a new file and open it for writing             │
│ 'a'     │ Open for writing, appending to the end if file exists │
│ 'b'     │ Binary mode                                           │
│ 't'     │ Text mode (default)                                   │
│ '+'     │ Open a file for updating (reading and writing)        │
└─────────┴───────────────────────────────────────────────────────┘
Demonstrates all critical file handling concepts that are often overlooked

1. Explicit encoding for cross-platform compatibility
with open('config.txt', 'w', encoding='utf-8') as f:
    f.write("Configuration data\n")
    f.flush()  # 2. Force immediate write to disk

3. 'r+' requires existing file, pointer starts at beginning
with open('config.txt', 'r+', encoding='utf-8') as f:
    existing = f.read()  # Read existing content first
    f.seek(0, 2)  # Move to end for appending (alternative to 'a+')
    f.write("Additional config\n")
    f.seek(0)  # 4. Reset pointer to read updated content
    updated_content = f.read()

f.seek(offset, whence) PARAMETERS:

whence parameter values:
0 - SEEK_SET: Absolute positioning from beginning of file (default)
1 - SEEK_CUR: Relative to current position  
2 - SEEK_END: Relative to end of file

Common use cases:
f.seek(0, 2)    # Go to end for appending (like 'a' mode behavior)
f.seek(0, 0)    # Reset to beginning for reading from start
f.seek(-1, 2)   # Go to last byte of file

5. Memory-efficient reading for large files
with open('large_log.txt', 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        if line_num > 1000:  # Process in chunks
            break
        process_log_line(line.strip())

6. Binary mode for non-text files (no encoding conversion)
with open('image.jpg', 'rb') as f:
    header = f.read(10)  # Read first 10 bytes exactly

7. 'a+' mode for appending and reading

'w+' vs 'a+' Mode Differences

'w+' mode:

-> Opens file for writing and reading
-> Truncates the file to zero length (deletes existing content)
-> File pointer starts at the beginning of the now-empty file
-> You can read immediately, but there's nothing to read since the file was truncated

'a+' mode:

-> Opens file for appending and reading
-> Preserves existing content
-> File pointer starts at the end of the file
-> Requires seek(0) to read existing content

Both modes require understanding file pointer positioning, 
but 'w+' is often more confusing because developers expect to read existing content that has already been erased.

When you open a file in 'a+' mode, the file pointer is initially at the end of the file. 
This means that when you try to read from the file using file.read(), it will not return any contents because the file pointer is already at the end of the file.
To read the contents of the file in 'a+' mode, you need to seek to the beginning of the file using file.seek(0) before reading. 
This will move the file pointer to the beginning of the file, allowing you to read the contents.

OPENING FILES:
-------------
f1 = open("employee.dat")        # Equivalent to 'r' or 'rt'
f2 = open("pic.jpg", 'r+b')      # Read and write in binary mode
f3 = open("score.txt", 'w')      # Write in text mode
f4 = open("data.txt", 'a')       # Append mode
f5 = open("file.txt", encoding='utf-8')  # Specify encoding

=============================================================================
READING FROM FILES
=============================================================================

READING METHODS:
---------------
"""

# Example: Reading entire file
def read_entire_file():
    """Read complete file content at once"""
    f = open("example.txt", "r", encoding='utf-8')
    data = f.read()  # Reads entire file content
    print(f"Entire file content:")  # print(f"Entire file content: \n{f.read()}") -> We can also write like this
    print(data)
    f.close()

# Example: Reading line by line
def read_line_by_line():
    """Read file one line at a time"""
    f = open("example.txt", "r", encoding='utf-8')
    
    # Method 1: Using readline()
    line1 = f.readline()  # Reads first line
    line2 = f.readline()  # Reads second line
    line3 = f.readline()  # Reads thrid line
    print("First line:", line1.strip())
    print("Second line:", line2.strip())
    print("Third line:", line3.strip())
    
    f.close()

# Example: Reading all lines into a list
def read_all_lines():
    """Read all lines into a list"""
    f = open("example.txt", "r", encoding='utf-8')
    lines = f.readlines()  # Returns list of all lines
    print("All lines as list:")
    for i, line in enumerate(lines):
        print(f"Line {i+1}: {line.strip()}")
    f.close()

# Example: Reading with loop
def read_with_loop():
    """Read file using for loop"""
    f = open("example.txt", "r", encoding='utf-8')
    print("Reading with loop:")
    for line_number, line in enumerate(f, 1):
        print(f"Line {line_number}: {line.strip()}")
    f.close()

# Example of Reading and writing multiple files at once

content = ["This should be one 1st file", "This should be one 2nd file", "This should be one 3rd file"]

filename = ["doc.txt", "Report.txt", "Presentation.txt"]
# METHOD 1
# with open(filename[0], 'w', encoding="utf-8") as f, \
#     open(filename[1], 'w', encoding="utf-8") as f2, \
#     open(filename[2], 'w', encoding="utf-8") as f3:
    
#     f.write(content[0])
#     f2.write(content[1])
#     f3.write(content[2])

# METHOD 2 (preferable)
for content, filename in zip(content, filename):
    with open(f"{filename}", 'w') as file:
        file.write(content)
"""
=============================================================================
WRITING TO FILES
=============================================================================

WRITING METHODS:
---------------
"""

# Example: Writing (overwrites existing content)
def write_to_file():
    """Write content to file (overwrites existing)"""
    f = open("output.txt", 'w', encoding='utf-8')
    f.write("This is the first line\n")
    f.write("This is the second line\n")
    f.write("This overwrites any existing content")
    f.close()
    print("Content written to output.txt")

# Example: Appending to file
def append_to_file():
    """Append content to existing file"""
    f = open("output.txt", 'a', encoding='utf-8')
    f.write("\nThis line is appended")
    f.write("\nAnother appended line")
    f.close()
    print("Content appended to output.txt")

# Example: Writing multiple lines
def write_multiple_lines():
    """Write multiple lines using writelines()"""
    lines = [
        "Line 1: Python File Handling\n",
        "Line 2: Reading and Writing\n", 
        "Line 3: File Operations\n"
    ]
    
    f = open("multiple_lines.txt", 'w', encoding='utf-8')
    f.writelines(lines)  # Write list of strings
    f.close()
    print("Multiple lines written to multiple_lines.txt")

"""
=============================================================================
PROPER FILE HANDLING WITH 'WITH' STATEMENT
=============================================================================

USING 'WITH' STATEMENT (RECOMMENDED):
------------------------------------
The 'with' statement automatically handles file closing, even if an error occurs.
This is the BEST PRACTICE for file handling.
"""

# Example: Reading with 'with' statement
def read_with_context_manager():
    """Read file using with statement (recommended)"""
    with open("example.txt", "r", encoding='utf-8') as f:
        content = f.read()
        print("Content read using 'with':")
        print(content)
    # File is automatically closed here, even if error occurs

# Example: Writing with 'with' statement  
def write_with_context_manager():
    """Write file using with statement (recommended)"""
    with open("safe_output.txt", "w", encoding='utf-8') as f:
        f.write("This is written safely\n")
        f.write("File will be closed automatically")
    print("File written and closed safely")

# Example: Processing large files efficiently
def process_large_file():
    """Process large file line by line efficiently"""
    with open("example.txt", "r", encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Process each line without loading entire file into memory
            processed_line = line.strip().upper()
            print(f"Line {line_num}: {processed_line}")

"""
=============================================================================
ERROR HANDLING IN FILE OPERATIONS
=============================================================================

HANDLING FILE ERRORS:
--------------------
"""

def safe_file_operations():
    """Demonstrate error handling in file operations"""
    
    # Handle file not found error
    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: File not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Handle writing errors
    try:
        with open("readonly.txt", "w") as f: # Here, if we made this file read only
# Then it protects the file from being changed or deleted by mistake.
# Python (and other programs) will not be able to write to it unless you remove the read-only attribute.
            f.write("Trying to write")
    except PermissionError:
        print("Error: Cannot write to read-only file!")

"""
=============================================================================
PRACTICAL EXAMPLES
=============================================================================

REAL-WORLD FILE OPERATIONS:
--------------------------
"""

def create_student_records():
    """Create and manage student records file"""
    students = [
        "John Doe, 85, Math\n",
        "Jane Smith, 92, Science\n", 
        "Bob Johnson, 78, English\n"
    ]
    
    # Write student records
    with open("students.txt", "w", encoding='utf-8') as f:
        f.writelines(students)
    print("Student records created")

def read_and_process_records():
    """Read and process student records"""
    try:
        with open("students.txt", "r", encoding='utf-8') as f:
            print("Student Records:")
            print("-" * 30)
            for line in f:
                name, score, subject = line.strip().split(", ")
# .split(", ") is necessary to break the line into a list of three parts.
# Without .split(", "), you cannot unpack the line into name, score, subject—you will get an error.
                print(f"Name: {name}")
                print(f"Score: {score}")
                print(f"Subject: {subject}")
                print("-" * 30)
    except FileNotFoundError:
        print("Student records file not found!")

def log_operations():
    """Example of logging operations to a file"""
    import datetime
    
    with open("operations.log", "a", encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Operation performed\n")
    print("Operation logged")

def copy_file_content():
    """Copy content from one file to another"""
    try:
        with open("source.txt", "r", encoding='utf-8') as source: # We need to create a file named source.txt for making this work
            with open("destination.txt", "w", encoding='utf-8') as dest:
                dest.write(source.read())
        print("File copied successfully")
    except FileNotFoundError as e:
        print(f"Source file not found!\nError: {e}")

"""
=============================================================================
BEST PRACTICES
=============================================================================

FILE HANDLING BEST PRACTICES:
-----------------------------
1. Always use 'with' statement for automatic file closing
2. Specify encoding explicitly (usually 'utf-8')
3. Handle exceptions (FileNotFoundError, PermissionError)
4. Use appropriate file modes ('r', 'w', 'a', 'x')
5. Don't rely on garbage collector to close files
6. Use readline() for large files to save memory
7. Close files properly if not using 'with' statement

COMMON MISTAKES TO AVOID:
------------------------
- Forgetting to close files
- Not handling file exceptions
- Using wrong file modes
- Not specifying encoding
- Loading entire large files into memory
- Not using 'with' statement

MEMORY EFFICIENT READING:
------------------------
# For large files, read line by line:
with open("large_file.txt", "r") as f:
    for line in f:  # Memory efficient
        print(f"{line}", end="")  # end="" prevents double newlines

# Instead of:
with open("large_file.txt", "r") as f:
    all_content = f.read()  # Loads entire file into memory

=============================================================================
QUICK REFERENCE
=============================================================================

COMMON OPERATIONS:
-----------------
# Reading
with open("file.txt", "r") as f:
    content = f.read()          # Read entire file
    line = f.readline()         # Read one line
    lines = f.readlines()       # Read all lines to list

# Writing  
with open("file.txt", "w") as f:
    f.write("text")             # Write string
    f.writelines(list_of_lines) # Write list of strings

# Appending
with open("file.txt", "a") as f:
    f.write("appended text")    # Add to end of file

# File existence check
import os
if os.path.exists("file.txt"):
    print("File exists")

=============================================================================
COMMON FILE ERRORS IN PYTHON
=============================================================================

| Error                | When It Happens                                               |
|----------------------|------------------------------------------------------------- |
| FileNotFoundError    | Trying to open a file for reading that does not exist ("r")  |
| PermissionError      | Trying to write to a read-only file, or lacking permissions  |
| IsADirectoryError    | Trying to open a directory as if it were a file              |
| IOError / OSError    | General input/output errors (disk full, hardware issues, etc.) |

=============================================================================
"""

# Example usage and testing
if __name__ == "__main__":
    print("=== FILE HANDLING EXAMPLES ===")
    
    # Create a sample file for testing
    with open("example.txt", "w", encoding='utf-8') as f:
        f.write("Line 1: Hello World\n")
        f.write("Line 2: Python File Handling\n") 
        f.write("Line 3: Learning Programming\n")
    
    print("Sample file created: example.txt")
    
    # Demonstrate different reading methods
    print("\n1. Reading entire file:")
    read_entire_file()
    
    print("\n2. Reading line by line:")
    read_line_by_line()
    
    print("\n3. Reading all lines:")
    read_all_lines()
    
    print("\n4. Reading with loop:")
    read_with_loop()
    
    # Demonstrate writing methods
    print("\n5. Writing to file:")
    write_to_file()
    
    print("\n6. Appending to file:")
    append_to_file()
    
    print("\n7. Writing multiple lines:")
    write_multiple_lines()
    
    # Demonstrate best practices
    print("\n8. Using 'with' statement:")
    read_with_context_manager()
    write_with_context_manager()
    
    print("\n9. Processing large file:")
    process_large_file()
    
    # Demonstrate practical examples
    print("\n10. Student records example:")
    create_student_records()
    read_and_process_records()
    
    print("\n11. Logging example:")
    log_operations()
    
    print("\n12. Error handling:")
    safe_file_operations()

    print("\n13. Copy file:")
    copy_file_content()
