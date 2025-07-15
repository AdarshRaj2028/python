# ============================================
# PYTHON EXCEPTION HANDLING - COMPLETE GUIDE
# ============================================

'''
WHAT ARE EXCEPTIONS?
- Exceptions are runtime errors that occur during program execution
- They interrupt the normal flow of the program
- Python has built-in exceptions and allows custom exceptions

TYPES OF ERRORS:
1. Syntax Errors (Parsing Errors): 
   - Caused by not following proper language structure
   - Examples: Missing colons (:), improper indentation, typos
   - Detected before program execution

2. Runtime Exceptions:
   - Occur during program execution
   - Can be handled using try-except blocks
   - Program crashes if not handled properly

EXCEPTION PROPAGATION:
- When an exception occurs, it stops the current process
- Exception passes to the calling process until handled
- If never handled, the program terminates with error message
'''

# ============================================
# COMMON BUILT-IN EXCEPTIONS
# ============================================

# AssertionError - assert statement evaluates to False
# assert 5 > 10  # Raises AssertionError

# AttributeError - Invalid attribute reference or assignment
# "hello".append("world")  # Strings don't have append method

# EOFError - input() reaches end-of-file unexpectedly
# Occurs when Ctrl+D (Unix) or Ctrl+Z (Windows) pressed during input()

# FloatingPointError - Floating point operation fails
# Usually from mathematical overflow or underflow

# ImportError/ModuleNotFoundError - Module cannot be imported
# import non_existent_module

# IndexError - Sequence index out of range
# my_list = [1, 2, 3]; my_list[10]  # Index doesn't exist

# KeyError - Dictionary key not found
# my_dict = {'a': 1}; my_dict['b']  # Key 'b' doesn't exist

# NameError - Variable name not found in scope
# print(undefined_variable)  # Variable not defined

# TypeError - Operation on inappropriate type
# "hello" + 5  # Cannot add string and integer

# ValueError - Correct type but inappropriate value
# int("hello")  # Cannot convert string to integer

# ZeroDivisionError - Division or modulo by zero
# 10 / 0  # Cannot divide by zero

# ============================================
# BASIC EXCEPTION HANDLING STRUCTURE
# ============================================

# SIMPLE TRY-EXCEPT (Catches any exception)
try:
    # Code that might raise an exception
    a = "hi"  # This will cause ValueError in next line
    b = int(a)  # Trying to convert non-numeric string to int
    print(type(b))
except:
    # Generic exception handler - catches ALL exceptions
    print("Exception Caught!")
    # NOTE: Using bare 'except:' is not recommended in production
    # It can hide unexpected errors and make debugging difficult

# ============================================
# SPECIFIC EXCEPTION HANDLING (RECOMMENDED)
# ============================================

try:
    # Multiple potential error sources
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    # Custom condition that raises exception
    if a < 0:
        raise TypeError("Negative numbers not allowed")
    
    c = a / b  # Potential ZeroDivisionError
    print(f"Result: {c}")

# Handle specific exceptions in order (most specific first)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
    
except ValueError:
    print("Error: Please enter valid numeric values")
    
except TypeError as e:
    print(f"Error: {e}")
    
except NameError:
    print("Error: Variable not defined")

print()
# IMPORTANT: Exception handling order matters!
# More specific exceptions should come before general ones

# ============================================
# MANUALLY RAISING EXCEPTIONS
# ============================================

# You can manually raise exceptions using 'raise' keyword
try:
    raise TypeError("This is a manually raised exception")
except TypeError as e:
# - "as e" creates a variable 'e' that holds the exception object
# - 'e' is just a variable name (you can use any name like 'error', 'err', etc.)
# - This lets you access the actual error message instead of just knowing an error happened
    print(f"Caught exception: {e}")
    print()

# With "as e" - you can see the specific error details which is not possible without variable(e)
try:
    number = int("hello")
except ValueError as e:
    print(f"Specific error: {e}")  # Shows: invalid literal for int() with base 10: 'hello'

print()

# Common use case: Input validation
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

# ============================================
# TRY-EXCEPT-ELSE-FINALLY STRUCTURE
# ============================================

try:
    print("Executing try block")
    # If no exception occurs, else block runs
    result = 10 / 2
    
except ZeroDivisionError:
    print("Division by zero occurred")
    
else:
    # Runs ONLY if no exception occurred in try block
    print(f"Success! Result is {result}")
    
finally:
    # ALWAYS runs, regardless of exceptions
    print("Cleanup operations (always executed)")
    # Use for: closing files, database connections, cleanup
print()
# ============================================
# USER-DEFINED CUSTOM EXCEPTIONS
# ============================================

# Create custom exception by inheriting from Exception class
class VoterEligibilityError(Exception):
    """Custom exception for voter eligibility validation"""
    
    def __init__(self, age, message="Age must be 18 or above to vote"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"VoterEligibilityError: {self.message} (Age provided: {self.age})"

# Using custom exception
try:
    age = 16
    print(f"Checking eligibility for age: {age}")
    
    if age < 18:
        raise VoterEligibilityError(age)
        
except VoterEligibilityError as e:
    print(f"Eligibility Error: {e}")
    
except TypeError:
    print("Error: Age must be a number")
    
else:
    print("Eligible to vote!")
    
finally:
    print("Eligibility check completed")
print()
# ============================================
# BEST PRACTICES FOR EXCEPTION HANDLING
# ============================================

'''
1. BE SPECIFIC: Catch specific exceptions rather than using bare except:
   ✓ except ValueError:
   ✗ except:

2. USE MULTIPLE EXCEPT BLOCKS: Handle different exceptions differently
   
3. ORDER MATTERS: More specific exceptions first, general ones last
   
4. USE FINALLY FOR CLEANUP: File closing, resource cleanup
   
5. DON'T IGNORE EXCEPTIONS: Always handle or log them appropriately
   
6. CUSTOM EXCEPTIONS: Create meaningful custom exceptions for your application
   
7. EXCEPTION CHAINING: Use 'raise ... from ...' to preserve original exception
   
8. LOG EXCEPTIONS: Use logging module for production applications

COMMON PATTERNS:
- Input validation with ValueError/TypeError
- File operations with FileNotFoundError/PermissionError  
- Network operations with ConnectionError/TimeoutError
- Database operations with custom database exceptions

REMEMBER:
- Exceptions are for exceptional circumstances, not normal program flow
- Handle exceptions at the appropriate level in your application
- Provide meaningful error messages to users
- Use exceptions to make your code more robust and user-friendly
'''

# ============================================
# EXCEPTION HIERARCHY (IMPORTANT TO KNOW)
# ============================================

'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- FileNotFoundError
      |    +-- PermissionError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning

Understanding this hierarchy helps in catching exceptions at the right level!
'''
