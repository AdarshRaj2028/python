"""
Iterators in Python
-------------------

Iterators are objects that allow you to traverse through all the elements of a collection, one element at a time. 
They are commonly used in for loops, comprehensions, and generators, often hidden in plain sight.

Key Concepts:
-------------
- An **iterator** is an object that implements two special methods: `__iter__()` and `__next__()`, collectively known as the iterator protocol.
- An **iterable** is any object from which you can obtain an iterator (e.g., lists, tuples, strings).
- The `iter()` function returns an iterator from an iterable by calling its `__iter__()` method.
- The `__next__()` method returns the next item in the sequence. When there are no more items, it raises a `StopIteration` exception.
- **Generators** provide a quick way to create iterators using functions and the `yield` statement.
- Custom iterator classes offer more control and flexibility, but require more code.

Why Iterators Are Essential:
----------------------------
1. **Memory Efficiency**
    - Generate values one at a time (lazy evaluation)
    - Avoid storing entire datasets in memory
    - Handle massive datasets efficiently

2. **Infinite/Unknown Size Data**
    - Process infinite sequences
    - Handle data streams of unknown size
    - Not possible with traditional lists/indexing

3. **Advanced Control**
    - Pause and resume iteration
    - Conditionally skip elements
    - Save iteration state
    - Fine-grained control over the iteration process

4. **Performance Benefits**
    - Faster for large datasets
    - Enable stream processing
    - No need to pre-generate entire datasets

5. **Compatibility**
    - Work with non-indexable objects (e.g., sets, dictionaries)
    - Seamless integration with Python built-ins
    - Provide abstraction and encapsulation

Iterator Protocol:
------------------
- `__iter__()`: Returns the iterator object (usually `self`)
- `__next__()`: Returns the next item or raises `StopIteration`
- Enables use with `for` loops, `next()`, and `iter()`
"""
our_list = [44, 77, 11, 33]

# Get an iterator using iter() method
our_iter = iter(our_list)

# Iterate through it using next() method

print(next(our_iter)) # Prints 44
print(next(our_iter)) # Prints 77

# next(obj) is same as calling obj.__next__() method
print(our_iter.__next__()) # Prints 11

print(next(our_iter)) # Prints 33

# print(next(our_iter)) # This will raise an error like StopIteration

# Creating a custom iterator
class pow_of_two:
    '''Class to implement an iterator of power of two''' # This also known as doc, SYNTAX: class_name.__doc__ to print this.

    def __init__(self, max = 0):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

print(pow_of_two.__doc__)
a = pow_of_two(4)
i = iter(a)
print(next(i))
print(next(i))
print(i.__next__()) # Same as the next(i)
print(next(i))
print(next(i))

# Creating an infinite custom iterator
class infinite_iterator:
    '''Infinite iterator to return all even number'''

    def __iter__(self):
        self.num = -2
        return self

    def __next__(self):
        # num = self.num
        self.num += 2 
        return self.num # or we can also return num, but for that we have to store self.num in it(Above comment).

print(infinite_iterator.__doc__)
a2 = infinite_iterator()
i2 = iter(a2)
print(next(i2))
print(i2.__next__()) # Same as next(), just for practicing
print(next(i2))
print(next(i2))


