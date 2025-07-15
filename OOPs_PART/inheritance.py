"""
=============================================================================
INHERITANCE IN OBJECT-ORIENTED PROGRAMMING
=============================================================================

DEFINITION:
Inheritance refers to defining a new class with little or no modification to an
existing class. The new class is called derived (or child) class and the
one from which it inherits is called the base (or parent) class.

TYPES OF INHERITANCE:

(a) SINGLE INHERITANCE
    - One child class inherits from one parent class
    - Simple linear relationship: A → B
    - Example: Animal → Dog
    
    class Animal:
        def eat(self):
            print("Animal eats")
    
    class Dog(Animal):  # Dog inherits from Animal
        def bark(self):
            print("Dog barks")

(b) MULTIPLE INHERITANCE
    - One child class inherits from multiple parent classes
    - Pattern: A, B → C (C inherits from both A and B)
    - Example: Flying + Swimming → Duck
    
    class Flying:
        def fly(self):
            print("Can fly")
    
    class Swimming:
        def swim(self):
            print("Can swim")
    
    class Duck(Flying, Swimming):  # Inherits from both
        def quack(self):
            print("Duck quacks")

(c) HIERARCHICAL INHERITANCE
    - Multiple child classes inherit from one parent class
    - Pattern: A → B, C, D (B, C, D all inherit from A)
    - Example: Vehicle → Car, Bike, Truck
    
    class Vehicle:
        def start(self):
            print("Vehicle starts")
    
    class Car(Vehicle):
        def drive(self):
            print("Car drives")
    
    class Bike(Vehicle):
        def ride(self):
            print("Bike rides")
    
    class Truck(Vehicle):
        def ride(self):
            print("Bike rides")

(d) MULTILEVEL INHERITANCE
    - Chain of inheritance through multiple levels
    - Pattern: A → B → C (C inherits from B, B inherits from A)
    - Example: Animal → Mammal → Dog
    
    class Animal:
        def breathe(self):
            print("Animal breathes")
    
    class Mammal(Animal):
        def feed_milk(self):
            print("Mammal feeds milk")
    
    class Dog(Mammal):
        def bark(self):
            print("Dog barks")

(e) HYBRID INHERITANCE
    - Combination of multiple inheritance types
    - Complex inheritance pattern combining above types
    - Pattern: Mix of hierarchical and multiple inheritance
    
    class A:
        pass
    
    class B(A):      # Single inheritance
        pass
    
    class C(A):      # Hierarchical inheritance
        pass
    
    class D(B, C):   # Multiple inheritance (Diamond problem)
        pass

KEY INHERITANCE CONCEPTS:

1. PARENT/BASE CLASS
   - Class being inherited from
   - Provides common attributes and methods
   - Also called superclass

2. CHILD/DERIVED CLASS
   - Class that inherits from parent
   - Gets all parent's attributes and methods
   - Can add its own unique features
   - Also called subclass

3. METHOD INHERITANCE
   - Child automatically gets parent's methods
   - Can use parent methods without redefining

4. METHOD OVERRIDING
   - Child can redefine parent's methods
   - Provides specialized behavior

5. SUPER() FUNCTION
   - Access parent class methods from child
   - Useful for extending rather than replacing

BENEFITS OF INHERITANCE:
- Code reusability (DRY principle or Don't Repeat Yourself Principle)
- Hierarchical organization
- Polymorphism support
- Easier maintenance
- Logical code structure

INHERITANCE SYNTAX:
class ParentClass:
    # Parent class definition
    pass

class ChildClass(ParentClass):
    # Child class inherits from ParentClass
    pass

# Multiple inheritance syntax:
class ChildClass(Parent1, Parent2):
    # Inherits from multiple parents
    pass
"""
# Creating Class and Object in Python
class myBird:

    def __init__(self):
        print("myBird class constructor is executing...")

    def whatType(self):
        print("I am a Bird")

    def canSwim(self):
        print("I can Swim")

# myPenguin class is inherting the attributes from the myBird class
class myPenguin(myBird):
    
    def __init__(self):
        # call super() function
        super().__init__() # General SYNTAX
        print("myPenguin class constructor is executing...")

    def whoisThis(self):
        print("I am Penguin...")

    def canRun(self):
        print("I can run faster...")

# Accessing the child class's attributes(Inheritance)
pg1 = myPenguin()
pg1.whatType()    # defined in myBird class
pg1.whoisThis()   # defined in myPenguin class
pg1.canSwim()     # defined in myBird class
pg1.canRun()      # defined in myPenguin class
print() # For newline

"""
=============================================================================
MULTIPLE INHERITANCE - CONCISE GUIDE
=============================================================================

DEFINITION:
A class can inherit from multiple parent classes simultaneously.
Child gets ALL features from ALL parents.

SYNTAX:
class Child(Parent1, Parent2, Parent3):
    pass

EXAMPLE:
class Flying:
    def fly(self): print("Can fly")

class Swimming:
    def swim(self): print("Can swim")

class Duck(Flying, Swimming):  # Inherits from both
    def quack(self): print("Quack!")

# Duck has fly(), swim(), and quack() methods

KEY CONCEPTS:

1. FEATURE INHERITANCE
   - Child gets methods/attributes from ALL parents
   - Can use any parent's functionality

2. DIAMOND PROBLEM & MRO (Method Resolution Order)
   - When multiple parents have same method name
   - Python uses MRO to decide which method to call
   - Check MRO: ClassName.__mro__
   - Left-to-right, depth-first resolution

3. SUPER() BEHAVIOR
   - In multiple inheritance, super() follows MRO
   - Calls next method in MRO chain, not necessarily direct parent

ADVANTAGES:
- Maximum code reuse
- Model complex real-world relationships
- Combine different capabilities

CHALLENGES:
- Diamond problem (method conflicts)
- Complex debugging
- Harder to understand

BEST PRACTICES:
- Keep hierarchies simple
- Understand your class MRO
- Use composition when inheritance gets complex
- Document complex relationships

REAL-WORLD EXAMPLE:
SmartPhone inherits from Phone + Computer + Camera + GPS
Result: Has calling, computing, photography, and navigation features
"""

# Multiple Inheritance

class Base1:
    def funcBase1(self):
        print("funcBase1() is executing...")

class Base2:
    def funcBase2(self):
        print("funcBase2() is executing...")

class Base3:
    def funcBase3(self):
        print("funcBase3() is executing...")

class MultiDerived(Base1, Base2, Base3):
    def funcMultiDerived(self):
        print("funcMultiDerived() is executing...")

md1 = MultiDerived()
md1.funcBase1()
md1.funcBase2()
md1.funcBase3()
md1.funcMultiDerived()

"""
=== ABSTRACT METHODS/FUNCTIONS CONCEPT REFERENCE ===

WHAT IS AN ABSTRACT METHOD?
- A method declared but not fully implemented in a parent class
- MUST be implemented by any class that inherits from it
- Acts like a contract: "If you inherit from me, you MUST implement this method"
- Ensures consistent interface across all subclasses

WHY USE ABSTRACT METHODS?
✅ Guarantees all subclasses have required methods
✅ Prevents incomplete class implementations
✅ Ensures consistent interface design
✅ Forces team members to implement essential methods
✅ Catches missing implementations at runtime

KEY RULE: "Base condition MUST be met, but enhancement is allowed"

=== BASIC EXAMPLE ===

from abc import ABC, abstractmethod

# Abstract class (blueprint/contract)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # MUST be implemented by subclasses
    
    @abstractmethod
    def move(self):
        pass  # MUST be implemented by subclasses

# Concrete classes (actual implementations)
class Dog(Animal):
    def make_sound(self):  # MANDATORY - meets base condition
        return "Woof!"     # Can enhance/modify as needed
    
    def move(self):        # MANDATORY - meets base condition
        return "Runs on four legs"

class Bird(Animal):
    def make_sound(self):  # MANDATORY - different implementation
        return "Chirp!"
    
    def move(self):        # MANDATORY - different implementation
        return "Flies with wings"

# Usage
dog = Dog()
print(dog.make_sound())  # Output: Woof!

# This would cause ERROR - cannot instantiate abstract class:
# animal = Animal()  # TypeError!

# This would cause ERROR - missing required methods:
# class BrokenAnimal(Animal):
#     pass  # Missing make_sound() and move() - Error when creating object!

=== ENHANCED IMPLEMENTATION EXAMPLE ===

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        return "Generic animal sound"  # Base implementation

class AdvancedDog(Animal):
    def make_sound(self):
        base = super().make_sound()    # Use base condition
        return f"{base} - specifically: WOOF!"  # Enhance it

=== KEY CONCEPTS ===

1. MANDATORY IMPLEMENTATION:
   - Cannot create objects of abstract class
   - Must implement ALL abstract methods in subclass
   - Missing implementation = Runtime error

2. ENHANCEMENT ALLOWED:
   - Can modify/improve the implementation
   - Can add extra functionality
   - Can call parent implementation with super()

3. INTERFACE CONSISTENCY:
   - All subclasses guaranteed to have same method names
   - Prevents "method not found" errors
   - Enables polymorphism (treating different objects the same way)

=== REAL-WORLD ANALOGY ===
Abstract Method = Job Requirements
- Job posting: "Must know Python" (abstract requirement)
- Candidate A: "I know basic Python" (meets requirement)
- Candidate B: "I know advanced Python + frameworks" (enhanced)
- Both candidates meet the base condition, but B enhanced it

SIMPLE RULE: 
"Abstract method = MUST implement + CAN enhance"
Base condition is mandatory, creativity in implementation is encouraged!
"""
