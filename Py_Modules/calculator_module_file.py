# calculator.py - This is your local module

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def get_info():
    """Get calculator info"""
    return "Simple Calculator Module v1.0"

# You can also store variables in modules
PI = 3.14159
VERSION = "1.0"
