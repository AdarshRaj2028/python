# Number Data Types:

# Python supports three number data types
# integer numbers (e.g. 100, 2030 etc.) floating point numbers (e.g. 12.34, 56,39 etc.) complex numbers (e.g. 3 + 4j, 5+ 10j)
# We can use the type() function to know which class a variable or a value belongs to and isinstance() function to check if it belongs to a particular class.
# While integers can be of any length, a floating point number is accurate only up to 15 decimal places (the 16th place is inaccurate).
# Numbers we deal with everyday are decimal (base 10) number system. Python can also express Binary, Octal and Hexa-Decimal numbers.
# As computer programmers (generally embedded programmer) need to work with binary (base 2), hexadecimal (base 16) and octal (base 8) number systems
# In Python, we can represent these numbers by appropriately placing a prefix before that number:

#-> 0b or 0B as Binary number prefix
#-> 0o or 0O as Octal number prefix
#-> 0x or 0X as Hexadecimal number prefix

# Number Type Conversion:

# We can also use built-in functions like - int(), float() and complex().
# To convert between types explicitly. These function can even convert from strings.

type_1, type_2, type_3 = 100, 100.29, 10 + 10j

print(type(type_1))
print(isinstance(type_1, int)) # isinstance() function checks if it belongs to a particular class or not.
print(type(type_2))
print(isinstance(type_2, float))
print(type(type_3))
print(isinstance(type_3, complex))

seven = "7"
print("\nType of seven before explicit conversion: ", type(seven))
print("Type of seven after explicit conversion: ", type(int(seven)))
print() # For new line

print(0b1101)
print(0xab)
print(0o23,"\n")

# Python Decimal

# However python 3.8+ has more accuracy in floating points, but still there are precision problems.
# But The fundamental issue is that floats give approximations while Decimals give exact representations.
# For any condition checking where precision matters, Decimal eliminates the unpredictable behavior that makes float comparisons unreliable. 
 
num_1 = 0.1
num_2 = 0.2
num_3 = 0.3
if(num_1 + num_2 == num_3): # This will print false due to floating value precision
    print(True) 
else: 
    print(False)

from decimal import Decimal as D

num_1,num_2,num_3 = D('0.1'),D('0.2'),D("0.3") # Remember, D(0.1) will be perceived as floating num, we need to write like this D("0.1") or D('0.1)
if(num_1 + num_2 == num_3): # This will print true due to floating value precision
    print(True) 
else: 
    print(False)

# Python Fraction

from fractions import Fraction as F
# used to convert the float or int into fractional num.
# Python's Fraction class from the fractions module represents rational numbers (fractions) exactly without floating-point precision errors,
# making it ideal for precise mathematical calculations
print(F('5.5'))
print(type(F('1.0')))
print(F(4,16)) # Here we don't need quotes
print()
# Python math module

import math
print (math.pi)
print (math.cos(10))
print (math.log(10))
print (math.log10(10))
print (math.exp(10))
print (math.factorial(5))
print (math.sinh(10))
print(abs(-12.54))

# Python random module

import random

print('Random number -> ', random.randrange(5,15))
print('Random number -> ', random.randrange(5,15))

day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
print(random.choice(day))

print (day)
random.shuffle(day)
print (day)

# Print random element 
print(random.random())
