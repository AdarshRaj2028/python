'''
============================================
PYTHON GENERATORS - CONCISE REFERENCE
============================================

WHAT ARE GENERATORS?
- Functions that use 'yield' instead of 'return'
- Return iterator objects that produce values on-demand
- Memory-efficient alternative to creating entire lists
- Can pause execution and resume from where they left off

WHY USE GENERATORS?
- Memory efficient: Create one value at a time, not entire dataset
- Lazy evaluation: Values computed only when needed
- Automatic iterator protocol implementation
- Perfect for large datasets or infinite sequences
- We cannot use yield in a normal function that uses return in the usual way.

"""
Difference between return and yield:

- 'return' sends back a complete value (like a list) and ends the function immediately.
- 'yield' produces a sequence of values one at a time, pausing the function between each.
- Using 'yield' creates a generator, which is memory-efficient for large or infinite data.
- Use 'return' when you want to output a final result all at once.
- Use 'yield' when you want to generate values lazily, one by one, especially in loops.
"""
Generators are a quick, easy way to create iterators using functions and yield.
Iterators (custom classes) give you more control and flexibility, but require more code.

============================================
GENERATOR vs NORMAL FUNCTION
============================================

KEY DIFFERENCES:
- Normal: return exits function, Generator: yield pauses function
- Normal: Creates all data in memory, Generator: One value at a time
- Normal: Returns actual data, Generator: Returns generator object
- Normal: Can't resume, Generator: Resumes from last yield

============================================
HOW GENERATORS WORK
============================================

EXECUTION FLOW:
1. gen = my_generator()    # Returns generator object (doesn't run code)
2. next(gen)              # Executes until first yield
3. next(gen)              # Resumes from last yield
4. StopIteration raised   # When function ends

BASIC EXAMPLE:
def count_to_three():
    yield 1
    yield 2
    yield 3

counter = count_to_three()
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# next(counter) would raise StopIteration

============================================
GENERATOR EXPRESSIONS
============================================

GENERATOR EXPRESSION (like list comprehension but with parentheses):

squares = (x**2 for x in range(5))     # Generator expression
- A generator stores the "recipe" or "instructions" for how to create each element one by one, rather than storing the actual elements themselves like a list does.

squares_list = [x**2 for x in range(5)]  # List comprehension

Generator uses minimal memory, list stores all values meaning:
-> Generator: Creates values one at a time when requested (like a factory that makes one item only when you ask for it) - uses almost no memory upfront
-> List: Creates and stores ALL values in memory at once (like buying 1000 items and storing them in your house) - uses memory proportional to the number of items

============================================
WHEN TO USE GENERATORS
============================================

USE GENERATORS FOR:
- Large datasets (memory efficiency)
- Reading files line by line
- Infinite sequences
- Data processing pipelines
- When you don't need all values at once

AVOID GENERATORS FOR:
- Small datasets where memory isn't a concern
- When you need random access to elements
- When you need to iterate multiple times (generators consumed once)

MEMORY COMPARISON:
big_list = [i for i in range(1000000)]     # ~8MB memory
big_gen = (i for i in range(1000000))      # ~200 bytes memory

big_list: Python immediately creates all 1,000,000 numbers (0, 1, 2, 3... 999,999) and stores them in memory at once = 8MB used.

big_gen: Python only stores the "recipe" to make numbers (the generator object itself) but doesn't create any actual numbers yet = only 200 bytes used until you start asking for numbers one by one.

============================================
KEY POINTS FOR REVISION
============================================

ESSENTIAL CONCEPTS:
1. yield pauses function, preserves state
2. Generator objects are iterators (use next() or for loops)
3. One-time use: generators are consumed once
4. Memory efficient: lazy evaluation
5. Automatic StopIteration when function ends

COMMON USAGE PATTERNS:
for item in generator_function():  # Most common
next(generator_object)            # Manual iteration
list(generator_function())        # Convert to list
(expression for item in iterable) # Generator expression
'''
# A simple generator function
# f a function contains yield anywhere in its body, 
# it automatically becomes a generator function—no matter what you name it.

def my_generator():
    n = 1
    print("This is printed first")
    # Generator function contains yield statements
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed last")
    yield n

a = my_generator()
print("\nIterating using next\n")
print(next(a))
print(next(a))
print(next(a))

print("\nIterating using for loop\n")
for item in my_generator():
    print(item)

print() 

# Generators with a loop
def reverse_string(my_string):
    length = len(my_string)
    # Loop from the last index to the first (inclusive), stepping backwards by 1
    for i in range(length - 1, -1, -1):
        # If length = 5, condition(4, -1(n-1, which means upto 0 i.e last term), -1)
        yield my_string[i]

# For loop to reverse the string

for char in reverse_string("REDRUM"):
    print(char)

print()

# Generator comprehension

squares = (x**2 for x in range(5))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print()

sum_of_squares = sum(x**2 for x in range(100000))
print(sum_of_squares)