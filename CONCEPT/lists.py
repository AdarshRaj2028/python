# ===================================================================
# Python Lists: A Comprehensive Revision Guide
# ===================================================================

# Core Properties of Lists
# ------------------------
# 1. Built-in Data Type: Lists are a fundamental data structure in Python for storing
#    collections of values.
# 2. Mutable: You can change, add, or remove elements after the list is created.
# 3. Ordered: Lists maintain the order of elements as they were defined.
# 4. Allow Duplicates: Lists can contain the same value multiple times.
# 5. Mixed Data Types: Unlike arrays in some languages, Python lists can store
#    multiple data types in the same list.
# 6. Indexed: Elements can be accessed using their position (starting from 0).

# Note: Arrays are linear data structures storing fixed-size elements of same type
# in contiguous memory, but Python lists are more flexible than traditional arrays.

# ---------------------------------
# 1. Creating Lists and Basic Access
# ---------------------------------
print("--- 1. Basic List Operations ---")

# Create a list with mixed data types
student = ["Adarsh", 8.57, 19, "Patna"]  # Index ranges from 0 to n-1
print("Original list:", student)

# Access individual elements using index
print("First element (index 0):", student[0])   # "Adarsh"
print("Last element (index 3):", student[3])    # "Patna"

# Modify an element (lists are mutable)
student[2] = 20  # Change age from 19 to 20
print("After modification:", student)


# ---------------------------------
# 2. List Slicing
# ---------------------------------
print("\n--- 2. List Slicing ---")
# List slicing works exactly like string slicing: list[start:end]
# The start index is included, the end index is excluded

print("Elements from index 1 to 3:", student[1:4])  # [8.57, 20, "Patna"]
print("Elements from index 2 to 3:", student[2:4])  # [20, "Patna"]

# Note: List slicing follows the same rules as string slicing
# Refer to string slicing concepts for more advanced slicing techniques


# ---------------------------------
# 3. Nested Lists (2D Lists)
# ---------------------------------
print("\n--- 3. Nested Lists ---")

# Create a list containing other lists (2D structure)
num2 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
print("2D list:", num2)

# Access elements in nested lists using double indexing
print("num2[2][1]:", num2[2][1])  # First [2] gets [5,6], then [1] gets 6
print("num2[2][0]:", num2[2][0])  # First [2] gets [5,6], then [0] gets 5


# ---------------------------------
# 4. List Methods - Mutability Concept
# ---------------------------------
# IMPORTANT CONCEPT:
# Lists are mutable → Methods change the original object → Most return None
# Strings are immutable → Methods return new objects → Original stays unchanged
#
# Most list methods are designed to modify the list in-place.
# The pop() method is an exception because it serves dual purposes:
# 1. Remove an element (modification)
# 2. Return the removed value (data retrieval)
#
# Methods like append(), insert(), sort(), remove() don't return values
# because they are purely for modification, not data retrieval.

print("\n--- 4. List Methods ---")

# Initialize lists for demonstration
num = [10, 40, 20, 50, 30]
words = ["apple", "apple", "appel"]  # Fixed typo: "applie" → "apple"

print("Original num list:", num)
print("Original words list:", words)


# ---------------------------------
# 5. Sorting Methods
# ---------------------------------
print("\n--- 5. Sorting Operations ---")

# Sort strings alphabetically (modifies original list)
words.sort()
print("Words after sorting:", words)

# Sort numbers in ascending order (modifies original list)
num.sort()
print("Numbers after ascending sort:", num)

# Sort in descending order using reverse parameter
num.sort(reverse=True)
print("Numbers after descending sort:", num)

# Reverse the current order of elements (not sorting, just reversing)
num.reverse()
print("Numbers after reverse():", num)


# ---------------------------------
# 6. Adding Elements
# ---------------------------------
print("\n--- 6. Adding Elements ---")

# Add single element at the end of the list
num.append(20)
print("After append(20):", num)

# Insert element at specific index: list.insert(index, element)
num.insert(4, 30)  # Insert 30 at index 4
print("After insert(4, 30):", num)


# ---------------------------------
# 7. Removing Elements
# ---------------------------------
print("\n--- 7. Removing Elements ---")

# Remove first occurrence of specified element
num.remove(20)  # Removes the first occurrence of 20
print("After remove(20):", num)

# Remove and return element at specific index
removed_element = num.pop(3)  # Remove element at index 3 and return it
print("Element removed by pop(3):", removed_element)
print("List after pop(3):", num)

# Additional removal methods:
# num.pop()        # Removes and returns the last element
# num.clear()      # Removes all elements from the list
# del num[index]   # Removes element at specific index (doesn't return it)


# ---------------------------------
# 8. Other Useful List Methods
# ---------------------------------
print("\n--- 8. Additional List Methods ---")

sample_list = [1, 2, 3, 2, 4, 2, 5]
print("Sample list:", sample_list)

# Count occurrences of an element
count_of_2 = sample_list.count(2)
print("Count of element 2:", count_of_2)

# Find index of first occurrence
index_of_4 = sample_list.index(4)
print("Index of element 4:", index_of_4)

# Extend list with another iterable
sample_list.extend([6, 7, 8])  # Adds multiple elements
print("After extend([6, 7, 8]):", sample_list)

# Create a copy of the list
list_copy = sample_list.copy()
print("Copied list:", list_copy)

# Get length of list
print("Length of sample_list:", len(sample_list))


# ---------------------------------
# 9. List Comprehensions (Bonus)
# ---------------------------------

# List comprehensions are a concise way to create lists by applying an expression to each element in an iterable. 
# They are often used because they make code more readable and efficient compared to traditional loop.
# They reduce the amount of code you have to write while accomplishing the same task.  

print("\n--- 9. List Comprehensions ---")

# Create a list of squares using comprehension
squares = [x**2 for x in range(1, 6)]
print("\nSquares using comprehension:", squares)

# If with list comprehension
number_list = [ x for x in range(20) if x % 2 == 0]
print("\n",number_list)

# Nested If with list comprehension
num_list = [ y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print("\n",num_list)

# If...Else with list comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print("\n", obj ,"\n")

# Filter even numbers using comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print("\nEven numbers:", even_numbers, "\n")

"""
=============================================================================
SHALLOW COPY vs DEEP COPY IN PYTHON
=============================================================================

DEFINITION:
Copying refers to creating a new object with the same values as the original.
However, the behavior differs based on whether objects contain references to 
other objects (like nested lists, dictionaries, etc.).

SHALLOW COPY:
- Creates a new object, but references to nested objects are shared
- Changes to nested objects affect both original and copy
- Only the outermost container is duplicated
- Inner objects are referenced, not duplicated

DEEP COPY:
- Creates completely independent copy including all nested objects
- Changes to nested objects don't affect the original
- Recursively copies all nested objects
- Completely separate memory locations

COPY METHODS:
1. copy.copy(obj)        # Shallow copy
2. copy.deepcopy(obj)    # Deep copy
3. list.copy()           # Shallow copy for lists
4. obj[:]                # Shallow copy using slicing

MEMORY REPRESENTATION:
Shallow Copy:
Original:     [1, 2, [3, 4]] ──┐
                         ↓     │ (shares reference)
Shallow Copy: [1, 2, [3, 4]] ──┘

Deep Copy:
Original:     [1, 2, [3, 4]]
                         ↓
Deep Copy:    [1, 2, [3, 4]]  (completely separate)

BEHAVIOR DIFFERENCES:
- Shallow: Modifying nested objects affects both copies
- Deep: Modifying nested objects affects only that copy
- Shallow: Faster and uses less memory
- Deep: Slower but provides complete independence

WHEN TO USE:
Shallow Copy:
- When you need a new container but can share nested objects
- Performance is critical
- Nested objects won't be modified

Deep Copy:
- When you need complete independence
- Nested objects will be modified
- Safety is more important than performance

IMPORTANT NOTES:
- For immutable objects (int, string, tuple), shallow copy behaves like deep copy
- For mutable nested objects (lists, dicts), the difference is significant
- Deep copy can be expensive for large, complex data structures
- Some objects cannot be deep copied (file objects, database connections)
"""

import copy 

# Original list with an inner list 
A = [1, 2, [3, 4]] 

# Shallow copy - creates new outer list but shares inner list reference
shallow_copy = copy.copy(A)

# Deep Copy - creates completely independent copy including inner list
deep_copy = copy.deepcopy(A)

# Change the inner list in the original
A[2][0] = 99  # Modifies the nested list

print("Original:", A)           # [1, 2, [99, 4]] - changed
print("Shallow Copy:", shallow_copy)  # [1, 2, [99, 4]] - also changed!
print("Deep Copy:", deep_copy)        # [1, 2, [3, 4]]  - unchanged

"""
OUTPUT EXPLANATION:
- Original: [1, 2, [99, 4]] - We modified this directly
- Shallow Copy: [1, 2, [99, 4]] - Inner list changed because it shares reference
- Deep Copy: [1, 2, [3, 4]] - Unchanged because it has its own inner list

This demonstrates that shallow copy shares references to nested objects,
while deep copy creates completely independent nested objects.
"""

# 10. The zip() Function and zip vs enumerate (Bonus)
# ---------------------------------------------------

# CONCEPT: zip()
# ---------------
# The zip() function combines two or more iterables (like lists or tuples) element-wise into tuples.
# It returns an iterator of tuples, where the i-th tuple contains the i-th element from each iterable.
# The resulting iterator stops when the shortest input iterable is exhausted.

print("\n--- 10. The zip() Function ---")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
subjects = ["Math", "Science", "English"]

# Combine lists using zip
student_records = list(zip(names, scores, subjects))
print("Student records using zip:", student_records)
# Output: [('Alice', 85, 'Math'), ('Bob', 92, 'Science'), ('Charlie', 78, 'English')]

# You can use zip in a loop to process multiple lists together
for name, score, subject in zip(names, scores, subjects):
    print(f"Name: {name}, Score: {score}, Subject: {subject}")

# CONCEPT: enumerate()
# --------------------
# The enumerate() function adds a counter (index) to an iterable and returns it as an enumerate object.
# Useful for getting both the index and the value when looping through a list.

print("\n--- 11. The enumerate() Function ---")

students = ["Alice", "Bob", "Charlie"]
for idx, student in enumerate(students, 1):  # Start counting from 1
    print(f"Student {idx}: {student}")

# zip() vs enumerate()
# --------------------
# - zip() is used to iterate over multiple iterables in parallel, pairing their elements.
# - enumerate() is used to get the index and value from a single iterable.

# Example showing the difference:
print("\n--- zip() vs enumerate() Example ---")

colors = ["red", "green", "blue"]
fruits = ["apple", "pear", "berry"]

print("Using zip:")
for color, fruit in zip(colors, fruits):
    print(f"{color} - {fruit}")

print("\nUsing enumerate:")
for idx, color in enumerate(colors):
    print(f"Index {idx}: {color}")

"""
=============================================================================
zip() vs enumerate() - Quick Reference
=============================================================================

zip():
- Combines multiple iterables element-wise into tuples
- Stops at the shortest iterable
- Example: zip([1,2,3], ['a','b','c']) → (1, 'a'), (2, 'b'), (3, 'c')

enumerate():
- Adds an index to each element of a single iterable
- Useful for getting both index and value
- Example: enumerate(['a','b','c']) → (0, 'a'), (1, 'b'), (2, 'c')

When to use:
- Use zip() when you want to process multiple lists together, element by element
- Use enumerate() when you need the index and value from a single list

=============================================================================
"""
