# Break : Terminates the loop when gets encountered
# If break statement id inside a mested loop(loop inside another loop), break will terminate the innermost loop.
# Continue : Terminates the current iteration, executing what is after it and moves to the correct iteration 
# range(): This function returns a sequence of numbers, starting from 0 (by default),
# increments by 1(by default), and stops before a specified number(We must need to mention). range(start?,stop,step?)
# pass statement: pass is a null statement that does nothing. It is used as a placeholder for future code.


# While loop is generally used when we don't know beforehand, the number of times to iterate
# Same as that of for loop, we can have an optional else block with while loop as well.
# A whole loop's else part runs if no break occurs and the condition is false.

print("Using for else")
i = 0
while i < 10:
   print(i)
   i += 1
else:
    print("Displayed Successfully!")

print("Using while loop to make a triangle pattern")
n = 6
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(".", end = '')
        j += 1
    j = 1
    while j <= ((2*i) - 1):
        print("*", end = "")
        j += 1
    print()
    i += 1

# Program: Print numbers divisible by 2 but not multiples of 10, up to user input (using While loop)
user = 10
i = 0

while i <= user:
    if i % 2 == 0 and i % 10 != 0:
        print(i)
    i += 1

# Prints the index of the num, provided by the list(user provided), Using For loop
s = []
init = int(input("Enter the size: "))
for i in range(init):
    user = int(input("Enter the num: "))
    s.append(user)
print(s)
user_num = int(input("Now enter the number, whose index you want to find: "))

# A for loop can also have an optional else block.
# The else part is executed when the items in the sequence used in for loop exhausts.
# A for loop's els epart runs if no break occurs.
 

# for i in range(len(s)): # You can use range(len(s)) to loop by index,
#                         # or use 'for value in s' to loop through elements.
#     if(s[i] == user_num):
#         print(i)
#         break
# else:
#     print("It's not present in the list.")
 
 # OR

for i, value in enumerate(s): # Use this method when we want both, Index(i) as Well as Value.
    if value == user_num:
        print(i)
        break
else:
    print("It's not present in the list.")

"""
Difference between return and yield:

- 'return' sends back a complete value (like a list) and ends the function immediately.
- 'yield' produces a sequence of values one at a time, pausing the function between each.
- Using 'yield' creates a generator, which is memory-efficient for large or infinite data.
- Use 'return' when you want to output a final result all at once.
- Use 'yield' when you want to generate values lazily, one by one, especially in loops.
"""

# Using return
def get_numbers_return():
    numbers = [1, 2, 3]
    return numbers  # Returns the entire list at once

print("\n\nUsing return:")
for num in get_numbers_return():
    print(num)

# Using yield
def get_numbers_yield():
    for i in range(1, 4):
        yield i  # Yields one number at a time

print("\nUsing yield:")
for num in get_numbers_yield():
    print(num)


   