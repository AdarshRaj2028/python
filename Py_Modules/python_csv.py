r"""
Python CSV Module: Complete Guide

***Running this will create certain neccessary files in the current directory for better understanding***

What is the CSV Module?
======================
The csv module is a built-in Python library that provides functionality for reading and writing CSV 
(Comma-Separated Values) files. It's part of Python's standard library, so no installation is required.

The module handles the complexity of parsing CSV files, including:
- Proper handling of quoted fields containing commas
- Different delimiters (comma, semicolon, tab, etc.)
- Escape characters and special formatting
- Different CSV dialects and formats

Key Components of the CSV Module
===============================

1. csv.reader() - Reads CSV files row by row as lists
2. csv.writer() - Writes data to CSV files row by row
3. csv.DictReader() - Reads CSV files as dictionaries (column headers as keys)
4. csv.DictWriter() - Writes dictionaries to CSV files
5. csv.Sniffer() - Detects CSV format and dialect automatically

Why the CSV Module is Important
==============================
- Handles edge cases automatically (quotes, commas in data, etc.)
- Provides consistent interface for CSV operations
- Memory efficient for large files (reads line by line)
- Supports different CSV dialects and formats
- Built-in error handling for malformed CSV files
- Cross-platform compatibility

Common Use Cases
===============

1. Data Import/Export
   - Reading data from databases exported as CSV
   - Importing spreadsheet data into Python programs
   - Exporting Python data structures to CSV for Excel

2. Configuration Management
   - Reading configuration files in CSV format
   - Managing application settings and parameters

3. Data Processing and Analysis
   - Processing large datasets from CSV files
   - Data cleaning and transformation
   - Statistical analysis of CSV data

4. Log File Processing
   - Reading and analyzing log files in CSV format
   - Generating reports from CSV log data

5. Data Exchange Between Systems
   - Transferring data between different applications
   - API data export/import in CSV format

Key Methods and Parameters
=========================

csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv.DictReader(file, fieldnames=None, delimiter=',')
csv.DictWriter(file, fieldnames, delimiter=',')

Use csv.reader() when:  Simple reading, data processing by index
Use csv.writer() when:  Simple writing, data in lists/tuples
Use DictReader() when:  Reading with column names, data analysis
Use DictWriter() when:  Writing with column names, structured output

Memory Trick
============
reader/writer = Lists (simple, indexed access)
DictReader/DictWriter = Dictionaries (named access, more readable)

Common Parameters:
- delimiter: Character that separates fields (default: comma)
- quotechar: Character used to quote fields (default: double quote)
- quoting: When to quote fields (QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE)
- lineterminator: String used to terminate lines (default: '\r\n')
- skipinitialspace: Ignore whitespace after delimiter (default: False)

Error Handling
=============
Common exceptions when working with CSV module:
- FileNotFoundError: When CSV file doesn't exist
- csv.Error: General CSV parsing errors
- UnicodeDecodeError: Character encoding issues
- PermissionError: File access permission problems

Best Practices
==============
1. Always use 'newline=""' parameter when opening files for writing
2. Use context managers (with statement) for automatic file closing
3. Handle encoding explicitly for international characters
4. Use DictReader/DictWriter for better code readability
5. Validate data before writing to CSV
6. Use appropriate quoting for data containing special characters
7. Handle exceptions gracefully with try-except blocks
8. Use fieldnames parameter in DictWriter for consistent column order

Performance Tips
===============
- Use csv.reader() for large files (memory efficient)
- Process data in chunks for very large CSV files
- Use appropriate data types to minimize memory usage
- Consider using pandas for complex data analysis tasks
- Use csv.Sniffer() to automatically detect CSV format
"""

# Example 1: Basic CSV Reading and Writing
import csv

# Writing to CSV file
def write_basic_csv():
    """Demonstrate basic CSV writing"""
    data = [
        ['Name', 'Age', 'City', 'Occupation'],
        ['John Doe', 28, 'New York', 'Engineer'],
        ['Jane Smith', 32, 'Los Angeles', 'Designer'],
        ['Bob Johnson', 45, 'Chicago', 'Manager'],
        ['Alice Brown', 29, 'Houston', 'Analyst']
    ]
    
    with open('basic_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
# The writerow() method writes a single row of data to a CSV file. 
# It takes an iterable (like a list, tuple, or string) as a parameter 
# and writes each item in that iterable as a comma-separated line in the CSV file
    print("Basic CSV file created: basic_data.csv")

# Reading from CSV file
def read_basic_csv():
    """Demonstrate basic CSV reading"""
    print("\nReading basic CSV file:")
    with open('basic_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row_num, row in enumerate(reader, 1):
            print(f"Row {row_num}: {row}")

# Run basic example
write_basic_csv()
read_basic_csv()
print()

# Example 2: Working with Dictionary Reader/Writer
import csv

def write_dict_csv():
    """Demonstrate DictWriter usage"""
    employees = [
        {'name': 'Sarah Connor', 'department': 'Security', 'salary': 85000, 'years': 3},
        {'name': 'John Matrix', 'department': 'Operations', 'salary': 75000, 'years': 5},
        {'name': 'Ellen Ripley', 'department': 'Engineering', 'salary': 90000, 'years': 7},
        {'name': 'Dutch Schaefer', 'department': 'Military', 'salary': 80000, 'years': 10}
    ]
    
    field = ['name', 'department', 'salary', 'years']
    
    with open('employees.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field)  # Fieldnames here means exact column names
        writer.writeheader()  # Write column headers(I.E only heading parts, fieldnames here to be exact)
        writer.writerows(employees)  # Writes data of employees below headings
'''
The writeheader() method is a built-in method of the csv.DictWriter class 
that automatically writes the column headers (field names) as the first row of a CSV file.
It uses the fieldnames parameter that was specified when creating the DictWriter object to determine what headers to write.

writeheader() is not used in dictionary only. 
However, it is specifically a method of the csv.DictWriter class, 
which means it's only available when working with dictionary-based CSV operations.
'''
print("Dictionary CSV file created: employees.csv")

def read_dict_csv():
    """Demonstrate DictReader usage"""
    print("\nReading dictionary CSV file:")
    with open('employees.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Department: {row['department']}, Salary: ${row['salary']}")

# Run dictionary example
write_dict_csv()
read_dict_csv()
print()

# Example 3: Data Analysis with CSV
import csv

def create_sales_data():
    """Create sample sales data for analysis"""
    sales_data = [
        ['Date', 'Product', 'Quantity', 'Unit_Price', 'Total_Sales'],
        ['2025-01-01', 'Laptop', 5, 1200, 6000],
        ['2025-01-02', 'Phone', 10, 800, 8000],
        ['2025-01-03', 'Tablet', 8, 500, 4000],
        ['2025-01-04', 'Laptop', 3, 1200, 3600],
        ['2025-01-05', 'Phone', 15, 800, 12000],
        ['2025-01-06', 'Tablet', 12, 500, 6000],
        ['2025-01-07', 'Laptop', 7, 1200, 8400]
    ]
    
    with open('sales_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sales_data)
# Both functions work with lists, but writerows() is specifically for a list of lists (multiple rows),
# while writerow() is for a single list (one row).

    print("Sales data CSV created: sales_data.csv")

def analyze_sales():
    """Perform basic analysis on sales data"""
    total_revenue = 0
    product_sales = {}
    product_quantities = {}
    
    with open('sales_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Calculate totals
            sales = int(row['Total_Sales'])
            quantity = int(row['Quantity'])
            product = row['Product']
            
            total_revenue += sales
            
            # Track by product
            if product in product_sales:
                product_sales[product] += sales
                product_quantities[product] += quantity
            else:
                product_sales[product] = sales
                product_quantities[product] = quantity
    
    print(f"\nSales Analysis:")
    print(f"Total Revenue: ${total_revenue:,}")
    print(f"\nRevenue by Product:")
    for product, revenue in product_sales.items():
        print(f"  {product}: ${revenue:,}")
    
    print(f"\nQuantities Sold:")
    for product, quantity in product_quantities.items():
        print(f"  {product}: {quantity} units")

# Run sales analysis
create_sales_data()
analyze_sales()
print()

# Example 4: Different Delimiters and Formats
import csv

def create_semicolon_csv():
    """Create CSV with semicolon delimiter"""
    data = [
        ['Country', 'Capital', 'Population', 'GDP_Billions'],
        ['United States', 'Washington DC', '331000000', '21427'],
        ['China', 'Beijing', '1439000000', '14342'],
        ['Japan', 'Tokyo', '126000000', '5082'],
        ['Germany', 'Berlin', '83000000', '3846']
    ]
    
    with open('countries.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(data)
    print("Semicolon-delimited CSV created: countries.csv")

def read_semicolon_csv():
    """Read semicolon-delimited CSV"""
    print("\nReading semicolon-delimited CSV:")
    with open('countries.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(' | '.join(row))

# Run delimiter example
create_semicolon_csv()
read_semicolon_csv()
print()

# Example 5: Error Handling and Validation
import csv
import os

def safe_csv_operations():
    """Demonstrate error handling with CSV operations"""
    
    def read_csv_with_validation(filename):
        """Read CSV file with comprehensive error handling"""
        try:
            # Check if file exists
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' does not exist!")
                return None
            
            # Check if file is empty
            if os.path.getsize(filename) == 0:
                print(f"Error: File '{filename}' is empty!")
                return None
            
            data = []
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                
                # Check if file has headers
                if reader.fieldnames is None:
                    print(f"Error: File '{filename}' has no headers!")
                    return None
                
                print(f"Successfully opened '{filename}'")
                print(f"Headers: {reader.fieldnames}")
                
                for row_num, row in enumerate(reader, 1):
                    # Validate row data
                    if any(value.strip() == '' for value in row.values()):
                        print(f"Warning: Row {row_num} has empty values")
                    
                    data.append(dict(row))
                    print(f"Row {row_num}: {dict(row)}")
                
                return data
                
        except FileNotFoundError:
            print(f"Error: Could not find file '{filename}'")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except UnicodeDecodeError as e:
            print(f"Encoding error: {e}")
        except PermissionError:
            print(f"Permission error: Cannot access file '{filename}'")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        return None
    
    # Create test data with some issues
    test_data = [
        ['id', 'name', 'email', 'age'],
        ['1', 'Alice Johnson', 'alice@email.com', '25'],
        ['2', 'Bob Smith', '', '30'],  # Empty email
        ['3', 'Charlie Brown', 'charlie@email.com', '28'],
        ['4', '', 'diana@email.com', '35']  # Empty name
    ]
    
    # Write test file
    with open('test_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(test_data)
    
    print("Testing CSV validation:")
    read_csv_with_validation('test_data.csv')
    
    print("\nTesting with non-existent file:")
    read_csv_with_validation('nonexistent.csv')

# Run error handling example
safe_csv_operations()
print()

# Example 6: Working with Large CSV Files
import csv

def process_large_csv():
    """Demonstrate memory-efficient processing of large CSV files"""
    
    # Create a larger sample dataset
    print("Creating large sample dataset...")
    with open('large_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Score', 'Category'])
        
        # Generate 1000 rows of sample data
        for i in range(1, 1001):
            name = f"Person_{i}"
            score = (i * 7) % 100  # Generate varied scores
            category = ['A', 'B', 'C'][i % 3]
            writer.writerow([i, name, score, category])
    
    print("Large CSV file created: large_data.csv")
    
    # Process file efficiently
    print("\nProcessing large file efficiently:")
    category_stats = {'A': [], 'B': [], 'C': []}
    row_count = 0
    
    with open('large_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            row_count += 1
            category = row['Category']
            score = int(row['Score'])
            category_stats[category].append(score)
            
            # Process in batches to show progress
            if row_count % 100 == 0:
                print(f"Processed {row_count} rows...")
    
    # Calculate statistics
    print(f"\nProcessed {row_count} total rows")
    for category, scores in category_stats.items():
        avg_score = sum(scores) / len(scores)
        print(f"Category {category}: {len(scores)} items, Average score: {avg_score:.2f}")

# Run large file example
process_large_csv()
print()

# Example 7: CSV Sniffer for Format Detection
import csv

def demonstrate_csv_sniffer():
    """Show how to use csv.Sniffer to detect CSV format"""
    
    # Create CSV files with different formats
    formats = [
        ('comma_format.csv', ',', [['Name', 'Age', 'City'], ['John', '25', 'NYC']]),
        ('semicolon_format.csv', ';', [['Name', 'Age', 'City'], ['Jane', '30', 'LA']]),
        ('tab_format.csv', '\t', [['Name', 'Age', 'City'], ['Bob', '35', 'Chicago']])
    ]
    
    # Create test files
    for filename, delimiter, data in formats:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerows(data)
    
    # Use Sniffer to detect format
    sniffer = csv.Sniffer()
    
    for filename, expected_delimiter, _ in formats:
        print(f"\nAnalyzing {filename}:")
        
        with open(filename, 'r') as file:
            # Read a sample to detect format
            sample = file.read(1024)
            file.seek(0)  # Reset file pointer
            
            # Detect delimiter
            try:
                dialect = sniffer.sniff(sample)
                print(f"  Detected delimiter: '{dialect.delimiter}'")
                print(f"  Expected delimiter: '{expected_delimiter}'")
                print(f"  Match: {dialect.delimiter == expected_delimiter}")
                
                # Check if file has headers
                has_header = sniffer.has_header(sample)
                print(f"  Has headers: {has_header}")
                
                # Read file using detected format
                reader = csv.reader(file, dialect)
                for row in reader:
                    print(f"  Data: {row}")
                    
            except csv.Error as e:
                print(f"  Could not detect format: {e}")

# Run sniffer example
demonstrate_csv_sniffer()

# Clean up created files (optional)
import os
files_to_clean = [
    'basic_data.csv', 'employees.csv', 'sales_data.csv', 'countries.csv',
    'test_data.csv', 'large_data.csv', 'comma_format.csv', 
    'semicolon_format.csv', 'tab_format.csv'
]

print(f"\nCreated {len(files_to_clean)} CSV files for demonstration.")
print("You can examine these files and run the examples multiple times.")
