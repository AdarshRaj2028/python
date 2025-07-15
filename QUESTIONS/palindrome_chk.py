# Method 1 (Using list reverse)
# user = int(input("Enter the size of the list: "))
# l = []
# for i in range(user):
#     user_list = input("Enter the number: ")
#     l.append(user_list)
# print("Normal List: ", l, "\nIs it palindrome: ")
# l1 = l.copy()
# l.reverse()
# if(l1 == l):
#     print("Yes, It is palindrome.")
# else:
#     print("No, It is not palindrome.")

# Method 2 (Manual index comparison (mirror check))
user = int(input("Enter the size of the list: "))
l = []
for i in range(user):
    user_list = input("Enter the number: ")
    l.append(user_list)
print("Normal List: ", l, "\nIs it palindrome: ")
for i in range(user//2):
    if(l[i] != l[user - 1 - i]):
        break
else:
    print("Yes, It is palindrome.")
    exit()
print("No, It is not palindrome.")

# Method 3 (two-pointer method (also called the double pointer method).)
# def is_palindrome(lst):
    # left, right = 0, len(lst) - 1  # Means left = 0 and right len(lst) - 1
    # while left < right:
    #     if lst[left] != lst[right]:
    #         return False
    #     left += 1
    #     right -= 1
    # return True
 
# Method 4 (Using String slicing)
# def isPalin(s):
#     if s == s[::-1]:
#         return True
#     return False

# s=[3,4,4,3,5]
# print(isPalin(s))


# From the above, 
# Use Method 3 (Two-pointer method) for production code. It provides the best balance of:

# -> Performance: O(n) time, O(1) space
# -> Readability: Clear, self-documenting logic
# -> Efficiency: Early termination and minimal memory usage

# For quick prototyping or one-off scripts where memory isn't a concern, 
# Method 4 (String slicing) offers the most concise code, 
# but Method 3 remains superior for any serious application.