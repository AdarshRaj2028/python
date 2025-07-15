# ============================================================================
# PYTHON FUNCTIONS - COMPREHENSIVE GUIDE FOR REVISION
# ============================================================================

"""
WHAT ARE FUNCTIONS?
- Block of code that performs a specific task and reduces redundancy
- Function implementation breaks programming into smaller and modular chunks
- Functions help make programs more modular, organized, reusable and easy to debug

FUNCTION SYNTAX:
def func_name(param1, param2...):
    '''docstring'''
    statement(s)
    return return_value  # Optional, depends on the type of work function does
Function can return multiple value, python will return them as tuple, then we can unpack them
To unpack the returned values, you just assign them to multiple variables at once

TYPES OF FUNCTIONS:
1. Built-in functions (print, len, input, etc.)
2. User-defined functions (created by programmer)

-> Defining a main function in Python is a way to organize the code that should run when your script is executed directly (not imported).
Simple steps:

Write your main logic inside a function called main():

def main():
    # your main code here

At the bottom of your file, add:

if __name__ == "__main__":
    main()

name is a special variable.
main is the value of name when the file is run directly.
if name == "main": is used to control what code runs in each case.

Why use it?

It lets you write code that can be used both as a reusable module and as a standalone script.
Code inside this block won't run when the file is imported elsewhere—only when run directly.

What this does:

When you run the file directly, main() runs.
When you import the file in another script, main() does NOT run automatically.

"""

# ============================================================================
# BASIC FUNCTION EXAMPLES
# ============================================================================

print("="*60)
print("BASIC FUNCTION EXAMPLES")
print("="*60)

# FUNCTION WITHOUT RETURN STATEMENT
def hello1():
    """Function that prints but doesn't return anything"""
    print("Hello World")

# FUNCTION WITH RETURN STATEMENT  
def hello2():
    """Function that returns a value back to caller"""
    return "Hello World"

"""
RETURN STATEMENT:
- Returns control back to the caller
- Used to return a value to the caller of the function
- Functions without return implicitly return None
"""

# Testing both function types
hello1()                    # Prints directly
print(hello2(), end="\n\n") # Returns value, then print() displays it

# ============================================================================
# FUNCTION WITH PARAMETERS AND DOCSTRING
# ============================================================================

def sum1(a, j):
    """
    This is a docstring which describes the purpose and functionality of the function.
    This function adds two numbers and prints the result.
    
    Parameters:
    a: First number
    j: Second number
    """
    print(a + j)

# Function call with arguments
sum1(5, 7)

# Accessing function documentation
print("Function documentation:", sum1.__doc__)
print()

# ============================================================================
# RECURSION - FUNCTION CALLING ITSELF
# ============================================================================

print("="*60)
print("RECURSION EXAMPLES")
print("="*60)

"""
RECURSION:
- When a function calls itself multiple times
- Must have a termination condition (base case) to prevent infinite loop
- Useful for problems that can be broken down into smaller similar problems
"""

# BASIC RECURSION EXAMPLE - COUNTDOWN
def show(n):
    """
    Recursive function to print numbers from n down to 1
    Base case: when n == 0, stop recursion
    """
    if n == 0:  # BASE CASE - termination condition
        return
    print(n)
    show(n - 1)  # RECURSIVE CALL with smaller value

try:
    user = int(input("Enter the number for countdown: "))
    show(user)
    print()
except ValueError as e:
    print(f"Please enter a valid integer: {e}")

# ADVANCED RECURSION EXAMPLE - LIST TRAVERSAL
def print_list_recursive(list1, i=0):
    """
    Recursive function to print all elements of a list
    
    Parameters:
    list1: The list to traverse
    i: Current index (default 0)
    
    Base case: when i equals length of list
    """
    if i == len(list1):  # BASE CASE
        return
    print(list1[i])
    print_list_recursive(list1, i + 1)  # RECURSIVE CALL with next index

# Test recursive list printing
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Recursive list printing:")
print_list_recursive(test_list)
print()

# ============================================================================
# FUNCTION ARGUMENT VARIATIONS
# ============================================================================

print("="*60)
print("FUNCTION ARGUMENT VARIATIONS")
print("="*60)

"""
ARGUMENT TYPES:
1. Default Arguments: Parameters with default values
2. Keyword Arguments: Arguments passed by parameter name
3. Arbitrary Arguments (*args): Variable number of positional arguments, For Multiple Positional Arguments
It allows a function to accept any number of positional arguments as a tuple.
4. Keyword Arbitrary Arguments (**kwargs): Variable number of keyword arguments, For Multiple Keyword Arguments
It allows a function to accept any number of keyword arguments as a dictionary.
"""

# DEFAULT ARGUMENTS
def hello(name, msg=", How are you doing?"):
    """
    Function with default parameter
    If msg is not provided, default value is used
    """
    print("Hello", name, msg)

# Testing default arguments
hello("Adarsh")                              # Uses default msg
hello("Adarsh", ", Have a nice day")         # Overrides default msg
print()

# ARBITRARY ARGUMENTS (*args)
def sumAll(*args):
    """
    Function with arbitrary arguments using *args
    
    *args explanation:
    - Collects all positional arguments into a tuple
    - Asterisk (*) is the unpacking operator
    - Allows variable number of arguments (0 to many)
    - Arguments are accessible as tuple inside function
    """
    total = 0
    for i in args:
        total += i
    return total

# Testing arbitrary arguments
print("Sum with 0 arguments:", sumAll())           # 0 arguments
print("Sum with 1 argument:", sumAll(5))           # 1 argument  
print("Sum with 3 arguments:", sumAll(1, 2, 3))    # 3 arguments
print("Sum with 5 arguments:", sumAll(1, 2, 3, 4, 5))  # 5 arguments
print()

# KEYWORD ARGUMENTS EXAMPLE
def greet_person(first_name, last_name, age=None):
    """Function demonstrating keyword arguments"""
    if age:
        print(f"Hello {first_name} {last_name}, you are {age} years old")
    else:
        print(f"Hello {first_name} {last_name}")

# Different ways to call with keyword arguments
greet_person("John", "Doe")                    # Positional arguments
greet_person(last_name="Smith", first_name="Jane")  # Keyword arguments
greet_person("Bob", last_name="Johnson", age=25)    # Mixed arguments
print()

# ============================================================================
# LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ============================================================================

print("="*60)
print("LAMBDA FUNCTIONS")
print("="*60)

"""
LAMBDA FUNCTIONS:
- Anonymous functions defined without a name
- Defined using 'lambda' keyword
- Syntax: lambda arguments: expression
- Used for simple, one-line functions
- Often used with filter(), map(), reduce() functions
"""

# BASIC LAMBDA EXAMPLE
double = lambda x: x * 2
print("Double of 10 is:", double(10))

# LAMBDA WITH MULTIPLE ARGUMENTS
add = lambda x, y: x + y
print("Sum of 5 and 3:", add(5, 3))

# LAMBDA WITH CONDITIONAL
max_of_two = lambda a, b: a if a > b else b
print("Maximum of 10 and 15:", max_of_two(10, 15))
print()

# ============================================================================
# LAMBDA WITH BUILT-IN FUNCTIONS
# ============================================================================

print("="*60)
print("LAMBDA WITH BUILT-IN FUNCTIONS")
print("="*60)

# FILTER() WITH LAMBDA - Extract even numbers
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# filter() creates new list with items where lambda returns True
even_numbers = list(filter(lambda x: (x % 2 == 0), my_list))
print("Original list:", my_list)
print("Even numbers:", even_numbers)

# Alternative filters
greater_than_5 = list(filter(lambda x: x > 5, my_list))
print("Numbers greater than 5:", greater_than_5)
print()

# MAP() WITH LAMBDA - Transform each element
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# map() applies lambda function to each item in the list
doubled_list = list(map(lambda x: x * 2, my_list))
print("Original list:", my_list)
print("Doubled list:", doubled_list)

# More map examples
squared_list = list(map(lambda x: x ** 2, my_list))
print("Squared list:", squared_list)

# Convert to strings
string_list = list(map(lambda x: f"Number: {x}", my_list))
print("String list:", string_list[:3], "...")  # Show first 3 elements
print()

# ============================================================================
# DECOUPLING OF THE FUNCTION
# ============================================================================
"""
=== DECOUPLING CONCEPT SUMMARY ===

WHAT IS DECOUPLING?
- Breaking down big functions into small, focused functions
- Each function does ONE specific job
- Reduces code redundancy by creating reusable functions

WHY DECOUPLE?
1. DRY Principle: Don't Repeat Yourself - write once, use everywhere
2. Easy Maintenance: Change logic in one place, affects everywhere
3. Easy Testing: Test each small function separately
4. Easy Reuse: Use same function in multiple places
5. Less Bugs: Fix once, fixed everywhere

SIMPLE RULE:
"One function = One job"

EXAMPLE:
-> BAD (Coupled - everything mixed):
def process_user():
    # validation + processing + saving all mixed together
    if len(name) < 2: return False
    if '@' not in email: return False
    name = name.title()
    save_to_file(name, email)

-> GOOD (Decoupled - separate functions):
def validate_name(name): return len(name) >= 2
def validate_email(email): return '@' in email  
def format_name(name): return name.title()
def save_user(name, email): # save logic here

def process_user():
    if not validate_name(name): return False
    if not validate_email(email): return False
    formatted_name = format_name(name)
    save_user(formatted_name, email)

BENEFITS:
- validate_name() can be reused in other functions
- Change validation logic in one place
- Easy to test each function separately
- Less redundant code

REMEMBER: Decoupling = Small reusable functions = Less redundancy
"""

print("="*60)
print("DECOUPLING OF THE FUNCTION")
print("="*60)

# Get user input for feet and inches
feet_inches = input("Enter the feet and inches(e.g. 5 12): ")

# Define a function to parse the input string into a tuple of feet and inches
def parse(feetinches):
    """
    Parse the input string into a tuple of feet and inches.
  Args:
        feetinches (str): The input string containing feet and inches.
  Returns:
        tuple: A tuple containing the feet and inches as floats.
    """
    # Remove leading and trailing whitespace from the input string
    parts = feetinches.strip()
    # Split the input string into a list of parts using space as the delimiter
    parts = " ".join(parts.split())
    # Extract the feet and inches from the list of parts
    feet = float(parts.split()[0])
    inches = float(parts.split()[1])
    # Return a tuple containing the feet and inches
    return (feet, inches)

# Define a function to convert feet and inches to meters
def convert(feet, inches):
    """
    Convert feet and inches to meters.

    Args:
        feet (float): The number of feet.
        inches (float): The number of inches.

    Returns:
        float: The equivalent length in meters.
    """
    # Use the conversion factors to calculate the length in meters
    meters = feet * 0.3048 + inches * 0.0254
    # Return the result
    return meters

# Call the parse function to parse the user input into a tuple of feet and inches
feet_inches_tuple = parse(feet_inches)
print("Feet Inches tuple: ", feet_inches_tuple)

# Call the convert function to convert the feet and inches to meters
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])

# Check if the result is less than 1 meter
if result < 1:
    # If true, print a message indicating that the kid is too small to ride
    print("The kid is too small to ride")
else:
    # If false, print a message indicating that the kid can ride
    print("The kid can ride")

# ============================================================================
# ADVANCED FUNCTION CONCEPTS
# ============================================================================

print("="*60)
print("ADVANCED FUNCTION CONCEPTS")
print("="*60)

# FUNCTION WITH **kwargs (KEYWORD ARGUMENTS)
def print_info(**kwargs):
    """
    Function with arbitrary keyword arguments
    **kwargs collects keyword arguments into a dictionary
    """
    print("Information provided:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Testing **kwargs
print_info(name="Alice", age=30, city="New York", job="Engineer")
print()

# FUNCTION WITH MIXED ARGUMENTS
def complex_function(required_arg, *args, default_arg="default", **kwargs):
    """
    Function demonstrating all argument types:
    - required_arg: Required positional argument
    - *args: Variable positional arguments, For Multiple Positional Arguments
    - default_arg: Default argument
    - **kwargs: Variable keyword arguments
    """
    print(f"Required: {required_arg}")
    print(f"Args: {args}")
    print(f"Default: {default_arg}")
    print(f"Kwargs: {kwargs}")

# Testing mixed arguments
complex_function("must_provide", 1, 2, 3, default_arg="custom", extra="info", count=5)
print()

# ============================================================================
# PRACTICAL FUNCTION EXAMPLES
# ============================================================================

print("="*60)
print("PRACTICAL FUNCTION EXAMPLES")
print("="*60)

# CALCULATOR FUNCTIONS
def calculator(operation, *numbers):
    """Multi-purpose calculator function"""
    if not numbers:
        return 0
    
    if operation == "add":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    else:
        return "Unknown operation"

# Testing calculator
print("Addition:", calculator("add", 1, 2, 3, 4, 5))
print("Multiplication:", calculator("multiply", 2, 3, 4))
print("Maximum:", calculator("max", 10, 5, 8, 3))
print()

# LIST PROCESSING FUNCTIONS
def process_list(numbers, operation):
    """Process list based on operation using lambda"""
    operations = {
        "double": lambda x: x * 2,
        "square": lambda x: x ** 2,
        "even": lambda x: x % 2 == 0,
        "positive": lambda x: x > 0
    }
    
    if operation in ["double", "square"]:
        return list(map(operations[operation], numbers))
    elif operation in ["even", "positive"]:
        return list(filter(operations[operation], numbers))
    else:
        return "Unknown operation"

# Testing list processing
test_numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
print("Original:", test_numbers)
print("Doubled:", process_list(test_numbers, "double"))
print("Squared:", process_list(test_numbers, "square"))
print("Even only:", process_list(test_numbers, "even"))
print("Positive only:", process_list(test_numbers, "positive"))

# ============================================================================
# KEY REVISION POINTS
# ============================================================================

"""
FUNCTION REVISION CHECKLIST:

BASIC CONCEPTS:
 def keyword to define functions
 return statement (optional)
 Function calls and arguments
 Docstrings for documentation

ARGUMENT TYPES:
 Positional arguments: func(a, b)
 Default arguments: func(a, b=10)
 Keyword arguments: func(a=5, b=10)
 *args: Variable positional arguments (tuple)
 **kwargs: Variable keyword arguments (dictionary)

RECURSION:
 Function calling itself
 Must have base case (termination condition)
 Useful for repetitive problems

LAMBDA FUNCTIONS:
 Anonymous functions: lambda x: x*2
 Used with filter(), map(), reduce()
 Good for simple, one-line functions

BUILT-IN FUNCTIONS WITH LAMBDA:
 filter(): Selects items based on condition
 map(): Transforms each item in iterable
 reduce(): Reduces iterable to single value

BEST PRACTICES:
 Use descriptive function names
 Write clear docstrings
 Keep functions focused on single task
 Use appropriate argument types
 Handle edge cases and errors
"""
r"""
=== WHEN TO USE `-> None` AND WHEN NOT TO ===

WHAT IS `-> None`?
- Type hint indicating a function doesn't return a meaningful value
- Makes code self-documenting and professional
- Helps IDEs and type checkers understand your intent

=== WHEN TO USE `-> None` ✅ ===

1. ACTION FUNCTIONS (Functions that DO things):
   def save_file(data: str) -> None:
       with open("file.txt", "w") as f:
           f.write(data)
   
   def print_message(msg: str) -> None:
       print(msg)
   
   def clear_screen() -> None:
       os.system('cls' if os.name == 'nt' else 'clear')

2. SETUP/INITIALIZATION FUNCTIONS:
   def main() -> None:
       # Main program logic
   
   def initialize_app() -> None:
       # Setup code
   
   def configure_settings() -> None:
       # Configuration logic

3. EARLY EXIT FUNCTIONS:
   def validate_input(data: str) -> None:
       if not data:
           return None  # Early exit for invalid input
       process_data(data)

=== WHEN NOT TO USE `-> None` ❌ ===

1. WHEN RETURNING EMPTY COLLECTIONS:
   # ❌ BAD: Forces None checks
   def get_items() -> list | None:
       if no_items:
           return None
       return items
   
   # ✅ GOOD: Safe iteration
   def get_items() -> list:
       if no_items:
           return []  # Empty list, not None
       return items

2. FOR ERROR CONDITIONS:
   # ❌ BAD: Using None for errors
   def divide(a: float, b: float) -> float | None:
       if b == 0:
           return None  # Ambiguous!
       return a / b
   
   # ✅ GOOD: Use exceptions
   def divide(a: float, b: float) -> float:
       if b == 0:
           raise ValueError("Cannot divide by zero")
       return a / b

3. WHEN FUNCTION SHOULD RETURN DATA:
   # ❌ BAD: Function that should return something
   def calculate_total(items: list) -> None:
       total = sum(items)
       print(total)  # Should return, not print
   
   # ✅ GOOD: Return the calculated value
   def calculate_total(items: list) -> float:
       return sum(items)

=== SPECIAL CASE: OPTIONAL RETURNS ===

When None is a VALID result (not an error):
def find_user(user_id: int) -> User | None:
    if user_exists(user_id):
        return User(user_id)
    else:
        return None  # Valid "not found" result

def get_config(key: str) -> str | None:
    if key in config:
        return config[key]
    else:
        return None  # Valid "not configured" result

=== EXAMPLES FROM TODO APP CONTEXT ===

✅ CORRECT Usage in Todo Functions:
def add(user_input: str) -> None:          # Adds todo, no return needed
def show() -> None:                        # Displays todos, no return needed
def edit(index: int) -> None:              # Edits todo, no return needed
def complete(index: int) -> None:          # Completes todo, no return needed
def clear_terminal() -> None:              # Performs action, no return needed
def pause_terminal() -> None:              # Waits for input, no return needed
def main() -> None:                        # Main program, no return needed

❌ WRONG Usage Examples:
def get_todos() -> None:                   # Should return list of todos
def validate_input(text: str) -> None:     # Should return bool (valid/invalid)
def calculate_length(text: str) -> None:   # Should return int (length)

=== QUICK DECISION GUIDE ===

Ask yourself:
1. "Does this function DO something?" → Use `-> None`
2. "Does this function RETURN data?" → Use `-> DataType`
3. "Does this function sometimes return data?" → Use `-> DataType | None`
4. "Does this function handle errors?" → Use exceptions, not None

SIMPLE RULES:
- Action functions (save, print, clear) → `-> None`
- Data functions (get, calculate, find) → `-> DataType` or `-> DataType | None`
- Error conditions → Raise exceptions, don't return None
- Empty collections → Return [], not None

PROFESSIONAL BENEFIT:
Using proper type hints makes your code self-documenting and helps other 
developers (including future you) understand function behavior immediately.
"""

print("\n" + "="*60)
print("FUNCTIONS REVISION COMPLETE")
print("="*60)
