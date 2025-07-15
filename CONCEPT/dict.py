'''
===================================================================
Python Dictionaries: A Comprehensive Revision Guide
===================================================================

Core Properties of Dictionaries
-------------------------------
1. Key-Value Pairs: Dictionaries store data in `key:value` pairs. They are
   highly optimized for retrieving a value when its key is known.

2. Mutable: You can change, add, or remove items after the dictionary is created.

3. No Duplicate Keys: Keys must be unique. If you use the same key more than
   once, the last assignment will overwrite the previous value.

4. Ordered (Python 3.7+): Dictionaries remember the order in which items were
   inserted. In Python versions before 3.7, they were considered unordered.
'''

# ---------------------------------
# 1. Creating a Dictionary
# ---------------------------------
# Dictionaries are defined with curly braces {}.
# Keys must be an immutable type (like string, number, or tuple).
# Values can be any data type, including lists, tuples, or other dictionaries,
# Can be any Python object, whether mutable or immutable

info = {
    "name": "Adarsh",                  # Key: "name", Value: "Adarsh"
    "cgpa": "8.57",
    "score": {                         # The value can be another dictionary (nested)
        "chem": 98,
        "math": 99,
        "phy": 95
    },
    "branch": "IT",
    "subject": ["Maths", "Python", "DSA"], # The value can also be a list or tuple.
    12: 12.99                          # A key can be an integer or float.
}

print("--- 1. Initial Dictionary ---")
print(info)


# ---------------------------------
# 2. Accessing Values
# ---------------------------------
# There are two main ways to get the value associated with a key.
# Method A: Square Brackets `[]`
# This is the direct way. It will raise a `KeyError` if the key does not exist.

print("\n--- 2a. Accessing with Square Brackets [] ---")
print('info["score"]:', info["score"])
print('Nested value info["score"]["math"]:', info["score"]["math"])

# The line below would cause a KeyError because the key "age" does not exist.
# print(info["age"])

# Method B: .get() Method
# This is a safer way. It returns `None` if the key is not found, avoiding an error.
# You can also provide a default value to be returned instead of None.

print("\n--- 2b. Accessing with .get() ---")
print('info.get("branch"):', info.get("branch"))
print('info.get("age"):', info.get("age"))  # Key "age" doesn't exist, so it returns None.
print('info.get("age", "Not Available"):', info.get("age", "Not Available")) # Provides a default value.


# ---------------------------------
# 3. Adding and Updating Items
# ---------------------------------
# You can add a new item or update an existing one using assignment.
info["is_adult"] = True  # Adds a new key-value pair
info["cgpa"] = "8.6"     # Updates the value for the existing key "cgpa"

# To add or update multiple items at once, use the .update() method.
# You can pass another dictionary to it.
info.update({"City": "Kolkata", "branch": "Information Technology"})

print("\n--- 3. After Adding and Updating Items ---")
print(info)


# ---------------------------------
# 4. Removing Items
# ---------------------------------
# Use .pop(key) to remove an item by its key. It also returns the removed value.
popped_value = info.pop(12)
print(f"\n--- 4a. After popping key 12 (Popped Value: {popped_value}) ---")
print(info)

# Use .popitem() to remove the last inserted item (LIFO: Last-In, First-Out).
# It returns the removed (key, value) pair as a tuple.
# NOTE: In Python versions before 3.7, it removed an arbitrary item.
last_item = info.popitem()
print(f"\n--- 4b. After .popitem() (Popped Item: {last_item}) ---")
print(info)


# ---------------------------------
# 5. Viewing Keys, Values, and Items
# ---------------------------------
# These methods return "view" objects, which are dynamic and reflect dictionary changes.
print("\n--- 5. Dictionary Views ---")
print("All Keys:", info.keys())
print("All Values:", info.values())
print("All (Key, Value) Pairs:", info.items())

# To get a simple list, you can convert the view objects.
pairs_list = list(info.items())
print("\nItems as a list of tuples:", pairs_list)
print("First pair from the list:", pairs_list[0])


# ---------------------------------
# 6. Iterating Through a Dictionary
# ---------------------------------
# The best practice for looping through a dictionary is to use the .items() method,
# which gives you both the key and the value in each iteration.
print("\n--- 6a. Iterating with .items() (Best Practice) ---")
for key, value in info.items():
    print(f"Key: {key} -> Value: {value}")

print("\n--- 6b. Iterating through a nested dictionary ---")
people = {
    1 : {"name" : "Adarsh",
         "age" : 19,
         "sex" : 'M'
         },
    2 : {"name" : "Deepak",
         "age" : 19,
         "sex" : 'M'
         },
}

print(people.items())

for p_id, p_info in people.items():  # p_id = key and p_info = value
    print("\nPeople ID:", p_id)

    for key in p_info:
        print(f"{key} : {p_info[key]}")

# ---------------------------------
# 7. Dictionary Comprehension
# ---------------------------------
# A concise and powerful way to create new dictionaries.

# Example: Create a dictionary of squares from 0 to 5.
# Here, we also merge it with a pre-existing pair {2: 23}(If needed or else we only have to write the comprehension part).
# The `**` operator unpacks the generated dictionary into the new one.
# Since a key must be unique, the value for key `2` from the comprehension (which is 4)
# will overwrite the initial value of 23.
# The double asterisk (**) is also an unpacking operator, like *, 
# but it works specifically with dictionaries and keyword arguments

squares = {2: 23, **{x: x * x for x in range(6)}}
print("\n--- 7. Dictionary from Comprehension ---")
print(squares)


# ---------------------------------
# 8. Checking for Keys with 'in'
# ---------------------------------
# The `in` operator is a fast way to check if a KEY exists in a dictionary.
# IMPORTANT: This membership test is only for keys, not values.
print("\n--- 8. Checking for Keys with 'in' ---")
print("Is key `4` in squares?", 4 in squares)          # True, because 4 is a key.
print("Is key `16` in squares?", 16 in squares)        # False, 16 is a value, not a key.
print("Is key `49` in squares?", 49 in squares)        # False, 49 is not a key.
print()

# ---------------------------------
# 9. Merging two dictionaries
# ---------------------------------
# This creates a new dictionary that combines all key value pairs from both dictionaries.
# If there are duplicate keys, the value from the second dictionary will overwrite the first.

dict1 = {
    "name" : "lalu",
    "age" : 12,
}

dict2 = {
    "gender" : "male",
    "D.O.B" : "15th August 2000",
}

dict3 = {**dict1, **dict2}

print(dict3.items())