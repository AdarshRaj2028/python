# ============================================================================
# ASSERT STATEMENT FOR DEBUGGING
# ============================================================================
# Assert is used to check assumptions during development
# Syntax: assert condition, "error_message"
# If condition is False, program crashes with AssertionError
# Example: assert y != 0, "Cannot divide by zero"

# Assertion without error message
def avg(marks):
    assert len(marks) != 0, "List is empty"
    return sum(marks)/len(marks)

mark1 = [11,22,33]
print("Average of mark1:", avg(mark1))

# mark1 = []        # This will give AssertionError
# print("Average of mark1:", avg(mark1))

# ============================================================================
# LIBRARY FEE CALCULATOR - MAIN PROGRAM
# ============================================================================

# INPUT VALIDATION WITH ASSERT (Enhanced version)
def get_validated_inputs():
    """Function to get and validate user inputs using assert"""
    grade = int(input("Enter the Grade(1-5): "))
    section = input("Enter the Section: ").upper()  # Convert to uppercase for consistency
    
    # Using assert for input validation (debugging purpose)
    assert 1 <= grade <= 5, f"Grade must be between 1-5, got {grade}"
    assert section in ['A', 'B'], f"Section must be 'A' or 'B', got {section}"
    
    return grade, section

# MAIN LOGIC WITH NESTED IF-ELSE CONDITIONS
def calculate_library_fee():
    try:
        G = int(input("Enter the Grade(1-5): "))
        S = input("Enter the Section: ").upper()
        
        # COMPOUND CONDITION CHECK
        # Using logical operators: and, or
        # Parentheses for clarity and proper precedence
        if (G >= 1 and G <= 5) and (S == 'A' or S == 'B'):
            
            # NESTED IF-ELIF-ELSE STRUCTURE
            # Rule 1: Grade 1 or 2 AND Section A = Fee 100
            if (G == 1 or G == 2) and S == 'A':
                print("The fee is 100")
            
            # Rule 2: Grade 3 or 4 OR Section B = Fee 200
            # IMPORTANT: This condition uses OR logic
            # For G=2, S=B: (False or False) or True = True
            elif (G == 3 or G == 4) or S == 'B':
                print("The fee is 200")
            
            # Rule 3: Grade 5 AND Section A = Fee 300
            elif G == 5 and S == 'A':
                print("The fee is 300")
            
            # Fallback case (though logically unreachable in this scenario)
            else:
                print("No Fees")
        
        # INPUT VALIDATION ERROR MESSAGE
        else:
            print("Enter Valid grade(1-5) and section(A and B).")
    
    except ValueError:
        print("Please enter a valid integer for grade.")

# ============================================================================
# TERNARY OPERATOR CONCEPTS
# ============================================================================

print("TERNARY OPERATOR EXAMPLES")

# BASIC TERNARY OPERATOR SYNTAX
# Syntax: variable = value_if_true if condition else value_if_false
# This is a shorthand for simple if-else statements

# Example 1: String comparison with multiple conditions
identity = input("Enter your Name: ")
name = "Adarsh" if (identity == "Adarsh" or identity == "adarsh") else "Unknown"
print(f"Identified as: {name}")

# IMPORTANT NOTE: Avoid using print() in ternary operator's else clause
# Better approach:
identity2 = input("Enter your Name again: ")
if identity2.lower() == "adarsh":
    name2 = "Adarsh"
    print(f"Welcome, {name2}!")
else:
    print("Enter the valid name")

# Example 2: Single-line conditional print
food = input("Enter your food: ")
print("Yes" if food in ["jalebi", "cake"] else "No")

# ============================================================================
# CLEVER TERNARY USING TUPLE INDEXING
# ============================================================================

# ADVANCED TECHNIQUE: Using boolean as index
# Syntax: variable = (false_value, true_value)[condition]
# How it works: False = 0 (index 0), True = 1 (index 1)

age = int(input("Enter your age: "))
vote = ("Cannot Vote", "Can Vote")[age >= 18]  # Fixed logic: >= 18, not > 18
print(f"Voting Status: {vote}")

# Alternative readable version:
vote_status = "Eligible" if age >= 18 else "Not Eligible"
print(f"Above 18: {vote_status}")

# ============================================================================
# KEY REVISION POINTS
# ============================================================================

"""
IMPORTANT CONCEPTS TO REMEMBER:

1. ASSERT STATEMENT:
   - Used for debugging and testing assumptions
   - Should NOT be used for user input validation in production
   - Can be disabled with -O flag in Python
   - Syntax: assert condition, "optional_message"

2. LOGICAL OPERATORS PRECEDENCE:
   - NOT has highest precedence
   - AND comes next
   - OR has lowest precedence
   - Use parentheses for clarity

3. TERNARY OPERATOR:
   - Shorthand for simple if-else
   - Format: value_if_true if condition else value_if_false
   - Keep it simple - complex logic should use regular if-else

4. TUPLE INDEXING TRICK:
   - (false_val, true_val)[boolean_condition]
   - Works because False=0, True=1
   - Less readable than regular ternary

5. INPUT VALIDATION:
   - Always validate user inputs
   - Use try-except for type conversion
   - Provide clear error messages

6. CODE READABILITY:
   - Use meaningful variable names
   - Add comments for complex logic
   - Break down complex conditions
"""

# ============================================================================
# ENHANCED VERSION WITH ASSERT DEBUGGING
# ============================================================================

def library_fee_with_assert():
    """Enhanced version using assert for debugging"""
    try:
        grade = int(input("Enter Grade (1-5): "))
        section = input("Enter Section (A/B): ").upper()
        
        # Assert statements for debugging (remove in production)
        assert isinstance(grade, int), "Grade must be an integer"
        assert 1 <= grade <= 5, f"Invalid grade: {grade}. Must be 1-5"
        assert section in ['A', 'B'], f"Invalid section: {section}. Must be A or B"
        
        # Fee calculation logic
        if (grade in [1, 2]) and section == 'A':
            fee = 100
        elif (grade in [3, 4]) or section == 'B':
            fee = 200
        elif grade == 5 and section == 'A':
            fee = 300
        else:
            fee = 0
        
        # Output with assertion check
        assert fee >= 0, "Fee cannot be negative"
        
        if fee > 0:
            print(f"Library fee: {fee}")
        else:
            print("No fee required")
            
    except (ValueError, AssertionError) as e:
        print(f"Error: {e}")

# Uncomment to run the enhanced version
# library_fee_with_assert()
