'''
The process in which a function calls itself directly or indirectly is called recursion.
The corresponding function is called as recursive function.
Using recursive algorithm problem, certain problems can be solved easily.

In recursion, there will be base cases. In base cases. 
In base cases for certain inputs, outputs will remain known to us.

Advantages of Recursion:

Recursive functions make the code look clean and elegant.
A complex task can be broken down into simpler sub-problems using recursion.
Sequence generation is easier with recursion than using some nested iteration.

Disadvantages of Recursion:

Sometimes the logic behind recursion is hard to follow through.
Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
Recursive functions are re hard to debug.
'''

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print("Factorial of 5 is", fact(5))