# ===================================================================
# Python Tuples: A Comprehensive Revision Guide
# ===================================================================

# Core Properties of Tuples
# -------------------------
# 1. Immutable: Once created, you cannot change, add, or remove elements from a tuple.
# 2. Ordered: Tuples maintain the order of elements as they were defined.
# 3. Allow Duplicates: Unlike dictionary keys, tuples can contain duplicate values.
# 4. Indexed: You can access elements using their index position (starting from 0).
# 5. Performance: Iterating through tuples is faster than lists due to immutability.
# 6. Write-Protected: Tuples guarantee that data won't accidentally change.
# 7. Reassignable: While the tuple itself is immutable, you can assign a new tuple 
#    to the same variable name.


# ---------------------------------
# 1. Creating Tuples and Basic Operations
# ---------------------------------
print("--- 1. Inbuilt Functions with Tuples ---")

# Define a tuple - parentheses are optional but recommended for clarity
tup = (4, 3, 7, 1, 2)  # Immutable collection of elements
print("Original tuple:", tup)

# Built-in functions that work with tuples
print("Minimum value:", min(tup))        # Returns the smallest element
print("Maximum value:", max(tup))        # Returns the largest element
print("Sorted tuple:", sorted(tup))      # Returns a new sorted LIST (not tuple)

# Tuple-specific methods
tup1 = tup.index(4)    # Returns the index of the first occurrence of the element
print("Index of element 4:", tup1)

tup2 = tup.count(4)    # Counts how many times the element appears in the tuple
print("Count of element 4:", tup2)


# ---------------------------------
# 2. Tuple Unpacking
# ---------------------------------
print("\n--- 2. Unpacking of Tuple ---")

# Create a tuple with mixed data types
student = 1, "Adarsh", [98, 99, 92.5]  # Parentheses are optional

# Unpack the tuple into separate variables
division, name, marks = student  # Each variable gets one element from the tuple
print("Division:", division)
print("Name:", name)
print("Marks:", marks)

# Membership testing - checking if an element exists in the tuple
print("Is 'Adarsh' NOT in student tuple?", "Adarsh" not in student)  # False
print("Is 'Adarsh' in student tuple?", "Adarsh" in student)          # True


# ---------------------------------
# 3. Single Element Tuples and Deletion
# ---------------------------------
# To create a tuple with a single element, you MUST include a trailing comma
l = 10,  # Without the comma, this would be just an integer, not a tuple
print("Type of l:", type(l))  # <class 'tuple'>

# You can delete the entire tuple variable, but not individual elements (immutable)
del l  # Removes the variable 'l' from memory


# ---------------------------------
# 4. Nested Tuples
# ---------------------------------
print("\n--- 4. Nested Tuple ---")

# Tuples can contain other tuples, lists, or any data type
tuple1 = ("point", [1, 2, 3, 4], (5, 6, 7))

# Accessing elements in nested structures using multiple indices
print("5th character of first element:", tuple1[0][4])  # 't' from "point"
print("3rd element of the list:", tuple1[1][2])         # 3 from [1,2,3,4]
print("2nd element of nested tuple:", tuple1[2][1])     # 6 from (5,6,7)


# ---------------------------------
# 5. Iterating Through Tuples
# ---------------------------------
print("\n--- 5. Loop used to represent tuple ---")

tuple2 = ('A', 'd', 'a', 'r', 's', 'h')
print("Name -> ", end="")  # Print without newline

# Loop through each element in the tuple
for letters in tuple2:
    print("", letters, sep="_", end="")  # Print each letter with underscore separator

print()  # Add a newline at the end


# ---------------------------------
# 6. Additional Tuple Operations
# ---------------------------------
print("\n--- 6. Additional Operations ---")

# Tuple concatenation (creates a new tuple)
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
combined = tuple_a + tuple_b
print("Combined tuple:", combined)

# Tuple repetition
repeated = tuple_a * 3
print("Repeated tuple:", repeated)

# Length of tuple
print("Length of tuple2:", len(tuple2))

# Converting between tuple and list
original_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(original_list)  # List to tuple
print("List to tuple:", converted_tuple)

converted_list = list(converted_tuple)  # Tuple to list
print("Tuple to list:", converted_list)


# ---------------------------------
# 7. When to Use Tuples vs Lists
# ---------------------------------
# Use tuples when:
# - Data should not change (coordinates, RGB values, database records)
# - You need a slight performance boost for iteration
# - You want to use the collection as a dictionary key (tuples are hashable)
# - You need to return multiple values from a function
#
# Use lists when:
# - You need to modify the data (add, remove, or change elements)
# - The size of the collection may change during program execution
