# ============================================
# PYTHON OPERATOR OVERLOADING - COMPLETE GUIDE
# ============================================

'''
WHAT IS OPERATOR OVERLOADING?
- Python operators work for built-in classes but behave differently with different types
- This lets your objects behave like built-in types with operators, making your code more natural and readable.
- Examples of same operator, different behavior:
  * + operator: 5 + 3 = 8 (arithmetic addition)
  * + operator: [1,2] + [3,4] = [1,2,3,4] (list concatenation)  
  * + operator: "Hello" + "World" = "HelloWorld" (string concatenation)

- This feature allowing same operator to have different meanings according to context
  is called OPERATOR OVERLOADING

HOW IT WORKS:
- Python uses special methods (magic methods) with double underscores
- When you use an operator, Python automatically calls the corresponding method
- Format: __methodname__ (dunder methods)
- You can define these methods in your custom classes to make them work with operators
'''

# ============================================
# ARITHMETIC OPERATOR OVERLOADING REFERENCE
# ============================================

# Addition: obj1 + obj2 → obj1.__add__(obj2)
# def __add__(self, other):
#     return SomeClass(self.value + other.value)

# Subtraction: obj1 - obj2 → obj1.__sub__(obj2)
# def __sub__(self, other):
#     return SomeClass(self.value - other.value)

# Multiplication: obj1 * obj2 → obj1.__mul__(obj2)
# def __mul__(self, other):
#     return SomeClass(self.value * other.value)

# Division: obj1 / obj2 → obj1.__truediv__(obj2)
# def __truediv__(self, other):
#     return SomeClass(self.value / other.value)

# Floor Division: obj1 // obj2 → obj1.__floordiv__(obj2)
# def __floordiv__(self, other):
#     return SomeClass(self.value // other.value)

# Modulo: obj1 % obj2 → obj1.__mod__(obj2)
# def __mod__(self, other):
#     return SomeClass(self.value % other.value)

# Power: obj1 ** obj2 → obj1.__pow__(obj2)
# def __pow__(self, other):
#     return SomeClass(self.value ** other.value)

# ============================================
# BITWISE OPERATOR OVERLOADING REFERENCE
# ============================================

# Bitwise Left Shift: obj1 << obj2 → obj1.__lshift__(obj2)
# def __lshift__(self, other):
#     return SomeClass(self.value << other.value)

# Bitwise Right Shift: obj1 >> obj2 → obj1.__rshift__(obj2)
# def __rshift__(self, other):
#     return SomeClass(self.value >> other.value)

# Bitwise AND: obj1 & obj2 → obj1.__and__(obj2)
# def __and__(self, other):
#     return SomeClass(self.value & other.value)

# Bitwise OR: obj1 | obj2 → obj1.__or__(obj2)
# def __or__(self, other):
#     return SomeClass(self.value | other.value)

# Bitwise XOR: obj1 ^ obj2 → obj1.__xor__(obj2)
# def __xor__(self, other):
#     return SomeClass(self.value ^ other.value)

# Bitwise NOT: ~obj1 → obj1.__invert__()
# def __invert__(self):
#     return SomeClass(~self.value)

# ============================================
# COMPARISON OPERATOR OVERLOADING REFERENCE
# ============================================

# Less than: obj1 < obj2 → obj1.__lt__(obj2)
# def __lt__(self, other):
#     return self.value < other.value

# Less than or equal: obj1 <= obj2 → obj1.__le__(obj2)
# def __le__(self, other):
#     return self.value <= other.value

# Equal to: obj1 == obj2 → obj1.__eq__(obj2)
# def __eq__(self, other):
#     return self.value == other.value

# Not equal: obj1 != obj2 → obj1.__ne__(obj2)
# def __ne__(self, other):
#     return self.value != other.value

# Greater than: obj1 > obj2 → obj1.__gt__(obj2)
# def __gt__(self, other):
#     return self.value > other.value

# Greater than or equal: obj1 >= obj2 → obj1.__ge__(obj2)
# def __ge__(self, other):
#     return self.value >= other.value

# ==========================================================
# PRACTICAL EXAMPLE: POINT CLASS WITH OPERATOR OVERLOADING
# ==========================================================

class myPoint:
    """
    A 2D Point class demonstrating operator overloading
    Shows how to make custom objects work with Python operators
    """
    
    def __init__(self, x=0, y=0):
        # Constructor: Initialize point coordinates
        self.x = x
        self.y = y
    
    def __str__(self):
        # String representation: Called when print() is used
        # This makes print(point_object) work nicely
        return f"{self.x}, {self.y}"
    
    def __add__(self, other):
        # Addition operator overloading: p1 + p2
        # Creates a new point by adding corresponding coordinates
        x = self.x + other.x 
        y = self.y + other.y 
        return myPoint(x, y)  # Return new Point object
    
    def __lt__(self, other):
        # Less than operator overloading: p1 < p2
        # Compares points by their distance from origin (magnitude)
        self_mag = (self.x ** 2) + (self.y ** 2)    # Distance² from origin
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag  # Return boolean comparison

# ============================================
# USING THE OVERLOADED OPERATORS
# ============================================

# Creating Point objects
p1 = myPoint(1, 2)  # Point at coordinates (1, 2)
p2 = myPoint(4, 5)  # Point at coordinates (4, 5)

# Using __str__ method (called by print)
print(p1)  # Output: 1, 2
print(p2)  # Output: 4, 5

print()  # Empty line for formatting

# Using overloaded operators (syntactic sugar)
print(p1 < p2)   # Uses __lt__ method - compares magnitudes
                 # p1 magnitude = √(1² + 2²) = √5 ≈ 2.24
                 # p2 magnitude = √(4² + 5²) = √41 ≈ 6.40
                 # Output: True (p1 is closer to origin)

print(p1 + p2)   # Uses __add__ method - adds coordinates
                 # Output: 5, 7 (1+4=5, 2+5=7)

print()

# Direct method calls (equivalent to operators above)
print(p1.__lt__(p2))   # Same as p1 < p2 - Output: True
print(p1.__add__(p2))  # Same as p1 + p2 - Output: 5, 7

# ============================================
# IMPORTANT CONCEPTS FOR REVISION
# ============================================

'''
KEY POINTS TO REMEMBER:

1. OPERATOR TO METHOD MAPPING:
   - Every operator has a corresponding magic method
   - Python automatically calls these methods when operators are used
   - p1 + p2 is syntactic sugar for p1.__add__(p2)
Syntactic sugar = a simpler or prettier way to write code that does the same thing as a longer or more complex version.

2. RETURN VALUES:
   - Arithmetic operators typically return new objects
   - Comparison operators return True/False
   - __str__ returns string representation

3. SELF vs OTHER:
   - self: The object on the left side of operator
   - other: The object on the right side of operator
   - In p1 + p2: p1 is self, p2 is other

4. CREATING NEW OBJECTS:
   - Arithmetic operations usually create and return new objects
   - Don't modify the original objects (immutability principle)
   - return myPoint(x, y) creates a new Point object

5. PRACTICAL APPLICATIONS:
   - Mathematical objects (vectors, matrices, complex numbers)
   - Custom data structures (custom lists, trees)
   - Domain-specific objects (money, measurements, coordinates)

6. AI/ML RELEVANCE:
   - NumPy arrays: array1 + array2 uses __add__
   - Pandas DataFrames: df1 + df2 uses __add__
   - TensorFlow/PyTorch tensors: tensor1 + tensor2 uses __add__
   - Makes mathematical code more readable and intuitive

7. COMMON PATTERNS:
   - Always define __str__ for readable output
   - Consider defining complementary operators (__eq__ with __ne__)
   - Use meaningful logic for comparisons
   - Return appropriate types (new objects for arithmetic, booleans for comparisons)

8. DEBUGGING TIPS:
   - Add print statements inside magic methods to see when they're called
   - Remember operator precedence still applies
   - Test with different data types and edge cases

9. BEST PRACTICES:
   - Keep operator behavior intuitive and expected
   - Don't overload operators in confusing ways
   - Document what your operators do
   - Consider type checking in methods for robustness

10. ADVANCED CONCEPTS:
    - Reverse operators (__radd__, __rsub__) for when left operand doesn't support operation
    - In-place operators (__iadd__, __isub__) for += style operations
    - Unary operators (__neg__, __pos__, __abs__) for -obj, +obj, abs(obj)

EXAMPLE OUTPUT EXPLANATION:
p1 = myPoint(1, 2)  # Point at (1, 2)
p2 = myPoint(4, 5)  # Point at (4, 5)

print(p1)           # Calls __str__ → Output: "1, 2"
print(p2)           # Calls __str__ → Output: "4, 5"
print(p1 < p2)      # Calls __lt__ → Output: True (√5 < √41)
print(p1 + p2)      # Calls __add__ → Output: "5, 7" (new Point(5,7))
'''

# ============================================
# ADDITIONAL USEFUL MAGIC METHODS
# ============================================

'''
OTHER IMPORTANT MAGIC METHODS:

__repr__(self): Developer-friendly string representation
__len__(self): Support for len() function
__bool__(self): Support for boolean conversion (if obj:)
__getitem__(self, key): Support for indexing (obj[key])
__setitem__(self, key, value): Support for assignment (obj[key] = value)
__contains__(self, item): Support for 'in' operator (item in obj)
__call__(self): Make object callable like a function (obj())

EXAMPLE EXTENSIONS TO POINT CLASS:
def __repr__(self):
    return f"Point({self.x}, {self.y})"

def __len__(self):
    return int((self.x**2 + self.y**2)**0.5)  # Distance from origin

def __bool__(self):
    return self.x != 0 or self.y != 0  # False only for origin (0,0)

def __eq__(self, other):
    return self.x == other.x and self.y == other.y

def __abs__(self):
    return (self.x**2 + self.y**2)**0.5  # Distance from origin

def __neg__(self):
    return myPoint(-self.x, -self.y)  # Negative point

def __mul__(self, scalar):
    return myPoint(self.x * scalar, self.y * scalar)  # Scale point
'''
