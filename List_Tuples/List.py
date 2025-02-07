# Lists are used to store multiple items in a single variable.
# A list is a collection which is ordered and changeable. 
# In Python, lists are created using square brackets: []

a = ["Apple", "Banana", "Cherry", 5, 6.7, True]

# To change the value of a specific index, assign a new value to it
a[1] = "Watermelon"
print(a)

# To delete the index, use the del keyword
del a[1]
print(a)

# To add an item to the end of the list, use the append() method
a.append("Orange")
print(a)

# To add an item at a specific index, use the insert() method
a.insert(1, "Grape")
print(a)

# To remove an item, use the remove() method (only if it exists)
if "Cherry" in a:
    a.remove("Cherry")
print(a)

# To clear all items from a list, use the clear() method
a.clear()
print(a)

# To concatenate two lists, use the extend() method
list1 = ["Apple", "Banana", "Cherry"]
list2 = [5, 6.7, True]
list1.extend(list2)
print(list1)

# To copy a list, use the copy() method
list1 = ["Apple", "Banana", "Cherry"]
list2 = list1.copy()
print(list2)

# To reverse the order of a list, use the reverse() method
list1 = ["Apple", "Banana", "Cherry"]
list1.reverse()
print(list1)

# To sort a list, ensure it contains only the same type of elements
numeric_list = [5, 6.7, 1, 3, 9]
numeric_list.sort()
print(numeric_list)  # Corrected: Only numbers are sorted

string_list = ["Apple", "Cherry", "Banana"]
string_list.sort()
print(string_list)  # Sorting works for strings

# To sort in descending order
numeric_list.sort(reverse=True)
print(numeric_list)

# To count occurrences of an item in a list, use the count() method
list1 = ["Apple", "Banana", "Cherry", "Cherry", "Grape", "Grape"]
print(list1.count("Cherry"))

# To get the index position of an item, ensure it exists first
if "Cherry" in list1:
    print(list1.index("Cherry"))

# To create a list of numbers, use the range() function
list1 = list(range(10))
print(list1)

# To convert a string to a list, use the split() method
list1 = "Hello World".split()
print(list1)

# To merge two lists, use the + operator
list1 = ["Apple", "Banana", "Cherry"]
list2 = [5, 6.7, True]
list3 = list1 + list2
print(list3)

# To repeat a list multiple times, use the * operator
list1 = ["Apple", "Banana", "Cherry"]
list2 = list1 * 3 
print(list2)

# To loop through a list, use a for loop
list1 = ["Apple", "Banana", "Cherry"]
for x in list1:
    print(x)

# To loop through the index numbers of a list, use the enumerate() function
list1 = ["Apple", "Banana", "Cherry"]
for index, x in enumerate(list1):
    print(index, x)

# To check if an item exists in a list, use the in keyword
list1 = ["Apple", "Banana", "Cherry"]
if "Cherry" in list1:
    print("Cherry is present")
else:
    print("Cherry is not present")

# To remove an item from a list, use the pop() method
list1 = ["Apple", "Banana", "Cherry"]
list1.pop(1)
print(list1)
