# ============================================
# OBJECT-ORIENTED PROGRAMMING (OOP) - COMPLETE GUIDE
# ============================================

'''
WHAT IS OOP?
- Python is a multi-paradigm programming language supporting different approaches
- OOP is one popular approach that solves problems by creating objects
- An object has two main characteristics:
  1. Attributes (data/properties) - what it HAS
  2. Behaviors (methods/functions) - what it CAN DO

REAL-WORLD EXAMPLE:
Dog Object:
- Attributes: name, age, height, weight, color
- Behaviors: barking, wagging, running

OOP BENEFITS:
- Creates reusable code (DRY - Don't Repeat Yourself principle)
- Makes code more organized and maintainable
- Models real-world entities effectively

FUNDAMENTAL OOP PRINCIPLES:
1. INHERITANCE: Using details from existing class in new class without modification
2. ENCAPSULATION: Hiding private details of class from other objects
3. POLYMORPHISM: Using common operations differently for different data types

KEY TERMINOLOGY:
- CLASS: Blueprint/template for creating objects
- OBJECT: Instance created from a class (instantiation process)
- CONSTRUCTOR: __init__ method that initializes each object, The __init__ method is a constructor.
Its job is to set up (initialize) the object's attributes when you create an object.
It does not return values; it just sets up the object.
We use parentheses() when creating an object(calling the constructor), 
and you use = to set or change an attribute after the object exists.
- METHODS: Functions defined inside class that describe object actions

In Python, variable names can start with different numbers of underscores, 
and each style has a specific meaning, especially inside classes. 
Here's what we should know about variable naming conventions in Python OOP:

1. Public Variables
Example: self.name
Can be accessed from anywhere (inside or outside the class).
No underscore at the start.
2. Protected Variables (Convention)
Example: self._percentage
Single underscore _ at the start.
By convention, it means “for internal use only” (should not be accessed directly from outside the class), but it's still accessible.
3. Private Variables (Name Mangling)
Example: self.__balance
Double underscore __ at the start.
Python “mangles” the name to prevent accidental access from outside the class (e.g., self.__balance becomes _ClassName__balance).
Used to avoid name conflicts in subclasses and to make it harder to access from outside.

-> Name Mangaling: Name mangling is a mechanism in Python that changes the name of a variable that starts with two underscores(__) inside a class.
This is done to make the variable harder to access from outside the class and to avoid accidental name conflicts in subclasses.

4. Special (Magic/Dunder) Variables
Example: __init__, __str__
Double underscores at the start and end.
These are reserved for special methods in Python (don't use this style for your own variables).


Hence, Use _varName when you want to signal "internal use" but don't need strict privacy.
Use __varName when you want to make the variable private and avoid accidental access or conflicts.


KEY DIFFERENCE BETWEEN CLASS AND OBJECT
- Class id logical, Object is physical
- Class is defined once, Objects can be many
- Object uses memory, Class does not 
'''

# ============================================
# BASIC CLASS DEFINITION AND OBJECT CREATION
# ============================================

# Simple class with constructor and methods
class myBird:
    def __init__(self):
        # Constructor automatically runs when object is created
        print("myBird class constructor is executing...")
        # self refers to the specific object being created
    
    def whatType(self):
        # Instance method - belongs to each object
        print("I am a Bird")
    
    def canSwim(self):
        print("I can Swim")

# ============================================
# CLASS WITH ATTRIBUTES AND PARAMETERS
# ============================================

class myParrot:
    # CLASS ATTRIBUTE: Shared by all instances of the class
    species = 'bird'  # Same for all parrots
    
    # INSTANCE ATTRIBUTES: Unique to each object
    def __init__(self, name, age):
        print("myParrot class constructor is executing...")
        # Parameter vs Attribute explanation:
        # 'name' and 'age' are parameters (temporary input values)
        # self.name and self.age are instance attributes (permanent object data)
        self.name = name    # Creates instance attribute from parameter
        self.age = age      # Each object gets its own name and age
    
    def canSing(self, thisSong):
        # Method with parameter that uses instance attributes
        return f'{self.name} can sing {thisSong}'
        # FIXED: Original code had syntax error - missing 'f' before string

# ============================================
# INHERITANCE - CHILD CLASS FROM PARENT CLASS
# ============================================

# myPenguin inherits from myBird (IS-A relationship)
class myPenguin(myBird):
    def __init__(self):
        # SUPER() FUNCTION: Calls parent class constructor
        super().__init__()  # Executes myBird's __init__
        print("Penguin is ready")
        # This ensures proper initialization chain
    
    def whoisThis(self):
        # Child class can have its own unique methods
        print("I am penguin")
    
    def canRun(self):
        print("I can run faster")
    
    # Note: myPenguin inherits canSwim() from myBird automatically

# ============================================
# OBJECT INSTANTIATION AND USAGE
# ============================================

# Creating objects (instances) from class
mp1 = myParrot("MyParrot1", 10)  # Calls __init__ with parameters
mp2 = myParrot("MyParrot2", 15)

# ACCESSING CLASS ATTRIBUTES
# __class__ gives access to the class of an object
print(f"MP1 is a {mp1.__class__.species}")  # Accesses class attribute
print(f"MP2 is also a {mp2.__class__.species}")

# ACCESSING INSTANCE ATTRIBUTES
print(f"{mp1.name} is {mp1.age} years of age")  # Each object has unique values
print(f"{mp2.name} is {mp2.age} years of age")

# CALLING INSTANCE METHODS
print(mp1.canSing("Chirp"))  # Method call on specific object

# ============================================
# INHERITANCE IN ACTION
# ============================================

# Creating child class object
pg1 = myPenguin()  # Calls both myBird and myPenguin constructors
pg1.whoisThis()    # Child class method
pg1.canSwim()      # Inherited from parent class
pg1.canRun()       # Child class method

# =====================================
# DATA ENCAPSULATION (THEORY + EXAMPLE)
# =====================================
'''
DATA ENCAPSULATION:
- Encapsulation is one of the core principles of OOP.
- It means hiding the internal state (data) of an object and only allowing access through methods.
- This protects the data from being changed accidentally and helps keep your code organized and secure.
- In Python, we use single underscore _ (protected) or double underscore __ (private, name mangling) to 
indicate that a variable should not be accessed directly from outside the class.
- Instead, we provide public methods (getters/setters) to interact with the data.
- Encapsulation is the blueprint or concept—the idea of hiding data and controlling access in OOP.
Properties in Python are the practical tool (the “product”) that lets you implement encapsulation in real code.
REAL-LIFE EXAMPLE:
Think of a bank account:
- You can't just reach into the bank's database and change your balance!
- You must use deposit and withdraw methods, which check if the operation is valid.
- The actual balance is hidden (encapsulated) inside the object.
'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # __balance is private (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid or insufficient funds")

    def get_balance(self):
        return self.__balance

# Usage Example
acc = BankAccount("Priya", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Current balance:", acc.get_balance())
# print(acc.__balance)  # This will raise an AttributeError (encapsulation in action)

# Extra Encapsulation Tips and Best Practices:
# - You can use @property and @setter to provide controlled access to private variables (more Pythonic than just get/set methods).
# - Privacy in Python is by convention, not enforced. Use _var for internal use, __var for stronger privacy (name mangling).
# - Directly accessing private variables (like acc._BankAccount__balance) is possible but not recommended.
# - Encapsulation makes code easier to maintain, debug, and change without breaking other code.
# - In other languages (like Java/C++), privacy is enforced by the language. In Python, it's about trust and convention.
# - Always use the provided methods or properties to interact with private data.
# - Common interview questions: What is encapsulation? How do you achieve it in Python? Difference between _var and __var? Why use getters/setters?
# - Best practice: Hide data that should not be changed directly, and expose only what is necessary for the user of your class.

# Extra example of encapsulation using properties

class personalComputer:
    def __init__(self):
        # Instance attribute - each computer object has its own price
        self.maxComputerprice = 20000
    
    def mySell(self):
        # Method to display current price
        print(f"Selling Price: {self.maxComputerprice}")
    
    def setMaxComputerPrice(self, price):
        # SETTER METHOD: Controlled way to modify attributes
        # This is better than direct attribute access
        self.maxComputerprice = price

print()  # Empty line for output formatting

# Creating computer object
pc = personalComputer()
pc.mySell()  # Display initial price

# DIRECT ATTRIBUTE ACCESS (not recommended in production)
pc.maxComputerprice = 30000
pc.mySell()  # FIXED: Original code missing parentheses

# USING SETTER METHOD (recommended approach)
pc.setMaxComputerPrice(40000)
pc.mySell()

# ============================================
# IMPORTANT OOP CONCEPTS TO REMEMBER
# ============================================

'''
1. SELF PARAMETER:
   - First parameter in all instance methods
   - Refers to the specific object calling the method
   - Links method to particular instance of class
   - Without self, can't access object's attributes or methods

2. CONSTRUCTOR (__init__):
   - Special method that runs automatically during object creation
   - Initializes object's starting state
   - Can accept parameters to customize each object

3. CLASS vs INSTANCE ATTRIBUTES:
   - Class attributes: Shared by all objects of that class
   - Instance(Object) attributes: Unique to each individual object

4. INHERITANCE BENEFITS:
   - Code reusability
   - Establishes IS-A relationships
   - Child classes can extend parent functionality
   - super() ensures proper initialization chain

5. ENCAPSULATION PRINCIPLES:
   - Use methods to control attribute access
   - Setter/getter methods provide controlled access
   - Protects data integrity by hiding the private details of a class from other objects.

6. METHOD TYPES:
   - Instance methods: Work with specific object data
   - Class methods: Work with class-level data (@classmethod)
   - Static methods: Independent utility functions (@staticmethod)

7. SPECIAL METHODS (Dunder Methods):
   - __init__: Constructor
   - __str__: String representation
   - __repr__: Developer string representation
   - __len__: Length operation
   - __add__: Addition operation
   - __eq__: Equality comparison
   - Many others for operator overloading

BEST PRACTICES:
- Use meaningful class and method names
- Keep classes focused on single responsibility
- Use inheritance for IS-A relationships
- Prefer composition over inheritance when appropriate
- Use encapsulation to protect data integrity
- Document classes and methods clearly

COMMON PATTERNS:
- Factory pattern: Classes that create other objects
- Singleton pattern: Only one instance allowed
- Observer pattern: Objects notify others of changes
- Strategy pattern: Different algorithms for same task
'''

# ============================================
# ADDITIONAL IMPORTANT CONCEPTS
# ============================================

'''
OBJECT IDENTITY AND EQUALITY:
- id(object): Returns unique identifier
- is operator: Checks if same object
- == operator: Checks if equal values

ATTRIBUTE ACCESS:
- getattr(object, 'attribute'): Get attribute value
- setattr(object, 'attribute', value): Set attribute value
- hasattr(object, 'attribute'): Check if attribute exists
- delattr(object, 'attribute'): Delete attribute

METHOD RESOLUTION ORDER (MRO):
- Order in which methods are searched in inheritance
- Use ClassName.__mro__ to see the order
- Important for multiple inheritance scenarios

PROPERTY DECORATORS:
- @property: Makes method accessible like attribute
- @attribute.setter: Creates setter for property
- @attribute.deleter: Creates deleter for property

PRIVATE ATTRIBUTES (CONVENTION):
- _attribute: Protected (internal use)
- __attribute: Private (name mangling)
- These are conventions, not enforced by Python

POLYMORPHISM EXAMPLE:
- Same method name, different behavior in different classes
- Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"
- Method overriding: Child class redefines parent method

COMPOSITION vs INHERITANCE:
- Inheritance: IS-A relationship (Car is a Vehicle)
- Composition: HAS-A relationship (Car has an Engine)
- Composition often preferred for flexibility
'''

# ============================================
# MEMORY AND PERFORMANCE CONSIDERATIONS
# ============================================

'''
OBJECT CREATION COST:
- Each object has memory overhead
- __slots__ can reduce memory usage for simple classes
- Consider object pooling for frequently created/destroyed objects

GARBAGE COLLECTION:
- Python automatically manages memory
- Circular references can cause memory leaks
- Use weak references when appropriate

CLASS vs INSTANCE METHODS PERFORMANCE:
- Instance methods slightly slower due to self parameter
- Static methods fastest (no implicit parameters)
- Class methods moderate speed

INHERITANCE DEPTH:
- Deep inheritance chains slow method resolution
- Keep inheritance hierarchies shallow when possible
- Multiple inheritance adds complexity to MRO

'''
