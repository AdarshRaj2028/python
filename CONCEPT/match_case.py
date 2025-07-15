"""
=============================================================================
PYTHON MATCH-CASE STATEMENT - ESSENTIAL GUIDE
=============================================================================

INTRODUCTION:
------------
Match-case is Python's pattern matching feature introduced in Python 3.10.
It's like a more powerful switch statement that can match patterns in data.
In Python's match-case (introduced in Python 3.10), you can use the | (bitwise OR) operator,
to match multiple literal patterns in a single case. 

BASIC SYNTAX:
------------
match expression:
    case pattern1:
        # code block
    case pattern2:
        # code block
    case _:  # default case (optional)
        # code block

=============================================================================
BASIC PATTERN MATCHING
=============================================================================

LITERAL MATCHING:
----------------
Match exact values like numbers, strings, booleans
"""

def basic_examples():
    """Simple literal value matching"""
    
    def check_grade(letter):
        match letter:
            case 'A':
                return "Excellent"
            case 'B':
                return "Good"
            case 'C':
                return "Average"
            case 'D':
                return "Below Average"
            case 'F':
                return "Fail"
            case _:  # Default case
                return "Invalid Grade"
    
    # Test examples
    print(check_grade('A'))  # Output: Excellent
    print(check_grade('C'))  # Output: Average
    print(check_grade('X'))  # Output: Invalid Grade

"""
VARIABLE PATTERN MATCHING:
-------------------------
Capture values into variables during matching
"""

def variable_examples():
    """Variable capture in patterns"""
    
    def categorize_age(age):
        match age:
            case x if x < 13:
                return f"Child: {x} years old"
            case x if 13 <= x < 20:
                return f"Teenager: {x} years old"
            case x if x >= 20:
                return f"Adult: {x} years old"
    
    # Test examples
    print(categorize_age(10))   # Output: Child: 10 years old
    print(categorize_age(16))   # Output: Teenager: 16 years old
    print(categorize_age(25))   # Output: Adult: 25 years old

"""
=============================================================================
LIST PATTERN MATCHING
=============================================================================

SIMPLE LIST MATCHING:
--------------------
Match list structures and extract elements
"""

def list_examples():
    """Basic list pattern matching"""
    
    def analyze_list(items):
        match items:
            case []:
                return "Empty list"
            case [x]:
                return f"Single item: {x}"
            case [x, y]:
                return f"Two items: {x} and {y}"
            case [first, *rest]:
                return f"First: {first}, Rest: {rest}"
    
    # Test examples
    print(analyze_list([]))           # Empty list
    print(analyze_list([5]))          # Single item: 5
    print(analyze_list([1, 2]))       # Two items: 1 and 2
    print(analyze_list([1, 2, 3, 4])) # First: 1, Rest: [2, 3, 4]

"""
=============================================================================
DICTIONARY PATTERN MATCHING
=============================================================================

SIMPLE DICTIONARY MATCHING:
--------------------------
Match dictionary structures
"""

def dictionary_examples():
    """Basic dictionary pattern matching"""
    
    def process_person(person):
        match person:
            case {"name": str(name), "age": int(age)}:
                return f"Person: {name}, Age: {age}"
            case {"name": str(name)}:
                return f"Person: {name} (age unknown)"
            case {"error": str(msg)}:
                return f"Error: {msg}"
            case {}:
                return "Empty data"
    
    # Test examples
    print(process_person({"name": "Alice", "age": 25}))  # Person: Alice, Age: 25
    print(process_person({"name": "Bob"}))               # Person: Bob (age unknown)
    print(process_person({"error": "Not found"}))        # Error: Not found
    print(process_person({}))                            # Empty data

"""
=============================================================================
PRACTICAL EXAMPLES
=============================================================================

SIMPLE CALCULATOR:
-----------------
Basic calculator using match-case
"""

def calculator_example():
    """Simple calculator with match-case"""
    
    def calculate(operation, a, b):
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b if b != 0 else "Cannot divide by zero"
            case _:
                return "Unknown operation"
    
    # Test examples
    print(calculate("add", 5, 3))       # 8
    print(calculate("multiply", 4, 2))  # 8
    print(calculate("divide", 10, 2))   # 5.0
    print(calculate("divide", 10, 0))   # Cannot divide by zero

"""
SIMPLE COMMAND HANDLER:
----------------------
Handle basic commands
"""

def command_example():
    """Simple command handling"""
    
    def handle_command(command):
        match command:
            case ["help"]:
                return "Available commands: help, quit, save"
            case ["quit"]:
                return "Goodbye!"
            case ["save", filename]:
                return f"Saving to {filename}"
            case ["open", filename]:
                return f"Opening {filename}"
            case _:
                return "Unknown command"
    
    # Test examples
    print(handle_command(["help"]))           # Available commands: help, quit, save
    print(handle_command(["save", "data.txt"])) # Saving to data.txt
    print(handle_command(["invalid"]))        # Unknown command

"""
=============================================================================
WHEN TO USE MATCH-CASE
=============================================================================

GOOD FOR:
--------
- Multiple specific value checks (like grade checking)
- Pattern matching in lists and dictionaries
- Command parsing
- Data validation with different formats

AVOID FOR:
---------
- Simple if-else (just 2-3 conditions)
- Complex mathematical comparisons
- When using Python < 3.10

COMPARISON WITH IF-ELIF:
-----------------------
# Instead of this:
if grade == 'A':
    return "Excellent"
elif grade == 'B':
    return "Good"
elif grade == 'C':
    return "Average"
else:
    return "Invalid"

# Use this:
match grade:
    case 'A':
        return "Excellent"
    case 'B':
        return "Good"
    case 'C':
        return "Average"
    case _:
        return "Invalid"

=============================================================================
QUICK REFERENCE
=============================================================================

BASIC PATTERNS:
--------------
case 42:                    # Exact value
case x:                     # Capture any value
case x if x > 10:          # With condition
case _:                     # Default (any value, don't capture)

LIST PATTERNS:
-------------
case []:                    # Empty list
case [x]:                   # Single item
case [x, y]:               # Exactly two items
case [first, *rest]:       # First item + remaining items

DICT PATTERNS:
-------------
case {}:                           # Empty dict
case {"key": value}:              # Specific key-value
case {"name": str(n), "age": int(a)}: # Type checking

=============================================================================
"""

# Example usage
if __name__ == "__main__":
    print("=== BASIC EXAMPLES ===")
    basic_examples()
    
    print("\n=== VARIABLE EXAMPLES ===")
    variable_examples()
    
    print("\n=== LIST EXAMPLES ===")
    list_examples()
    
    print("\n=== DICTIONARY EXAMPLES ===")
    dictionary_examples()
    
    print("\n=== CALCULATOR EXAMPLE ===")
    calculator_example()
    
    print("\n=== COMMAND EXAMPLE ===")
    command_example()
