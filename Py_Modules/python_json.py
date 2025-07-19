"""
Python JSON Module: Core Concepts

***Running this file will create a json file, that is essential for understanding the examples***
***Refer the basic quiz app for more understanding examples***

What is JSON?
============
JSON (JavaScript Object Notation) is a lightweight, text-based data interchange format.
Uses key-value pairs similar to Python dictionaries and is widely used for data exchange
between different systems, APIs, configuration files, and web applications.

JSON Structure Example:
{
    "name": "John Doe",
    "age": 30,
    "is_student": false,
    "courses": ["Python", "JavaScript"],
    "address": {"city": "New York", "zipcode": "10001"},
    "spouse": null
}

What is the JSON Module?
=======================
The json module is a built-in Python library that provides functionality for:
- Converting Python objects to JSON format (serialization)
- Converting JSON data to Python objects (deserialization)
- Reading and writing JSON files

Key Functions in JSON Module
============================
1. json.dumps() - Convert Python object to JSON string
2. json.loads() - Convert JSON string to Python object  
3. json.dump() - Write Python object to JSON file
4. json.load() - Read JSON data from file to Python object

Memory Trick: 
- dumps/loads work with STRINGS
- dump/load work with FILES
- The 's' in dumps/loads stands for 'string'

Data Type Mappings
=================
Python to JSON:
- dict → object
- list, tuple → array
- str → string
- int, float → number
- True → true
- False → false
- None → null

JSON to Python:
- object → dict
- array → list
- string → str
- number → int or float
- true → True
- false → False
- null → None

Common Use Cases
===============

1. API Data Exchange
   - Sending/receiving data to/from web APIs
   - Processing JSON responses from REST services

2. Configuration Files
   - Storing application settings and configurations
   - User preferences and application state

3. Data Storage and Transfer
   - Lightweight database alternative for simple data
   - Data export/import between different systems

4. Web Development
   - AJAX requests and responses
   - Client-server communication

5. Log Files and Analytics
   - Structured logging with JSON format
   - Data analysis and processing

Parameters and Options
=====================

json.dumps(obj, indent=None, separators=None, sort_keys=False, ensure_ascii=True)
json.loads(s, strict=True)
json.dump(obj, fp, indent=None, separators=None, sort_keys=False)
json.load(fp)

Common Parameters:
- indent: Pretty-printing with indentation (None, number, or string)
- separators: Tuple of (item_separator, key_separator)
- sort_keys: Sort dictionary keys in output (True/False)
- ensure_ascii: Escape non-ASCII characters (True/False)

Best Practices
==============
1. Always handle JSON parsing exceptions with try-except
2. Use proper indentation for readable JSON files
3. Validate JSON data structure before processing
4. Be careful with data types that don't have direct JSON equivalents
5. Use appropriate encoding (UTF-8) for international characters
6. Consider using json.JSONEncoder for custom object serialization
7. Be aware of floating-point precision issues
8. Use meaningful key names in JSON objects

Error Handling
=============
Common exceptions when working with JSON:
- json.JSONDecodeError: Invalid JSON format or syntax errors
- TypeError: Unsupported data type for serialization
- FileNotFoundError: JSON file doesn't exist
- PermissionError: File access permission issues
- UnicodeDecodeError: Character encoding problems

Performance Tips
===============
- Use json.loads() for parsing JSON strings in memory
- Use json.load() for reading JSON files directly
- Consider using ujson library for better performance with large datasets
- Avoid unnecessary pretty-printing (indent parameter) for production
- Cache parsed JSON data when possible to avoid repeated parsing
"""

# Example 1: Basic JSON String Operations
import json

def basic_json_operations():
    """Core JSON string to Python and back"""[1]
    person = {"name": "Alice", "age": 28, "skills": ["Python", "SQL"]}
    
    # Python to JSON string
    json_string = json.dumps(person)
    print(f"JSON String: {json_string}")
    
    # JSON string back to Python
    python_data = json.loads(json_string)
    print(f"Back to Python: {python_data['name']}")

basic_json_operations()

# Example 2: JSON File Operations
import json

def json_file_example():
    """Essential file read/write operations"""[2]
    data = {
        "app_name": "Todo App",
        "settings": {"theme": "dark", "notifications": True},
        "users": [{"name": "John", "tasks": 5}]
    }
    
    # Write to file
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    # Read from file  
    with open('config.json', 'r') as file:
        loaded_data = json.load(file)
    
    print(f"App: {loaded_data['app_name']}")
    print(f"Theme: {loaded_data['settings']['theme']}")

json_file_example()

# Example 3: Error Handling
import json

def safe_json_operations():
    """Proper error handling for JSON operations"""[3]
    
    def safe_parse(json_string):
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            return None
    
    # Valid JSON
    valid = '{"name": "John", "age": 30}'
    result = safe_parse(valid)
    print(f"Valid result: {result}")
    
    # Invalid JSON
    invalid = '{name: "John", age: 30}'  # Missing quotes
    result = safe_parse(invalid)
    print(f"Invalid result: {result}")

safe_json_operations()
