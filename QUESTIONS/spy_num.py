# Question:
# Write a Python program to find and print all "Spy Numbers", between two given numbers L and R (inclusive).
# A Spy Number is a number where the sum of its digits is equal to the product of its digits.

L = int(input("Enter L: "))
R = int(input("Enter R: "))
sum1 = 0
prod = 1
while L <= R:
    sum1 = 0
    prod = 1
    i = L
    while i != 0:
        rem = i % 10
        sum1 += rem
        prod *= rem
        i //= 10
    if(sum1 == prod):
        print(L)
    L += 1
