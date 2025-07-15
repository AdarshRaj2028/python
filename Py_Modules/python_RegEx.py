'''
The regex module (officially called the re module in Python) is a built-in package that provides regular expression matching operations.
Regular expressions (RegEx) are sequences of characters that form search patterns,
allowing you to check if strings contain specified patterns or perform complex string manipulations

Regular expressions allow you to locate and change strings in very powerful ways.
They work in almost exactly the same way in every programming language as well.

Regular expressions (Regex) are used to :
1. Search for a specific string in a large amount of data
2. Verify that a string has the proper format (Email, Phone #) 
3. Find a string and replace it with another strings 
4. Format data into the proper form for importing for example 
'''
# import the Regex module
import re

# ------------- Was a match found -------------------

# Search for ape in the string
if re.search("ape2", "The ape was at the apex"):
    # print("There is an ape")
    print(True)
else:
    print(False)

print()

#  ----------- Get All matches ------------------
# . is used to match any 1 character or space(ape.)
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)
print()

# finditer returns as iterator of matching objects
# You can use span to get the location

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):

    # Span returns a tuple
    locTuple = i.span()

    print(locTuple)

    # Slice the match out using the tuple values
    print(theStr[locTuple[0]: locTuple[1]])

    print()

# ------------- Match 1 of Several Letters ---------------
# 
# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties 
# unless they are listed

animalStr = 'Cat rat mat fat Pat'

allAnimals = re.findall("[crMfP]at", animalStr)
for i in allAnimals:
    print(i)

print()

# We can also follow for characters in a range
# Remember to include upper and lowercase letters
someAnimals = re.findall("[a-zA-Z]at", animalStr) # This means to find all character from lower case 'a' to lower case 'z' and from upper case 'A' to upper case 'Z'
for i in someAnimals:
    print(i)

print()

# Use ^ to denote any character, except whatever characters are between the brackets
animalStr = 'Cat rat mat fat pat'
someAnimals = re.findall("[^Cr]at", animalStr)
for i in someAnimals:
    print(i)

print()

# -------------- Replace All Matches -----------------

# Replace matching items in a string
# re.compile() is used to compile a regular expression pattern into a pattern object that can be reused multiple times. 
# When you compile a regular expression pattern, 
# you're essentially telling Python: "Hey, take this search pattern and convert it into a special format that's faster to use."

owlFood = "rat cat mat pat"

# You can compile a regex into pattern objects which provide additional methods
regex = re.compile("[cr]at") 

# sub() replaces items that match the regex in the string with the 1st attribute string passed to sub
# re.sub() looks through your text, finds specific patterns (like words, numbers, or characters), and replaces them with something else. 
# It's like having a smart assistant that can find and change text for you automatically
owlFood = regex.sub("owl", owlFood)

print(owlFood)
print()

# ------------------------Solving Backslash Problems---------------------------------

# Regex use the backslash to designate special characters and Python does the same inside strings which causes issues.

# Let's try to get "\\stuff" out of a string

randStr = "Here is \\stuff"

# This won't find it

print("Find \\stuff: ", re.search("\\stuff", randStr))

#This does, but we have to put in 4 slashes which is messy

print("Find \\stuff : ", re.search("\\\\stuff", randStr))

# You can get around this by using raw strings(put r in the place where we put f during string formatting) which don't treat backslashes as special
# You can use either raw strings (with r) or regular strings when creating regex patterns, but raw strings are strongly recommended for regex patterns.
# Raw strings prevent Python from interpreting backslashes as escape characters before the regex engine sees them
print("Find \\stuff : ", re.search(r"\\stuff", randStr))

print()

# --------------------- Matching Any Character --------------------------
# We saw that . matches any character, but what if we want to match a period
# Backslash the period, You do the same with [, ] and others

randStr1 = "F.B.I. I.R.S. CIA"

print("Matches :", len(re.findall(".\..\..", randStr1)))  # type: ignore
# Here ".\..\..", randStr1, first . means First character, \. means next dot, then . means next character, again \. means next dot in FBI or IRS, then next . is next character
print("Matches :", re.findall(".\..\..", randStr1)) # type: ignore
print() 

# ------------------ Matching Whitespace ------------------------
# We can match many whitespace characters

randStr2 = '''This is a long
string that goes
on for many lines'''

print(randStr2)

# Remove newlines
regex = re.compile("\n")

randStr2 = regex.sub(" ", randStr2)

print(randStr2)
#  You can also match 
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab
# \d+ is a regex pattern that means "match one or more digits"
# \d = any single digit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# + = one or more times
# \d{3} means "match exactly 3 digits".
# The {3} is called a quantifier that specifies exactly how many times the preceding pattern should repeat.

# You may need to remove \r\n on Windows

# Always use raw strings for regex patterns:

# Good
email_pattern = re.compile(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}')

# Avoid (but works)
email_pattern = re.compile('[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}')

print()

# Using re.sub() for Text Replacement

text = "Phone: 123-456-7890, Emergency: 911"

# Replace phone numbers with [REDACTED]
censored = re.sub(r'\d{3}-\d{3}-\d{4}', '[REDACTED]', text)
print(censored)  # Output: "Phone: [REDACTED], Emergency: 911"

# Replace all numbers
all_censored = re.sub(r'\d+', 'XXX', text)
print(all_censored)  # Output: "Phone: XXX-XXX-XXX, Emergency: XXX"
print()

# ---------- Matching Any Single Number -------------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]

randStr3 = "12345"

print("Matches :", len(re.findall("\d", randStr3))) # type: ignore
print("Matches :", re.findall("\d", randStr3)) # type: ignore
print()

# ----------- Matching Multiple Numbers ---------- 

# You can match multiple digits by following the \d with {numofValues}
# Match 5 numbers only 
if re.search("\d{5}", "12345"):  # type: ignore
    print("It is a zip code")

# You can also match within a range
# Match values that are between 5 and 7 digits
numStr = "123 12345 123456 1234567"

print("Matches:", len(re.findall("\d{5,7}", numStr))) # type: ignore

print()

# ------------------ Matching Any Single Letter or Number --------------------
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]

phNum = "412-555-1212"

# Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}", phNum):  # type: ignore 
    print("It is a phone number.")

# Check for valid first name between 2 and 20 characters
if re.search("\w{2,20}", "Ultraman"):  # type: ignore
    print("It is a valid name")


# ------------------ Matching WhiteSpace ----------------
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

# Check for the valid first and last name with a space
if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):  # type: ignore
    print("It is a vaild full name")
print()

# ---------------- Matching One or More -------------------
# + matches 1 or more characters

# Match a followed by 1 or more characters 
print("Matches :", len(re.findall("a+", "a as ape bug"))) 
print("Matches :", re.findall("a+", "a as ape bug"))

print()

# ------------------- Problem ------------------------

# Create a Regex that matches email addresses from a List
# 1. 1 to 20 Lowercase and uppercase letters, numbers, plus .%+-
# 2. An @ symbol
# 3. 2 to 20 Lowercase and uppercase letters, numbers, plus-
# 4. A period
# 5. 2 to 3 Lowercase and uppercase Letters

emailList = "db@aol.com m@.com @apple.com db@.com"

print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-za-z]{2,3}", emailList))) # type: ignore
print("Email Matches :", re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-za-z]{2,3}", emailList)) # type: ignore

