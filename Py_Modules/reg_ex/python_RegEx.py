r"""
======================================================================
PYTHON REGEX (re) MODULE: COMPLETE CONCEPT GUIDE
======================================================================

***Running this file will demonstrate essential regex concepts with practical examples***

What is Regex?
==============
Regular Expressions (Regex) are sequences of characters that form search patterns.
The re module is Python's built-in library for regex operations - no installation needed!

Key Strengths:
- Works nearly identically across all programming languages
- Find, validate, replace, and extract text efficiently
- Handle complex string operations in single lines
- Process large amounts of text data quickly

Common Use Cases
===============
1. Data Validation: Email, phone numbers, passwords, URLs
2. Text Processing: Log file analysis, web scraping, data extraction
3. String Manipulation: Find and replace, text cleaning, formatting
4. Data Extraction: Parsing structured/unstructured text

Core Functions
=============
Function          | Purpose                        | Returns
------------------|--------------------------------|---------------------------
re.search()       | Find first match anywhere      | Match object or None
re.match()        | Match at string beginning      | Match object or None
re.findall()      | Find all matches               | List of strings
re.finditer()     | Find all matches (iterator)    | Iterator of Match objects
re.sub()          | Replace matches                | Modified string
re.split()        | Split by pattern               | List of strings
re.compile()      | Compile pattern for reuse      | Pattern object

Memory Trick: "SFF" - Search, Findall, Finditer (the main search functions)

Essential Patterns
==================

Basic Patterns:
.               Any character except newline
^               Start of string
$               End of string
*               0 or more repetitions
+               1 or more repetitions
?               0 or 1 repetition (optional)
{n}             Exactly n repetitions
{n,m}           Between n and m repetitions
[]              Character set
|               OR operator
()              Capturing group

Character Classes:
\d              Any digit [0-9]
\D              Any non-digit
\w              Word character [a-zA-Z0-9_]
\W              Non-word character
\s              Whitespace (space, tab, newline)
\S              Non-whitespace
\b              Word boundary

Escape Special Characters:
\.  \*  \+  \?  \[  \]  \(  \)  \^  \$  \|  \\

Regex Flags (Modifiers)
=======================
re.IGNORECASE (re.I)    Case-insensitive matching
re.MULTILINE (re.M)     ^ and $ match line beginnings/ends
re.DOTALL (re.S)        . matches newline too
re.VERBOSE (re.X)       Allow comments in pattern

Usage: re.search(pattern, string, re.IGNORECASE)

RAW STRINGS - CRITICAL!
===========================
Always use raw strings (r"") for regex patterns!

Why? Backslash conflicts:
- Python: "\n" = newline, "\t" = tab  
- Regex: "\d" = digit, "\w" = word character

Without raw string:    "\\d+"     (need double backslash)
With raw string:       r"\d+"     (clean and readable)

Rule: If your pattern contains \, use r""

Quantifiers - Greedy vs Lazy
=============================
Greedy (default) - Match as much as possible:
*       +       ?       {n,m}

Lazy - Match as little as possible:
*?      +?      ??      {n,m}?

Example:
Greedy: "<.*>" in "<tag>text</tag>" matches entire string
Lazy:   "<.*?>" matches "<tag>" and "</tag>" separately

Groups and Capturing
====================
(pattern)       Capturing group (extract matched portions)
(?:pattern)     Non-capturing group (faster, no capture)
(?P<name>...)   Named group
\1, \2          Backreference to group 1, 2

Example:
pattern = r"(\w+)@(\w+)\.(\w+)"
match = re.search(pattern, "user@example.com")
match.group(1)  # "user"
match.group(2)  # "example"

Lookahead & Lookbehind (Advanced)
==================================
(?=...)     Positive lookahead (followed by)
(?!...)     Negative lookahead (NOT followed by)
(?<=...)    Positive lookbehind (preceded by)
(?<!...)    Negative lookbehind (NOT preceded by)

Common use: Password validation requiring multiple character types

Common Gotchas
==============
-> Forgetting raw strings: "\d+" instead of r"\d+"
-> Greedy matching: Use .*? instead of .* when needed
-> Not escaping special chars: Use \. for literal period
-> Ignoring None returns: Always check if match exists
-> Using wrong function: match() vs search() vs findall()

Best Practices
==============
-> Always use raw strings: r"\d+" not "\d+"
-> Compile patterns for reuse: pattern = re.compile(r"...")
-> Use specific patterns: \d+ not .+
-> Validate before processing: check if match exists
-> Test patterns with online tools (regex101.com)
-> Handle None returns from search/match
-> Use non-capturing groups when you don't need capture: (?:...)

Learning Path
=============
Beginner:     Basic patterns (., *, +, ?) → Character classes (\d, \w, \s)
Intermediate: Quantifiers {n,m} → Groups () → Flags
Advanced:     Lookaheads/Lookbehinds → Named groups → Complex patterns
"""

import re

print("="*70)
print("PYTHON REGEX MODULE - PRACTICAL EXAMPLES")
print("="*70)
print()

# ============================================================================
# 1. BASIC MATCHING
# ============================================================================

print("1. BASIC PATTERN MATCHING")
print("-" * 70)

# Check if pattern exists
if re.search("ape", "The ape was at the apex"):
    print("Found 'ape' in string")

# Case-insensitive search
if re.search("APE", "The ape was at the apex", re.IGNORECASE):
    print("Found 'APE' (case-insensitive)")

# Match at beginning only
if re.match("The", "The ape was at the apex"):
    print("String starts with 'The'")

print()

# ============================================================================
# 2. FINDALL vs FINDITER
# ============================================================================

print("2. FINDALL vs FINDITER")
print("-" * 70)

text = "The ape was at the apex"

# findall returns list
all_matches = re.findall(r"ape.", text)
print(f"findall() returns list: {all_matches}")

# finditer returns iterator with positions
print("finditer() returns iterator with positions:")
for match in re.finditer(r"ape.", text):
    print(f"  '{match.group()}' at position {match.span()}")

print()

# ============================================================================
# 3. CHARACTER CLASSES
# ============================================================================

print("3. CHARACTER CLASSES")
print("-" * 70)

animal_str = 'Cat rat mat fat Pat'

# Match specific characters
matches = re.findall(r"[crfP]at", animal_str)
print(f"[crfP]at: {matches}")

# Match ranges
matches = re.findall(r"[a-zA-Z]at", animal_str)
print(f"[a-zA-Z]at: {matches}")

# Negated class (NOT these characters)
matches = re.findall(r"[^Cr]at", animal_str)
print(f"[^Cr]at (NOT C or r): {matches}")

print()

# ============================================================================
# 4. SPECIAL CHARACTER CLASSES (\d, \w, \s)
# ============================================================================

print("4. SPECIAL CHARACTER CLASSES")
print("-" * 70)

text = "Phone: 123-456-7890, Code: ABC123"

# \d - Digits
digits = re.findall(r"\d+", text)
print(f"\\d+ (digits): {digits}")

# \w - Word characters
words = re.findall(r"\w+", text)
print(f"\\w+ (words): {words}")

# Combined pattern
phone = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(f"Phone pattern: {phone}")

print()

# ============================================================================
# 5. QUANTIFIERS
# ============================================================================

print("5. QUANTIFIERS")
print("-" * 70)

# Exactly n times: {n}
zips = re.findall(r"\d{5}", "Zips: 12345 123456 1234")
print(f"\\d{{5}} (exactly 5 digits): {zips}")

# Range: {n,m}
codes = re.findall(r"\d{3,5}", "123 12345 123456")
print(f"\\d{{3,5}} (3 to 5 digits): {codes}")

# One or more: +
repeated = re.findall(r"a+", "a aa aaa b")
print(f"a+ (one or more): {repeated}")

# Optional: ?
colors = re.findall(r"colou?r", "color colour")
print(f"colou?r (optional u): {colors}")

print()

# ============================================================================
# 6. GREEDY VS LAZY
# ============================================================================

print("6. GREEDY VS LAZY MATCHING")
print("-" * 70)

html = "<div>Content 1</div><div>Content 2</div>"

# Greedy - matches as much as possible
greedy = re.findall(r"<div>.*</div>", html)
print(f"Greedy (.*): {greedy}")

# Lazy - matches as little as possible  
lazy = re.findall(r"<div>.*?</div>", html)
print(f"Lazy (.*?): {lazy}")

print()

# ============================================================================
# 7. ANCHORS (^ and $)
# ============================================================================

print("7. ANCHORS")
print("-" * 70)

# ^ - Start of string
if re.search(r"^Hello", "Hello World"):
    print("Starts with 'Hello'")

# $ - End of string
if re.search(r"World$", "Hello World"):
    print("Ends with 'World'")

# Word boundaries
text = "The cat scattered"
whole_word = re.findall(r"\bcat\b", text)
print(f"\\bcat\\b (whole word only): {whole_word}")

print()

# ============================================================================
# 8. GROUPS AND CAPTURING
# ============================================================================

print("8. GROUPS AND CAPTURING")
print("-" * 70)

email = "john.doe@company.com"
pattern = r"(\w+)\.(\w+)@(\w+)\.(\w+)"
match = re.search(pattern, email)

if match:
    print(f"Full: {match.group(0)}")
    print(f"First name: {match.group(1)}")
    print(f"Last name: {match.group(2)}")
    print(f"Domain: {match.group(3)}")

# Named groups
pattern_named = r"(?P<first>\w+)\.(?P<last>\w+)@(?P<domain>\w+)\.(?P<tld>\w+)"
match_named = re.search(pattern_named, email)
if match_named:
    print(f"Using named groups - Domain: {match_named.group('domain')}")

print()

# ============================================================================
# 9. BACKREFERENCES
# ============================================================================

print("9. BACKREFERENCES")
print("-" * 70)

# Find repeated words
text = "The the cat sat on the the mat"
duplicates = re.findall(r"\b(\w+)\s+\1\b", text, re.IGNORECASE)
print(f"Duplicate words: {duplicates}")

print()

# ============================================================================
# 10. SUBSTITUTION (re.sub)
# ============================================================================

print("10. SUBSTITUTION WITH re.sub()")
print("-" * 70)

# Simple replacement
text = "The cat and the dog"
replaced = re.sub(r"cat", "tiger", text)
print(f"Replace: {replaced}")

# Censor phone numbers
text_phone = "Call 123-456-7890 or 987-654-3210"
censored = re.sub(r"\d{3}-\d{3}-\d{4}", "[REDACTED]", text_phone)
print(f"Censored: {censored}")

# Reformat dates with backreferences
dates = "Date: 2025-01-15"
formatted = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", dates)
print(f"Reformatted: {formatted}")

print()

# ============================================================================
# 11. SPLITTING
# ============================================================================

print("11. SPLITTING WITH re.split()")
print("-" * 70)

# Split by multiple delimiters
text = "apple,banana;cherry:date"
fruits = re.split(r"[,;:]", text)
print(f"Split by multiple: {fruits}")

# Split by whitespace
text_spaces = "word1    word2  word3"
words = re.split(r"\s+", text_spaces)
print(f"Split by whitespace: {words}")

print()

# ============================================================================
# 12. COMPILING PATTERNS
# ============================================================================

print("12. COMPILING FOR REUSE")
print("-" * 70)

# Compile pattern (more efficient for reuse)
email_pattern = re.compile(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}")

test_emails = ["valid@example.com", "invalid@", "another@test.co.uk"]

for email in test_emails:
    if email_pattern.search(email):
        print(f"Valid: {email}")
    else:
        print(f"Not valid: {email}")

print()

# ============================================================================
# 13. HANDLING BACKSLASHES
# ============================================================================

print("13. RAW STRINGS - SOLVING BACKSLASH PROBLEMS")
print("-" * 70)

text = "Here is \\stuff"

# Without raw string (requires 4 backslashes!)
# print(re.search("\\\\stuff", text))

# With raw string (clean and correct)
pattern = r'\\stuff'
print(f"Found \\stuff: {re.search(pattern, text)}")

# Finding literal dots
text_dots = "F.B.I. and C.I.A."
matches = re.findall(r"\.\w\.", text_dots)
print(f"Patterns like .X.: {matches}")

print()

# ============================================================================
# 14. REAL-WORLD VALIDATION
# ============================================================================

print("14. REAL-WORLD VALIDATION")
print("-" * 70)

# Email validation
def validate_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Phone validation (US)
def validate_phone(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

# Password strength (requires: uppercase, lowercase, digit, 8+ chars)
def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$"
    return bool(re.match(pattern, password))

# Test
test_data = [
    ("Email", "user@example.com", validate_email),
    ("Phone", "123-456-7890", validate_phone),
    ("Password", "Strong123", validate_password),
]

for name, value, validator in test_data:
    result = "True" if validator(value) else "False"
    print(f"{result} {name}: {value}")

print()

# ============================================================================
# 15. TEXT CLEANING
# ============================================================================

print("15. TEXT CLEANING")
print("-" * 70)

dirty = "Hello!!!   Multiple    spaces...  here???"

# Remove extra spaces
cleaned = re.sub(r"\s+", " ", dirty)
print(f"Clean spaces: {cleaned}")

# Remove duplicate punctuation
cleaned = re.sub(r"([!.?])\1+", r"\1", dirty)
print(f"Clean punctuation: {cleaned}")

print()

# ============================================================================
# 16. LOG FILE PARSING
# ============================================================================

print("16. LOG FILE PARSING")
print("-" * 70)

log = """
2025-01-15 10:23:45 ERROR Database connection failed
2025-01-15 10:24:15 ERROR Connection timeout
2025-01-15 10:25:00 INFO Connection successful
"""

# Extract ERROR messages
errors = re.findall(r".*ERROR.*", log)
print(f"ERROR count: {len(errors)}")

# Parse log structure
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)"
for match in re.finditer(pattern, log):
    timestamp, level, message = match.groups()
    if level == "ERROR":
        print(f"  {timestamp} - {message}")

print()

# ============================================================================
# 17. ERROR HANDLING
# ============================================================================

print("17. ERROR HANDLING")
print("-" * 70)

def safe_search(pattern, text):
    try:
        return re.search(pattern, text)
    except re.error as e:
        print(f"Invalid regex: {e}")
        return None

# Valid pattern
result = safe_search(r"\d+", "Test 123")
print(f"Valid pattern: {result}")

# Invalid pattern (unmatched parenthesis)
result = safe_search(r"(\d+", "Test 123")
print(f"Invalid pattern: {result}")

print()
