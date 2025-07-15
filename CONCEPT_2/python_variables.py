# Global Variables - A variable which is declared outside of the function or in global scope is known as global variable. 
# Whenever the variable inside the function is to be declared global, we use the 'global' keyword.
# Outside function, it is global by default. 
# This means, global variable can be accessed inside or outside of the function.
# Local Variables - A variable which is declared inside the function's body or in the local scope is known as local variable.
# Nonlocal Variables - Nonlocal variable are used in nested function whose local scope is not defined. 
# This means, the variable can be neither in the local nor the global scope
# global keyword is necessary in any function where you assign a new value to variable for which you want to use global keyword.
# It is not needed if you only mutate (append, remove, etc.) the list.

print("Global and local variable with different name.\n")
x = 'global' # Global variable can be accessed from anywhere

def func1():
    global x
    y = 'local'
    x = x * 2
    print("Inside Function: ", x)
    print("Inside Function: ",y)

print("Global x: ", x)
func1()
print("Global x: ", x)
# print(y) , This will give error since y is a local variable and is only defined in func1.

print("Creating and using a Non-Local variable\n")

def outer():
    x = 'local'
    def inner():
        nonlocal x    # Nonlocal variable are used in nested function
        x = 'nonlocal'
        print("Inner: ", x)

    print(x) # Before calling function
    inner()
    print('Outer:', x)

outer()