# ============================================================================
# PYTHON CLOSURES - COMPREHENSIVE GUIDE FOR REVISION
# ============================================================================

"""
WHAT IS A CLOSURE?

A closure = inner function + outer function's variables (remembered and accessible later).

A closure is a function that "remembers" variables from the place where it was created,
even after that place is no longer active in memory.
Closures are best when you want to “fix” some arguments and reuse the function with different inputs, 
making your code more modular and reusable. 
Regular functions are fine when you always want to provide all arguments every time.

Think of it like a backpack that a function carries with it, containing all the 
variables it needs from its "home" environment.

A closure specifically means:

-> The inner function uses variables from the outer function (enclosing scope).
-> The outer function returns the inner function.
-> The returned inner function “remembers” the values from the outer function,
even after the outer function has finished.
-> All closures are nested functions, but not all nested functions are closures.

If you just write a function inside another function but don't use any variables from the outer function, 
or don't return the inner function, it's not a closure.

KEY COMPONENTS:
1. Outer function (enclosing function)
2. Inner function (nested function) 
3. Inner function uses variables from outer function
4. Outer function returns the inner function
5. The returned function "remembers" the outer function's variables
"""

# ============================================================================
# BASIC CLOSURE EXAMPLE - MESSAGE PRINTER
# ============================================================================

def print_message(message):  # OUTER/ENCLOSING FUNCTION
    """
    This is the outer function that takes a message parameter.
    It creates and returns an inner function that remembers this message.
    """
    
    def print_message_inner():  # INNER/NESTED FUNCTION
        """
        This inner function has access to the 'message' variable 
        from its parent function, even after the parent function finishes.
        This is the CLOSURE - it "closes over" the message variable.
        """
        print(message)  # Uses 'message' from outer function scope
    
    # Return the inner function (not calling it, just returning the function object)
    return print_message_inner

print("="*60)
print("BASIC CLOSURE DEMONSTRATION")
print("="*60)

# CREATING A CLOSURE
# When we call print_message("Hello"), it returns the inner function
# The inner function remembers the message "Hello" even though 
# print_message() has finished executing
another = print_message("Hello")

# Now 'another' is a function that remembers "Hello"
another()  # Output: Hello

# We can create multiple closures with different messages
greeting1 = print_message("Good Morning!")
greeting2 = print_message("Good Evening!")

greeting1()  # Output: Good Morning!
greeting2()  # Output: Good Evening!

print("\n" + "="*60)

# ============================================================================
# PRACTICAL CLOSURE EXAMPLE - MULTIPLIER FACTORY
# ============================================================================

def multiplier_outer(n):  # OUTER FUNCTION - takes a multiplier value
    """
    This function creates customized multiplier functions.
    Each returned function remembers its specific multiplier value.
    This is like a "function factory" - it manufactures specialized functions.
    """
    
    def multiplier_inner(x):  # INNER FUNCTION - takes the number to multiply
        """
        This function multiplies the input 'x' by the remembered value 'n'.
        It has access to 'n' from the outer function scope.
        """
        return x * n  # 'n' comes from the outer function's parameter
    
    return multiplier_inner  # Return the customized multiplier function

print("PRACTICAL CLOSURE DEMONSTRATION - FUNCTION FACTORY")
print("="*60)

# CREATE SPECIALIZED MULTIPLIER FUNCTIONS
# Each function remembers its own multiplier value

times3 = multiplier_outer(3)  # Creates a function that multiplies by 3
times5 = multiplier_outer(5)  # Creates a function that multiplies by 5

# Now we have two different functions, each with their own "memory"
print(f"3 x 9 = {times3(9)}")    # Output: 27
print(f"5 x 3 = {times5(3)}")    # Output: 15

# COMBINING CLOSURES
# We can even use one closure's result as input to another
result = times5(times3(2))  # First: 3×2=6, Then: 5×6=30
print(f"5 x (3 x 2) = {result}")  # Output: 30

print("\n" + "="*60)

# ============================================================================
# WHY ARE CLOSURES USEFUL? - REAL WORLD EXAMPLES
# ============================================================================

print("REAL-WORLD CLOSURE APPLICATIONS")
print("="*60)

# EXAMPLE 1: CONFIGURATION FUNCTIONS
def create_logger(prefix):
    """Creates a logging function with a specific prefix"""
    def log(message):
        print(f"[{prefix}] {message}")
    return log

# Create different loggers for different parts of your application
error_logger = create_logger("ERROR")
info_logger = create_logger("INFO")
debug_logger = create_logger("DEBUG")

error_logger("Database connection failed")  # [ERROR] Database connection failed
info_logger("User logged in successfully")  # [INFO] User logged in successfully
debug_logger("Processing user data")        # [DEBUG] Processing user data

print()

# EXAMPLE 2: COUNTER FUNCTIONS (STATEFUL FUNCTIONS)
def create_counter(start=0):
    """Creates a counter function that remembers its current count"""
    count = start  # This variable is "captured" by the closure
    
    def counter():
        nonlocal count  # Allows us to modify the captured variable
        count += 1
        return count
    
    return counter

# Create independent counters
counter1 = create_counter(0)   # Starts from 0
counter2 = create_counter(100) # Starts from 100

print("Counter 1:", counter1())  # 1
print("Counter 1:", counter1())  # 2
print("Counter 2:", counter2())  # 101
print("Counter 1:", counter1())  # 3
print("Counter 2:", counter2())  # 102

print()

# EXAMPLE 3: MATHEMATICAL FUNCTION GENERATORS
def create_power_function(power):
    """Creates functions that raise numbers to a specific power"""
    def power_function(base):
        return base ** power
    return power_function

square = create_power_function(2)    # x²
cube = create_power_function(3)      # x³
fourth_power = create_power_function(4)  # x⁴

print(f"5² = {square(5)}")           # 25
print(f"3³ = {cube(3)}")             # 27
print(f"2⁴ = {fourth_power(2)}")     # 16

print("\n" + "="*60)

# ============================================================================
# CLOSURE vs CLASS COMPARISON
# ============================================================================

print("CLOSURE vs CLASS - WHEN TO USE WHICH?")
print("="*60)

# USING A CLASS (Object-Oriented Approach)
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def multiply(self, value):
        return value * self.factor

# USING A CLOSURE (Functional Approach)
def create_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply

# Both achieve the same result
class_multiplier = Multiplier(7)
closure_multiplier = create_multiplier(7)

print(f"Class approach: {class_multiplier.multiply(6)}")    # 42
print(f"Closure approach: {closure_multiplier(6)}")        # 42

print("\n" + "="*60)

# ============================================================================
# KEY REVISION POINTS
# ============================================================================

"""
CLOSURE CHECKLIST - WHAT MAKES A CLOSURE:
✓ Nested function (inner function inside outer function)
✓ Inner function references variables from outer function
✓ Outer function returns the inner function
✓ The returned function "remembers" the outer function's variables

WHEN TO USE CLOSURES:
✓ Creating specialized functions (function factories)
✓ Maintaining state without classes
✓ Configuration functions with preset values
✓ Event handlers that need to remember context
✓ Decorators (advanced topic)

BENEFITS OF CLOSURES:
✓ Cleaner code than global variables
✓ Data encapsulation (variables are private to the closure)
✓ Function customization and reusability
✓ Memory efficient for simple stateful operations
✓ Functional programming patterns

CLOSURE vs OTHER APPROACHES:
- Closure vs Global Variables: Closures are safer and cleaner
- Closure vs Classes: Closures are simpler for single-method objects
- Closure vs Regular Functions: Closures can maintain state

COMMON PITFALLS:
⚠ Late binding in loops (variables change after closure creation)
⚠ Memory usage (closures keep references to outer scope)
⚠ Debugging can be more complex

REAL-WORLD USAGE:
- Web frameworks (Flask, Django) use closures extensively
- Event handling and callbacks
- Configuration and settings management
- Decorators and middleware
- Functional programming patterns
"""

print("CLOSURE REVISION SUMMARY")
print("="*60)
print("1. Closure = Inner function + Outer function's variables")
print("2. Used for: Function factories, state management, configuration")
print("3. Benefits: Clean code, encapsulation, reusability")
print("4. Common in: Web frameworks, decorators, callbacks")
print("5. Alternative to: Global variables, simple classes")
print("="*60)

# ============================================================================
# PRACTICE EXERCISES (Uncomment to try)
# ============================================================================

"""
EXERCISE 1: Create a closure that generates greeting functions
def create_greeter(greeting):
    # Your code here
    pass

hello = create_greeter("Hello")
hi = create_greeter("Hi")
print(hello("Alice"))  # Should print: Hello, Alice!
print(hi("Bob"))       # Should print: Hi, Bob!

EXERCISE 2: Create a closure-based calculator
def create_calculator(operation):
    # Your code here (operation can be 'add', 'subtract', 'multiply', 'divide')
    pass

add_10 = create_calculator('add')(10)
multiply_5 = create_calculator('multiply')(5)
"""
