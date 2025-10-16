import math as m # Importing module as well as renaming it.
# or
# from math import pi # Usage of from
# or
# from math import * # Import all names from the standard module math

print("The value of pi ->", m.pi)

'''
-> If there are a large number of files to handle in your Python program,
   we can arrange our code within different directories to make things more manageable and reachable.
-> A directory or folder is a collection of or set of files and sub directories.
-> Python has the os module, which provides us with many useful methods to work with directories (and files as well).
-> Directory management in Python means creating a directory, renaming'it, listing all directories and working with them.
'''
import os

print("Working directory -> ", os.getcwd()) # Returns the present working directory 
print("Working directory -> ", os.getcwdb()) # Returns the present working directory as a byte object
# os.getcwdb() returns a byte object (bytes), which is a machine-level representation of data. 
# The b at the end of the function name stands for bytes.
# print("\n",os.listdir())
# All files and sub directories inside a directory can be known using the listdir() method.

# os.chdir('C:\\Users\\corridor\\Desktop\\Python Programming'), Used to change directory.

# os.mkdir('Example') # Used to make a new directory

# os.rename("Example 1", "Example") # used to rename a directory

# os.remove(file name) # Removing a file 
# os.rmdir(file name) # Removing a directory

r"""
=== LOCAL MODULES CONCEPT REFERENCE ===

WHAT IS A LOCAL MODULE?
- A Python file (.py) you create containing functions/variables
- Imported and used in other files within your project
- Like creating your own custom library

WHY USE MODULES?
✅ Code Reusability: Write once, use everywhere
✅ Organization: Keep related functions together  
✅ Maintainability: Change in one place, affects all
✅ Team Collaboration: Work on separate files

WHEN TO USE:
✅ Functions needed in multiple files
✅ Large projects (1000+ lines)
✅ Working with teams
❌ Small single-file projects
❌ Functions used only once

=== BASIC EXAMPLE ===

# File: utils.py (Your module)
def validate_email(email):
    return '@' in email and '.' in email

def clean_text(text):
    return text.strip().title()

def save_to_file(data, filename):
    with open(filename, 'a') as f:
        f.write(data + "\n")

# File: main.py (Uses your module)
import utils

email = "user@example.com"
if utils.validate_email(email):
    clean_name = utils.clean_text("john doe")
    utils.save_to_file(clean_name, "users.txt")

=== IMPORT METHODS ===
import utils                    # utils.function_name()
from utils import validate_email # validate_email() directly
import utils as u               # u.function_name()

=== PROJECT STRUCTURE ===
my_project/
├── main.py           # Main file
├── validation.py     # Validation functions
├── file_ops.py       # File operations
└── config.py         # Settings

BEST PRACTICES:
- Use descriptive names (user_utils.py not utils.py)
- Group related functions together
- Don't create modules too early
- Import only what you need

SIMPLE RULE: "If copying same function to multiple files, make it a module!"
"""
# Main File
# main.py - This uses your module

# Import your local module
import calculator_module_file

def main():
    print("=== LOCAL MODULE DEMO ===")
    print(calculator_module_file.get_info())
    print(f"Module version: {calculator_module_file.VERSION}")
    print("-" * 30)
    
    # Use functions from your module
    num1 = 10
    num2 = 5
    
    print(f"Numbers: {num1} and {num2}")
    print(f"Addition: {calculator_module_file.add(num1, num2)}")
    print(f"Subtraction: {calculator_module_file.subtract(num1, num2)}")
    print(f"Multiplication: {calculator_module_file.multiply(num1, num2)}")
    print(f"Division: {calculator_module_file.divide(num1, num2)}")
    print(f"PI value: {calculator_module_file.PI}")
    
    # Test error handling
    print(f"Divide by zero: {calculator_module_file.divide(10, 0)}")

if __name__ == "__main__":
    main()
