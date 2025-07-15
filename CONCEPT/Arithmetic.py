# ============================================================================
# PYTHON ARITHMETIC OPERATORS - COMPREHENSIVE GUIDE FOR REVISION
# ============================================================================

"""
PYTHON INPUT BEHAVIOR:
- Python's input() function ALWAYS returns a string by default
- You must explicitly convert to int, float, etc. using type casting
- Example: int(input()), float(input()), str(input())
"""

# ============================================================================
# ARITHMETIC OPERATORS DEMONSTRATION
# ============================================================================

# Initialize test values
a = 9      # Integer
b = 5.5    # Float

print("="*60)
print("ARITHMETIC OPERATORS IN PYTHON")
print("="*60)

# FLOOR DIVISION OPERATOR (//)
print(f"Floor Division: {a} // {b} = {a // b}")
"""
FLOOR DIVISION (//):
- Also called "integer division"
- Returns the largest integer less than or equal to the division result
- Always rounds DOWN to the nearest integer
- Works with both int and float operands
- Result type depends on operands: int//int = int, int//float = float
"""

# REGULAR DIVISION OPERATOR (/)
print(f"Regular Division: {a} / {b} = {a / b}")
"""
REGULAR DIVISION (/):
- Always returns a float in Python 3
- Gives the exact mathematical result
- Even if both operands are integers: 9/3 = 3.0 (not 3)
"""

# EXPONENTIATION OPERATOR (**)
print(f"Exponentiation: {a} ** {b} = {a ** b}")
"""
EXPONENTIATION (**):
- Raises first number to the power of second number
- a ** b means "a to the power of b"
- Can handle fractional powers (roots): 9 ** 0.5 = 3.0 (square root)
"""

# ============================================================================
# UNARY OPERATORS AND MULTIPLE OPERATOR SEQUENCES
# ============================================================================

print("\n" + "="*60)
print("UNARY OPERATORS - CORRECTED EXPLANATION")
print("="*60)

# DOUBLE PLUS (++) - NOT AN INCREMENT OPERATOR
print(f"Double plus: {a} ++ {b} = {a ++ b}")
"""
IMPORTANT CLARIFICATION:
- a ++ b DOES work in Python and equals 14.5
- This is NOT an increment operator like in C++ or Java
- Python interprets ++ as two unary plus operators: a + (+b)
- The ++ sequence means "plus positive" not "increment"
"""

# DOUBLE MINUS (--) - NOT A DECREMENT OPERATOR  
print(f"Double minus: {a} -- {b} = {a -- b}")
"""
DOUBLE MINUS EXPLANATION:
- a -- b DOES work in Python and equals 14.5
- This is NOT a decrement operator
- Python interprets -- as: a - (-b) = a + b
- The -- sequence means "minus negative" which equals "plus"
"""

print("\nUNARY OPERATOR EXAMPLES:")
print(f"  +{b} = {+b}")           # Unary plus (no change)
print(f"  -{b} = {-b}")           # Unary minus (negation)
print(f"  ++{b} = {++b}")         # Double unary plus (no change)
print(f"  --{b} = {--b}")         # Double unary minus (no change)
print(f"  ---{b} = {---b}")       # Triple unary minus (negation)
print(f"  ----{b} = {----b}")     # Quadruple unary minus (no change)

print("\nRULE: Odd number of minus signs = negative, Even = positive")

# ============================================================================
# WHAT PYTHON ACTUALLY DOESN'T SUPPORT
# ============================================================================

print("\n" + "="*60)
print("WHAT PYTHON DOESN'T SUPPORT")
print("="*60)

"""
PYTHON DOESN'T SUPPORT STANDALONE INCREMENT/DECREMENT:
a++     (SyntaxError)
++a     (SyntaxError) 
a--     (SyntaxError)
--a     (SyntaxError)

CORRECT WAYS TO INCREMENT/DECREMENT:
a = a + 1  or  a += 1
a = a - 1  or  a -= 1
"""

# Demonstrate correct increment/decrement
x = 10
print(f"Original x: {x}")

x += 1  # Correct increment
print(f"After x += 1: {x}")

x -= 1  # Correct decrement  
print(f"After x -= 1: {x}")

# These would cause SyntaxError if uncommented:
# x++    # Error: invalid syntax
# ++x    # Error: invalid syntax

# ============================================================================
# MODULO OPERATOR (%)
# ============================================================================

print(f"\nModulo: {a} % {b} = {a % b}")
"""
MODULO OPERATOR (%):
- Returns the remainder after division
- Sign of result follows the sign of the divisor (second operand)
- If divisor is negative, remainder will be negative
- Examples: 9 % 5.5 = 3.5, 9 % -5.5 = -2.0
"""

print("\n" + "="*60)
print("MODULO WITH NEGATIVE NUMBERS")
print("="*60)

# Demonstrating modulo with negative numbers
positive_divisor = 7 % 3
negative_divisor = 7 % -3
print(f"7 % 3 = {positive_divisor}")    # Positive divisor, positive result
print(f"7 % -3 = {negative_divisor}")   # Negative divisor, negative result
print("RULE: Remainder sign follows divisor sign")

# ============================================================================
# USER INPUT AND TYPE CONVERSION
# ============================================================================

print("\n" + "="*60)
print("USER INPUT AND TYPE CONVERSION")
print("="*60)

"""
INPUT PROCESS:
1. input() returns string
2. float() converts string to floating-point number
3. Arithmetic operations performed
4. int() converts result back to integer (truncates decimal part)
"""

try:
    x = float(input("Enter first value: "))
    y = float(input("Enter second value: "))
    
    print(f"\nInput values: x = {x}, y = {y}")
    print(f"Sum as float: {x + y}")
    
    # Convert sum to integer (truncates decimal part)
    c = int(x + y)
    print(f"Sum as integer: {c}")
    
    print("\nNOTE: int() truncates decimal part, doesn't round")
    print(f"Example: int(5.9) = {int(5.9)}, not 6")
    
except ValueError as e:
    print(f"ValueError: Please enter valid numbers. {e}")

# ============================================================================
# ADDITIONAL ARITHMETIC OPERATIONS
# ============================================================================

print("\n" + "="*60)
print("ADDITIONAL ARITHMETIC OPERATIONS")
print("="*60)

# More arithmetic examples
a, b = 9, 5.5

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# ============================================================================
# OPERATOR PRECEDENCE AND ASSOCIATIVITY
# ============================================================================

print("\n" + "="*60)
print("OPERATOR PRECEDENCE (HIGH TO LOW)")
print("="*60)

"""
OPERATOR PRECEDENCE ORDER:
1. ** (Exponentiation) - Right to left associativity
2. +x, -x (Unary plus/minus) - Right to left
3. *, /, //, % (Multiplication, Division, Floor division, Modulo) - Left to right
4. +, - (Addition, Subtraction) - Left to right

EXAMPLES:
"""

expression1 = 2 + 3 * 4      # = 2 + 12 = 14 (not 20)
expression2 = 2 ** 3 ** 2    # = 2 ** 9 = 512 (not 64, right-to-left)
expression3 = 10 - 3 * 2     # = 10 - 6 = 4 (not 14)

print(f"2 + 3 * 4 = {expression1}")
print(f"2 ** 3 ** 2 = {expression2}")
print(f"10 - 3 * 2 = {expression3}")

# ============================================================================
# COMMON MISTAKES AND BEST PRACTICES
# ============================================================================

print("\n" + "="*60)
print("COMMON MISTAKES AND BEST PRACTICES")
print("="*60)

"""
COMMON MISTAKES:
- Thinking ++ and -- are increment/decrement operators
- Forgetting to convert input() to appropriate type
- Confusing / and // operators
- Not understanding modulo with negative numbers
- Ignoring operator precedence
- Misunderstanding unary operator sequences

BEST PRACTICES:
- Always convert input() to required type
- Use parentheses for clarity in complex expressions
- Understand the difference between / and //
- Be aware of operator precedence
- Use meaningful variable names
- Use += and -= for increment/decrement
- Avoid confusing unary operator sequences like ++ and --
"""

# Examples of best practices
try:
    user_age = int(input("Enter your age: "))  # Clear variable name, proper conversion
    calculation = (a + b) * 2  # Parentheses for clarity
    is_even = (user_age % 2) == 0  # Clear boolean expression

    print(f"User age: {user_age}")
    print(f"Calculation with parentheses: ({a} + {b}) * 2 = {calculation}")
    print(f"Is age even? {is_even}")
except ValueError:
    print("Please enter a valid integer for age.")

# ============================================================================
# KEY REVISION POINTS
# ============================================================================

"""
REVISION CHECKLIST:

ARITHMETIC OPERATORS:
-> + (Addition), - (Subtraction), * (Multiplication)
-> / (Division - always returns float)
-> // (Floor Division - rounds down to nearest integer)
-> % (Modulo - returns remainder)
-> ** (Exponentiation - power operation)

UNARY OPERATORS:
-> +x (Unary plus - no change)
-> -x (Unary minus - negation)
-> Multiple unary operators: ++, --, +++, etc. are valid
-> ++ and -- are NOT increment/decrement operators

INPUT/OUTPUT:
-> input() always returns string
-> Use int(), float(), str() for type conversion
-> Handle ValueError for invalid inputs

OPERATOR PRECEDENCE:
-> ** (highest, right-to-left)
-> Unary +, -
-> *, /, //, %
-> +, - (lowest, left-to-right)
-> Use parentheses for clarity

SPECIAL CASES:
-> Modulo sign follows divisor
-> Floor division with floats returns float
-> Python 3 division always returns float
-> Use += and -= for increment/decrement

ERROR HANDLING:
-> Use try-except for input validation
-> Check for division by zero
-> Validate user input types
"""

print("\n" + "="*60)
print("ARITHMETIC OPERATORS REVISION COMPLETE")
print("="*60)
