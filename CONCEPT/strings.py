# ===================================================================
# Python Strings: A Comprehensive Revision Guide
# ===================================================================

# Core Properties of Strings
# --------------------------
# 1. Data Type: Strings store sequences of characters (alphabets, digits, special chars).
# 2. Internal Representation: Computers convert characters to binary numbers (0s and 1s).
# 3. Encoding/Decoding: Character-to-number conversion is encoding; reverse is decoding.
# 4. Popular Encodings: ASCII and Unicode are commonly used encoding standards.
# 5. Immutable: Once created, strings cannot be changed (any "modification" creates new string).
# 6. Indexed: Each character can be accessed using its position (starting from 0).

# Note: Arrays are linear data structures storing fixed-size elements of same type
# in contiguous memory, but Python lists are more flexible than traditional arrays.


# ---------------------------------
# 1. String Creation and Concatenation
# ---------------------------------
print("--- 1. String Creation and Concatenation ---")

# Different ways to create strings
str1 = "Hello"
str2 = ' '
str3 = """World"""  # Triple quotes allow multi-line strings
str4 = """Hey there,
My name is Adarsh Raj.
I love Python."""
str5 = "Hey there,\
 What's up?"  # prints Hey there, What's up?

# String concatenation using + operator
print("Concatenated string:", str1 + str2 + str3)
print("Multi-line string:")
print(str4)

# String formatting - inserting variables into strings dynamically
name = "Adarsh"
print("\nOld way (harder to read):", "Hello " + name + ", welcome!")
print("Modern way (f-strings):", f"Hello {name}, welcome!")  # Python 3.6+ feature


# ---------------------------------
# 2. String Length and Basic Operations
# ---------------------------------
print("\n--- 2. String Length ---")
print("Length of str1:", len(str1))  # Returns number of characters


# ---------------------------------
# 3. Indexing vs Slicing Concepts
# ---------------------------------
# ──────────────── Indexing vs Slicing in Python ────────────────
# 
# INDEXING:
# - Used to access a single character
# - Index starts from 0 to n-1 (where n is string length)
# - Works the same for strings, lists, tuples, etc.
# Example: s = "Adarsh" → s[0] = 'A', s[5] = 'h'
#
# SLICING:
# - Returns a substring (slice) of the original string
# - Syntax: string[start : end : step]
# - start → inclusive (character at this index IS included)
# - end → exclusive (character at this index is NOT included)
# - Think: "from start up to but not including end"
# - Slicing never returns index ≥ n; end = n is allowed but stops at n-1
# - "Indices" is plural of "index"

# ---------------------------------
# Step Parameter in String Slicing
# ---------------------------------
# Syntax: string[start : end : step]
# 
# The STEP parameter controls how many characters to skip between each character
# that gets included in the slice.
#
# How Step Works:
# - Default step = 1: Takes every character (no skipping)
# - step = 2: Takes every 2nd character (skips 1 character between each)
# - step = 3: Takes every 3rd character (skips 2 characters between each)
# - Negative step: Reverses the direction of slicing
#
# Examples:
# text = "ABCDEFGH"
#
# text[0:6]     → "ABCDEF"  (step=1 default, every character from 0 to 5)
# text[0:6:2]   → "ACE"     (every 2nd character: A, skip B, C, skip D, E)
# text[0:8:3]   → "ADG"     (every 3rd character: A, skip BC, D, skip EF, G)
# text[::-1]    → "HGFEDCBA" (entire string reversed using negative step)
# text[6:2:-1]  → "GFED"    (from index 6 to 3, going backwards)
# text[1:7:2]   → "BDF"     (from index 1 to 6, every 2nd character)
#
# Common Use Cases:
# text[::-1]    → Reverse entire string
# text[::2]     → Get every other character
# text[1::2]    → Get every other character starting from index 1
# text[2:8:3]   → Get every 3rd character from index 2 to 7


print("\n--- 3. String Slicing Examples ---")
str_demo = "Adarsh"
print("Original string:", str_demo)

# Basic slicing examples
print("str_demo[0:6]:", str_demo[0:6])  # Full string (indices 0,1,2,3,4,5)
print("str_demo[:4]:", str_demo[:4])    # Same as str_demo[0:4] → "Adar"
print("str_demo[2:]:", str_demo[2:])    # Same as str_demo[2:len(str)] → "arsh"
print("str_demo[4:]:", str_demo[4:])    # From index 4 to end → "sh"

# Negative indexing (counts from the end)
print("\n--- 4. Negative Index Slicing ---")
# Negative indices: A(-6) d(-5) a(-4) r(-3) s(-2) h(-1)
print("str_demo[-6:]:", str_demo[-6:])      # Full string from -6 to end
print("str_demo[3:-2]:", str_demo[3:-2])    # From index 3 to -2 (exclusive) → "r"

text = "ABCDEFGH"

# Basic slicing (step = 1 by default)
print(text[0:6])     # "ABCDEF" - every character from 0 to 5

# Using step = 2
print(text[0:6:2])   # "ACE" - every 2nd character (A, skip B, C, skip D, E)

# Using step = 3  
print(text[0:8:3])   # "ADG" - every 3rd character (A, skip BC, D, skip EF, G)

# Negative step (reverses direction)
print(text[::-1])    # "HGFEDCBA" - entire string reversed
print(text[6:2:-1])  # "GFED" - from index 6 to 3, going backwards

# Combining with start/end
print(text[1:7:2])   # "BDF" - from index 1 to 6, every 2nd character


# ---------------------------------
# 4. String Methods
# ---------------------------------
print("\n--- 5. String Functions ---")

str_func = "i am awesome."
print("Original string:", str_func)

# String methods (remember: strings are immutable, so these return new strings)
print("endswith('ome.'):", str_func.endswith("ome."))        # True if ends with substring
print("capitalize():", str_func.capitalize())                # Capitalizes first character
print("replace():", str_func.replace("awesome", "Great"))    # Replaces first word with second
print("find('me'):", str_func.find("me"))                   # Returns index of first occurrence (-1 if not found)
print("count('a'):", str_func.count("a"))                   # Counts occurrences of substring

# The empty parentheses () are mandatory syntax for calling any function or method in Python. 
# They tell Python "execute this function now" rather than just "give me a reference to this function."
# This rule applies consistently whether the function needs arguments or not - it's part of Python's fundamental syntax for function calls.

'''
str.join(iterable) is a string method in Python.
It joins elements of an iterable (like a list of strings) into a single string,
using the string it is called on as the separator.

Example:
words = ["buy", "some", "milk"]
sentence = " ".join(words)  # Result: "buy some milk"
The argument to join must be an iterable of strings.
join is not a list method; it is a string method that takes a list (or tuple) of strings

Always use " ".join(user_input.split()) to collapse multiple spaces between words, not " ".join(user_input).
'''
# Example: Using join to combine a list of words into a sentence

words = ["Python", "is", "fun", "and", "powerful"]
sentence = " ".join(words)  # Joins the list into a single string with spaces
string_1 = "Hey  there,     How are   you. "
sentence1 = " ".join(string_1.split())  # Joins the list into a single string with spaces

print()
print(sentence1)  # Output: H
print(sentence,"\n")  # Output: Python is fun and powerful

# Membership testing
print("'a' in str_func:", 'a' in str_func)  # True
print("'z' in str_func:", 'z' in str_func)  # False


# ---------------------------------
# 5. String Iteration
# ---------------------------------
print("\n--- 6. Iterating through a string ---")

letter_count = 0
for letters in 'hello world':
    if letters == 'l':
        letter_count += 1
print(f"{letter_count} times the 'l' letter has been found")

# Using enumerate() to get both index and character
mystr = "Adarsh"
my_list_enumerate = list(enumerate(mystr))
print("list(enumerate(mystr)):", my_list_enumerate)  # [(0, 'A'), (1, 'd'), ...]


# ---------------------------------
# 6. Escape Sequences
# ---------------------------------
print("\n--- 7. Escape Sequences ---")

# Different ways to handle quotes in strings
print("""Tell me "What's your name".""")  # Triple quotes allow both ' and "
print("Tell me \"What's your name\".")     # Escape quotes with backslash

# Hexadecimal escape sequences
print("ABC written in \\x41\\x42\\x43 (HEX) representation:", end=" ")
print("\x41\x42\x43")

# Other common escape sequences: \t (tab), \n (newline), \\ (backslash), etc.


# ---------------------------------
# 7. String Formatting Methods
# ---------------------------------
print("\n--- 8. String Formatting ---")

name = "Adarsh"

# Method 1: .format() method (Python 2.7+ and 3.x)
print("Using .format():", "My name is {}".format(name))

# Method 2: f-strings (Python 3.6+, recommended for Python 3.12)
print("Using f-strings:", f"My name is {name}")

# Advanced formatting with .format()
print("\n--- 9. Advanced Number Formatting ---")

# Binary representation
print("Binary representation of {0} is {0:b}".format(20))

# Scientific notation (exponent)
print("Exponent representation: {0:e}".format(29.49))

# Floating point precision
print("One third is: {0:.3f}".format(1/3))  # Rounds to 3 decimal places

# Additional formatting options available in Python 3.12
number = 1234567.89
print(f"With thousand separators: {number:,.2f}")      # 1,234,567.89
print(f"Percentage format: {0.1234:.2%}")              # 12.34%, (.2 means upto 2 decimal places)
print(f"Padded with zeros: {42:05d}")                  # 00042


# ---------------------------------
# 8. Python Version Notes
# ---------------------------------
# PYTHON VERSION COMPATIBILITY NOTES:
# 
# Python 3.7 vs Python 3.12 differences in this code:
# 1. f-strings: Available in both (introduced in 3.6)
# 2. .format(): Available in both (works across all Python 3.x versions)
# 3. String methods: All methods shown work identically in both versions
# 4. Slicing behavior: Identical in both versions
# 
# New in Python 3.12 (not shown above):
# - Improved error messages for string operations
# - Performance improvements in string processing
# - Enhanced f-string debugging capabilities
# 
# If using Python 3.7:
# - All code above works without modification
# - f-strings work the same way
# - String methods have identical behavior
