# ===============================
# PYTHON PROPERTY - SIMPLE GUIDE
# ===============================

"""
What is a property?
- A property lets you control access to an attribute (variable) in a class.
- You can add validation, make it read-only, or compute its value on the fly.
- You use it like an attribute, but it works like a method behind the scenes.
- Python properties let you control access to class attributes by adding logic (like validation) when getting or setting values. 
- They make your code safer and cleaner, allowing you to use attributes as if they were simple variables.
- Encapsulation is the blueprint or concept—the idea of hiding data and controlling access in OOP.
- Properties in Python are the practical tool (the “product”) that lets you implement encapsulation in real code.

Why use property?
- To protect data (validation)
- To make code cleaner (no need to call get/set methods)
- To create read-only or computed attributes


Attributes are variables that belong to an object or a class.

In our examples, attributes are things like:

self._temperature in TempCelsius and Celsius
self.value or self._value in Simple and WithProperty
self.first, self.last, and self._age in Person

They store data about each object. For example, self._temperature stores the temperature value for each Celsius object.

"""

# 1. Need for using properties

# We need properties in Python to control how attributes are accessed and changed, 
# especially when we want to add validation or make an attribute read-only.

# Why is this useful?

# Suppose you have a class for a student’s marks. You want to make sure the marks are always between 0 and 100.
# If you use a normal attribute, anyone can set it to any value — even a negative number or 200!

# Student class example

# Without property (No validation)

class Student:
    def __init__(self, marks):
        self.marks = marks

s = Student(0)
s.marks = 150  # No error! This is not valid.

# With property (With validation)

class Student1:
    def __init__(self, marks):
        self._marks = marks

    @property  # @property makes the marks method act like an attribute getter.
    def marks(self):   # This is getter method for marks.
        return self._marks

    @marks.setter  # @marks.setter lets you define what happens when you set marks.
    def marks(self, value):  # This is setter method for marks.
           if 0 <= value <= 100:
                self._marks = value
           else:
                raise ValueError("Marks must be between 0 and 100")
# Now, s.marks = 90 will call the setter and check the value automatically.
s = Student1(0)
try: 
    s.marks = 150  # Raises ValueError! Now you can't set invalid marks.
except ValueError as e:
    print("Error:", e)
# Student1(90) sets the initial value when you create the object.
# s.marks = 150 tries to change the value later, and the setter checks if it's valid.

'''
An attribute getter is a method that is called when you read (access) an attribute,s value.
An attribute setter is a method that is called when you assign (set) a new value to an attribute.

Getters and setters were introduced to let you control access to attributes in a clean, Pythonic way!

The function names must be the same!

The getter and setter must have the same name (e.g., marks), so Python knows they are for the same property.
The @property decorator creates the getter.
The @marks.setter decorator creates the setter for the same property.
'''

# 2. Using property() function (Old way)
class TempCelsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
    temperature = property(get_temperature, set_temperature)

print("\n--- property() function example ---")
c1 = TempCelsius(10)
print("Initial temp:", c1.temperature)
c1.temperature = 30
print("Changed temp:", c1.temperature)
# c1.temperature = -300  # Uncomment to see validation error #hey there

# 3. Using @property decorator (Recommended way)
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

print("\n--- @property decorator example ---")
c2 = Celsius(15)
print("Initial temp:", c2.temperature)
c2.temperature = 50
print("Changed temp:", c2.temperature)
# c2.temperature = -300  # Uncomment to see validation error

# 4. Comparison: Different ways to manage attributes
class Traditional:
    def __init__(self, value=0):
        self._value = value
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value = value

class Simple:
    def __init__(self, value=0):
        self.value = value  # No validation

class WithProperty:
    def __init__(self, value=0):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self._value = value

print("\n--- Comparison of approaches ---")
t = Traditional(10)
print("Traditional get:", t.get_value())
t.set_value(20)
print("Traditional set:", t.get_value())

s = Simple(10)
print("Simple direct:", s.value)
s.value = 20
print("Simple set:", s.value)

p = WithProperty(10)
print("Property get:", p.value)
p.value = 30
print("Property set:", p.value)
# p.value = -5  # Uncomment to see validation error

# 5. More property examples
class Person:
    def __init__(self, first, last, age=0):
        self.first = first
        self.last = last
        self._age = age
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value
    @property
    def is_adult(self):
        return self._age >= 18

print("ADVANCED PROPERTY EXAMPLES")
print("="*60)

person = Person("John", "Doe", 25)
print(f"Full name: {person.full_name}")    # Computed property
print(f"Age: {person.age}")                # Property with validation

# person.age (the property) and person._age (the attribute) will both give you the same value, because the property simply returns self._age.
# person.age calls the property method (which can include validation or logic).
# person._age accesses the attribute directly (no validation, just the raw value).
print(f"Is adult: {person.is_adult}")      # Boolean property
print()
# Example: Difference between public, _protected, and __private attributes
print("\n--- Attribute Naming Example ---")

class Demo:
    def __init__(self):
        self.age = 10           # public
        self._age = 20         # protected (by convention)
        self.__age = 30        # private (name mangling)

    @property
    def age_property(self):
        return self.__age      # property to access __age

obj = Demo()
print("obj.age (public):", obj.age)           # 10
print("obj._age (protected):", obj._age)     # 20
# print(obj.__age)  # AttributeError!
print("obj._Demo__age (private):", obj._Demo__age)  # type: ignore # 30 (name mangled)
# but its not recommended to access like this
# Accessing private attributes directly is not recommended, but you can do it using name mangling
print("obj.age_property (property):", obj.age_property)  # 30 (via property)

# Summary:
# - obj.age is public, can be accessed directly.
# - obj._age is 'protected' by convention, but still accessible.
# - obj.__age is name-mangled, not directly accessible.
# - obj.age_property is a property that lets you access __age safely.

# ============================================================================
# KEY REVISION POINTS
# ============================================================================

"""
PROPERTY CREATION METHODS:
1. property() function: temperature = property(getter, setter, deleter, doc)
2. @property decorator: More readable and Pythonic

BENEFITS OF PROPERTIES:
✓ Clean syntax (obj.attr instead of obj.get_attr())
✓ Data validation and error handling
✓ Computed properties (calculated on-the-fly)
✓ Backward compatibility (can convert attributes to properties)
✓ Encapsulation (hide internal implementation)
✓ Read-only attributes (getter without setter)

DECORATOR TYPES:
- @property: Creates getter method
- @attr.setter: Creates setter method  
- @attr.deleter: Creates deleter method

NAMING CONVENTIONS:
- _attribute: Private attribute (internal use)
- attribute: Public property (external access)

WHEN TO USE PROPERTIES:
✓ Need data validation
✓ Want computed/calculated attributes
✓ Need to maintain backward compatibility
✓ Want to control attribute access
✓ Creating read-only attributes

PROPERTY vs REGULAR ATTRIBUTES:
- Regular: Direct access, no validation, stored value
- Property: Method calls, validation possible, can be computed
"""
print()
print("REVISION SUMMARY")
print("="*60)
print("1. property() function: Traditional but verbose")
print("2. @property decorator: Modern and clean")
print("3. Use for validation, computed values, and clean APIs")
print("4. Essential for professional Python development")
print("="*60)
