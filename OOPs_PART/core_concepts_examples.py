"""
Python Core Concepts Explained with Real-life Examples

1. Python property
2. Data Encapsulation
3. Python closure
4. Operator Overloading
5. Virtual Environment (Explanation)
"""

# 1. Python property
class Student:
    def __init__(self, name, percentage):
        self.name = name
        self._percentage = percentage  # _percentage is a 'private' variable

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if 0 <= value <= 100:
            self._percentage = value
        else:
            raise ValueError("Percentage must be between 0 and 100")

# Usage Example
s = Student("Rahul", 85)
print(f"{s.name}'s percentage:", s.percentage)
s.percentage = 95
print(f"Updated percentage:", s.percentage)
# s.percentage = 120  # Uncommenting this will raise an error

# =====================================
# 2. DATA ENCAPSULATION (THEORY + EXAMPLE)
# =====================================
'''
DATA ENCAPSULATION:
- Encapsulation is one of the core principles of OOP.
- It means hiding the internal state (data) of an object and only allowing access through methods.
- This protects the data from being changed accidentally and helps keep your code organized and secure.
- In Python, we use single underscore _ (protected) or double underscore __ (private, name mangling) to indicate that a variable should not be accessed directly from outside the class.
- Instead, we provide public methods (getters/setters) to interact with the data.

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

# 3. Python closure

def outer_func(msg):
    def inner_func():
        print(f"Message: {msg}")
    return inner_func

# Usage Example
hi_func = outer_func("Hello World!")
hi_func()  # prints 'Message: Hello World!'

# 4. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Usage Example
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__
print("Sum of points:", p3)

# 5. Virtual Environment (Explanation)
print("\nVirtual Environment: A virtual environment is an isolated Python environment. It helps you manage dependencies for different projects separately.\nTo create one, use: python -m venv myenv\nTo activate on Windows: myenv\\Scripts\\activate\nTo deactivate: deactivate\n")
