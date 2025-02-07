# Creating a set (Duplicate "apple" is ignored)
thisset = {"apple", "banana", "cherry", "apple"}
print("Original set:", thisset)  # Output: {'apple', 'banana', 'cherry'}

# Adding an item to the set
thisset.add("orange")
print("After adding 'orange':", thisset)

# Removing an item using remove() (Raises error if item doesn't exist)
thisset.remove("banana")
print("After removing 'banana':", thisset)

# Removing an item using discard() (No error if item doesn't exist)
thisset.discard("cherry")
print("After discarding 'cherry':", thisset)

# Clearing the set (Removing all elements)
thisset.clear()
print("After clearing the set:", thisset)  # Output: set()

# Creating two new sets
set1 = {"a", "b", "c"}
set2 = {"a", "b", "c", 1, 2, 3}
print("Set1:", set1)
print("Set2:", set2)

# Copying a set
set3 = set1.copy()
print("Copy of set1:", set3)

# Updating set1 by adding elements from set2 (Modifies set1)
set1.update(set2)
print("After updating set1 with set2:", set1)

# Keeping only items found in both sets (Intersection Update - modifies set1)
set1.intersection_update(set2)
print("After intersection_update:", set1)

# Keeping only elements that are in one of the sets, but not both (Symmetric Difference Update - modifies set1)
set1.symmetric_difference_update(set2)
print("After symmetric_difference_update:", set1)

# Checking if set1 is a subset of set2 (Returns True or False)
print("Is set1 a subset of set2?", set1.issubset(set2))

# Checking if set1 is a superset of set2 (Returns True or False)
print("Is set1 a superset of set2?", set1.issuperset(set2))

# Checking if set1 and set2 have no common elements (Returns True or False)
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))

# Creating a union (Combining both sets but not modifying the original sets)
set_union = set1.union(set2)
print("Union of set1 and set2:", set_union)

# Creating an intersection (Common elements of both sets without modifying original sets)
set_intersection = set1.intersection(set2)
print("Intersection of set1 and set2:", set_intersection)

# Creating a symmetric difference (Elements that are in either set but not in both)
set_sym_diff = set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", set_sym_diff)

# Creating a difference (Elements in set1 but not in set2)
set_difference = set1.difference(set2)
print("Difference (set1 - set2):", set_difference)

# Modifying set1 by removing elements found in set2
set1.difference_update(set2)
print("After difference_update (set1 - set2):", set1)

# Final Boolean Checks
print("Are set1 and set2 disjoint after difference_update?", set1.isdisjoint(set2))
print("Is set1 a subset of set2 after difference_update?", set1.issubset(set2))
print("Is set1 a superset of set2 after difference_update?", set1.issuperset(set2))