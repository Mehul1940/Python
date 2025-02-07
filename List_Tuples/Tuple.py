# Tuples are similar to lists but immutable (cannot be changed).
# Tuples are written with round brackets ().
# Tuples are ordered and allow duplicate items.
# A tuple with a single item requires a comma after the value.

# Simple Tuple
tuple1 = ("Apple", "Banana", "Cherry", 5, 6.7, True)
tuple2 = (5,)  # Corrected: Single-item tuple must have a comma
print(tuple1)
print(tuple2)

# Tuple Concatenation
tuple3 = tuple1 + tuple2
print(tuple3)

# Tuple Repetition
tuple4 = tuple1 * 3
print(tuple4)

# Empty Tuple
tuple6 = tuple()
print(tuple6)

# Tuple with a single item (Corrected)
tuple7 = ("Hello World",)  # Now it's a single-item tuple
print(tuple7)

# Tuple from range()
tuple8 = tuple(range(10))
print(tuple8)

# Tuple from a list
tuple9 = tuple([1, 2, 3])
print(tuple9)

# Tuple from a set (Order is not guaranteed)
tuple10 = tuple({1, 2, 3})
print(tuple10)

# Tuple from a dictionary (Only keys are taken)
tuple11 = tuple({1: "One", 2: "Two"})
print(tuple11)

# Correct way to access dictionary values:
dict1 = {1: "One", 2: "Two"}
tuple12 = tuple(dict1.items())  # Converts key-value pairs to tuples
print(tuple12)
print(tuple12[1])  # Now correctly returns (2, "Two")
