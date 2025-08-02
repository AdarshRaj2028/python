# Sets is a collection of unordered items. Sets are mutable(Their elements are immutable)
# Each elements must be unique and immutable(Like Int, float, string, tuples, boolean...), Not elements which are mutable(Like Lists, Dict)
# You can’t access elements using indexes like set[0]
# Internally, sets use hashing, which is why the order keeps changing
# Searching in sets is faster than lists (O(1) average time)
# Helpful in algorithms/DSA for checking repeated items quickly

print("Usage of some Sets method.\n")

collection = {1,2,3,5,5,5,5,5,5, "Hello", "there"} # It ignores duplicate values.
collection_1 = set() # Syntax for creating empty set

print(5 in collection)
print(5 not in collection)
collection_1.add(7) # Adds an element in the set, Whether it is int, float, string etc...
collection_1.add(1) # Takes only one agrument at a time.
collection_1.add(1) # Adding same element will be ignored.
collection_1.update([9,8,7,6,5,4]) # Adds multiple elements, lists and sets.
print(collection_1)

collection.remove(5) # Removes the specified element
print(collection)

collection.clear() # -> This clears the set

print(collection_1.pop()) # Deleted a element randomly.
print(collection_1)

# Discard and remove both methods are used to remove elements.
# But if the element that we are trying to remove is not present,
# Discard will not give any error, whereas remove will give error
collection_1.discard(10) 
# collection_1.remove(10) 

print("\nIterating through a set")
for letters in set("Adarsh"):
    print(letters)

print("\nUsage of Sets method like Union, Intersection.")

set1 = {1,2,3,4}
set2 = {3,4,5,6}
# intersection finds what's common between two sets, while difference finds what's unique to the first set.
print("\n->", set1.symmetric_difference(set2)) 
print("\n->", set2.symmetric_difference(set1)) 
print("\n->", set1.difference(set2)) 
print("\n->", set2.difference(set1)) 
print("\n->", set1.union(set2)) # They only modifies copy of the set, not the actual set.
print("\n->", set1.intersection(set2))

# Python frozenset
# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
# While tuples are immutable Lists, frozensets are immutable sets.

print("\nPython Frozenset\n")

myset1 = frozenset([1, 2, 3, 4])
myset2 = frozenset([3, 4, 5, 6])

print(myset1)
print(myset2)
print(myset1.difference(myset2))
print(myset1.union(myset2))
print(myset1.intersection(myset2))
print(myset1.symmetric_difference(myset2))
# myset1.add(10)

# Sets Comprehension
print("\n***Sets Comprehension***\n")
myset3 = {x for x in range(10) if x % 2 == 0}
print("Sets of even numbers:", myset3)

nums = [1, 1, 2, 2, 3, 3, 4, 5]
myset2 = {x ** 2 for x in nums}
print("\nSets of unique sqaures:", myset2, "\n")