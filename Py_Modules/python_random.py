r"""
======================================================================
📘 PYTHON RANDOM MODULE: CONCEPTS, USAGE & BEST PRACTICES
======================================================================

--------------------------------------------------------------------------------
🚨 SECURITY WARNING!
--------------------------------------------------------------------------------
* Do NOT use the `random` module for security or cryptography purposes.
* Always use the `secrets` module for generating secure random numbers/tokens.

--------------------------------------------------------------------------------
🔎 OVERVIEW
--------------------------------------------------------------------------------
* The `random` module provides PSEUDO-random number generators based on deterministic algorithms (not truly random).
* Useful for:
    - Simulations (dice, games, etc.)
    - Random selection/shuffling
    - Generating test data or for reproducibility in experiments

--------------------------------------------------------------------------------
📚 COMMON FUNCTIONS IN THE RANDOM MODULE
--------------------------------------------------------------------------------

1. random.random()
    - Returns a random float in the range [0.0, 1.0)
2. random.randint(a, b)
    - Returns a random integer N such that a <= N <= b (inclusive)
3. random.randrange(start, stop[, step])
    - Returns a random integer from range(start, stop, step) (stop EXCLUSIVE)
    - Useful for picking random even/odd numbers within a range
4. random.uniform(a, b)
    - Returns a random float N in the range [a, b] (inclusive)
5. random.choice(seq)
    - Returns a random element from a non-empty sequence
6. random.choices(seq, k=1, weights=None)
    - Returns a list of k elements, **with replacement**; items can repeat
    - weights/ cum_weights allow to bias selection
7. random.sample(population, k)
    - Returns k UNIQUE elements from a population, **without replacement**
    - population can be a sequence (no repeats in result)
8. random.shuffle(seq)
    - Shuffles the list/object *in place*, does not return a new list

--------------------------------------------------------------------------------
🔄 DIFFERENCE BETWEEN sample() AND choices()
--------------------------------------------------------------------------------
* sample(): Sampling WITHOUT replacement. All items are unique.
* choices(): Sampling WITH replacement. Duplicates are possible.

--------------------------------------------------------------------------------
🗝️ SEEDING THE RANDOM GENERATOR
--------------------------------------------------------------------------------
* random.seed(n)
    - Sets the initial state of the random number generator
    - Using the SAME seed will always produce the SAME results (essential for reproducible results/testing)

--------------------------------------------------------------------------------
⚠️ ADDITIONAL NOTES
--------------------------------------------------------------------------------
* random module functions may raise ValueError if parameters are invalid (e.g., k > len(population) for sample()).
* random.choice/choices/sample work for lists, tuples, strings, but not for sets or dictionaries directly.

--------------------------------------------------------------------------------
🔗 EXTENDED FUNCTIONALITY (Python 3.8+ and 3.9+)
--------------------------------------------------------------------------------
* random.sample() with `counts` parameter (Python 3.9+)
    - Allows memory-efficient sampling from a weighted population
* random.shuffle() can accept a `random` callable (Python 3.9+)
* random.getrandbits(k)
    - Returns a Python integer with k random bits.
    - For generating random binary data, e.g., random.getrandbits(8) for random byte.

======================================================================
🎯 COMMON PITFALLS & TIPS
======================================================================

- Don'print()
t use random with sets or dicts directly (convert to list first).
- Don't assume random numbers are unpredictable on every system—NEVER use for cryptographic/security needs.
- For cryptographically secure tokens/passwords, use secrets module:
    e.g., import secrets; secrets.token_hex(16)
- Prefer using random.sample() for unique picks; use choices() when repeats are okay.
- Always check the Python version if using advanced sampling features (`counts` parameter, etc).

======================================================================
"""

# =============== RUNNABLE USAGE EXAMPLES BELOW =================

import random

# 1. Get a random float between 0.0 and 1.0
random_value = random.random()
print("Random float between 0.0 and 1.0:", random_value)
print()

# 2. Get a random integer between 1 and 10 (inclusive)
random_int = random.randint(1, 10)
print("Random integer between 1 and 10:", random_int)
print()

# 3. Get a random float between two numbers
random_float = random.uniform(1, 10)
print("Random float between 1 and 10:", random_float)
print()

# 4. Generate multiple random integers (list comprehension)
random_list = [random.randint(1, 10) for _ in range(10)]
print("List of 10 random integers between 1 and 10:", random_list)
print()

# 5. Random integer using range constraints
random_even = random.randrange(0, 101, 2)
print("Random even number between 0 and 100:", random_even)
print()

# 6. Random selection from a list/tuple/string
elements = ['apple', 'banana', 'cherry']
random_elem = random.choice(elements)
print("Random element from list:", random_elem)
print()

# 7. Multiple random picks with possible repeats (with replacement)
random_colors = random.choices(['red', 'blue', 'green'], k=5)
print("Random colors (with replacement):", random_colors)
print()

# 8. Weighted random picks (greater chance to pick higher-weighted items)
weights = [0.6, 0.3, 0.1]
weighted_random = random.choices(['X', 'Y', 'Z'], weights=weights, k=10)
print("Weighted random pick (with replacement):", weighted_random)
print()

# 9. Unique random picks, no repeats (without replacement)
deck = list(range(1, 53))
hand = random.sample(deck, 5)
print("A hand of 5 unique cards from deck:", hand)
print()

# 10. Shuffle a list in-place
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled list:", cards)

# 11. Efficient large weighted sampling using `counts` (Python 3.9+)
item_types = ['common', 'rare', 'legendary']
item_counts = [100, 10, 2]
loot = random.sample(item_types, k=3, counts=item_counts)
print("Sampled loot with counts:", loot)
print()

# 12. Generating random bits (e.g., for use in binary protocols)
rand_byte = random.getrandbits(8)
print("Random 8-bit integer:", rand_byte)
print()

# 13. Set the seed for reproducible results in random operations
random.seed(42)
print("Random float with seed 42:", random.random())  # Will always produce same output for seed 42
print()
