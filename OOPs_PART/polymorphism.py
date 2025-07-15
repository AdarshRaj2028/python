"""
=============================================================================
POLYMORPHISM IN OBJECT-ORIENTED PROGRAMMING
=============================================================================

DEFINITION:
Polymorphism is one of the core concepts of OOP that describes situations in 
which something occurs in several different forms. The word "polymorphism" 
comes from Greek: "poly" means many, and "morphism" means forms.
It allows objects of different types to be accessed through the same interface,
with each type providing its own independent implementation.

KEY CONCEPT:
"One interface, multiple implementations" - You can use the same method name
to perform different operations depending on the object type.

TYPES OF POLYMORPHISM:

(a) COMPILE-TIME POLYMORPHISM (Static Polymorphism)
    - Resolved during compilation
    - Also known as Method Overloading or Operator Overloading
    - Same method name with different parameters
    
    Example - Method Overloading:
    class Calculator:
        def add(self, a, b):           # Two parameters
            return a + b
        
        def add(self, a, b, c):        # Three parameters  
            return a + b + c
        
        def add(self, a, b, c, d):     # Four parameters
            return a + b + c + d

(b) RUNTIME POLYMORPHISM (Dynamic Polymorphism)
    - Resolved during program execution
    - Also known as Method Overriding
    - Child class provides specific implementation of parent method
    
    Example - Method Overriding:
    class Animal:
        def make_sound(self):
            print("Animal makes a sound")
    
    class Dog(Animal):
        def make_sound(self):          # Override parent method
            print("Dog barks")
    
    class Cat(Animal):
        def make_sound(self):          # Override parent method
            print("Cat meows")

MAIN TYPES OF POLYMORPHISM IN DETAIL:

1. AD HOC POLYMORPHISM
   - Function/Method Overloading
   - Operator Overloading
   - Defines common interface for individually specified types

2. PARAMETRIC POLYMORPHISM
   - Generic functions that work with multiple types
   - Uses abstract symbols instead of concrete types
   - Example: Generic collections, templates

3. SUBTYPE POLYMORPHISM (Most Common)
   - Objects of derived class treated as objects of base class
   - Uses inheritance relationship
   - Runtime method resolution

POLYMORPHISM IMPLEMENTATION EXAMPLES:

# Runtime Polymorphism Example
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):                    # Override parent method
        return self.length * self.width
    
    def perimeter(self):               # Override parent method
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):                    # Override parent method
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):               # Override parent method
        return 2 * 3.14159 * self.radius

# Polymorphic behavior
shapes = [Rectangle(5, 3), Circle(4), Rectangle(2, 8)]
for shape in shapes:
    print(f"Area: {shape.area()}")    # Same method, different behavior

KEY POLYMORPHISM CONCEPTS:

1. VIRTUAL METHODS
   - Methods that can be overridden in derived classes
   - Enable runtime method resolution

2. DYNAMIC BINDING
   - Decision of which method to call made at runtime
   - Based on actual object type, not declared type

3. METHOD OVERRIDING
   - Child class replaces parent class method implementation
   - Same method signature, different behavior

4. METHOD OVERLOADING
   - Multiple methods with same name but different parameters
   - Resolved at compile time

5. INTERFACE POLYMORPHISM
   - Multiple classes implement same interface
   - Same method names, different implementations

BENEFITS OF POLYMORPHISM:

1. FLEXIBILITY
   - Code can work with objects of different classes
   - Easy to modify and extend existing code

2. REUSABILITY
   - Write generic interfaces implemented by multiple classes
   - Reduces code duplication

3. MODULARITY
   - Separate concerns by treating objects as common superclass
   - Promotes modular design

4. EXTENSIBILITY
   - Easy to add new classes without modifying existing code
   - New functionality without breaking existing code

5. CODE READABILITY
   - Cleaner, more concise code
   - Easier to understand and debug

6. MAINTAINABILITY
   - Reduces complexity
   - Improves code organization

POLYMORPHISM APPLICATIONS:

1. INHERITANCE HIERARCHIES
   - Base class defines interface(Common structure or Common method), derived classes implement

2. INTERFACE DESIGN
   - Define contracts that multiple classes can implement
   - Contract here refers to a set of methods or behavious that a class must implement
   - It's like a promise that any class implementing this interface will have certain methods
   - Although the actual implementation can vary across different classes, but each class will respect that contract by providing those methods

3. DEPENDENCY INJECTION
   - Pass objects through interfaces rather than concrete types
   - In simple terms, We don't depend on a concrete class like "Rectangle" or "Circle"
   - A concrete class is a class with actual implementations of methods. For example, a “Rectangle” class has specific code to calculate the area of a rectangle. 
   - That is concrete because its fully defined.
   - Now, if we rely on that specific class (“Rectangle”), our code becomes tightly coupled to it. 
   - That means if we want to change to another shape, like a circle, we would have to rewrite the code.
   - Instead we rely on the higher-level interfaces, like "Shapes" which defines a general contract(like area method) but doesn't define how it's done 

4. COLLECTIONS OF MIXED TYPES
   - Store different object types in same collection
   - Process them uniformly

5. PLUGIN ARCHITECTURES
   - Different plugins implement same interface
   - System works with any plugin

POLYMORPHISM TEST:
An object is polymorphic if it passes multiple "isinstance" or "is-a" tests.
We can use isinstance() function to check if it belongs to a particular class.
All objects in Python are polymorphic because they inherit from base Object.

REAL-WORLD ANALOGY:
Think of a remote control (interface) that can operate different devices
(TV, AC, Music System). Same buttons, different behaviors depending on device.

POLYMORPHISM vs OTHER OOP CONCEPTS:
- Inheritance: "IS-A" relationship (Dog IS-A Animal)
- Polymorphism: "BEHAVES-AS" relationship (Dog BEHAVES-AS Animal but differently)
- Encapsulation: Data hiding and bundling
- Abstraction: Hiding implementation complexity

IMPORTANT NOTES:
- Polymorphism is the 3rd pillar of OOP (after Encapsulation and Inheritance)
- Enables writing flexible, maintainable, and extensible code
- Essential for design patterns and frameworks
- Promotes loose coupling between classes
"""

# Example

class myParrot:         # CLASS (blueprint)
    
    def canFly(self):   # METHOD (action/function)
        print("Parrot can fly...")

    def canSwim(self):
        print("Parrot can't swim...")

class myPenguin:

    def canFly(self):
        print("Penguin can't fly...")

    def canSwim(self):
        print("Penguin can swim...")

# Common interface
def flying_bird_test(bird):
    bird.canFly()
    bird.canSwim()

# Instantiate objects
bird_parrot = myParrot()
bird_penguin = myPenguin()

# Passing the object

flying_bird_test(bird_parrot)
print()
flying_bird_test(bird_penguin)