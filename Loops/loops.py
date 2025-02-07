# Loops in Python

# While Loop
i = 1
while i <= 10:
    print("Using While Loop",i)
    i += 1

print("-------------")

# Do While Loop
i = 1
while True:
    print("Using Do While Loop",i)
    if i == 10:
        break
    i += 1

print("-------------")

# For Loop
for i in range(1, 11):
    print("Using For Loop",i)
else:
    print("Loop is done")

print("-------------")

# For Each Loop
list = [1, 2, 3, 4, 5]
for i in list:
    print("Using For Each Loop",i)

print("-------------")

# Break and Continue and pass
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print("Using While Loop and Break",i)

print("-------------")

i = 0
while i < 10:
    i += 1
    if i == 6:
        continue
    print("Using While Loop and Continue",i)

print("-------------")

for i in range(1, 10):
    pass

print("-------------")

# Range
for i in range(1, 10):
    print("Using Range",i)

print("-------------")

# Enumerate
list = [1, 2, 3, 4, 5]
for i in enumerate(list): 
    print("Using Enumerate",i)

print("-------------")

# Zip
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
for i in zip(list1, list2):
    print("Using Zip",i)

print("-------------")

# Comprehensions
list = [1, 2, 3, 4, 5]
new_list = [i * 2 for i in list]
print("Using Comprehensions",new_list)

print("-------------")
