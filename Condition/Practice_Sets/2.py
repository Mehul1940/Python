# Marks Taken For Each Subject By Users
Java = int(input("Enter Java Marks: "))
Python = int(input("Enter Python Marks: "))
C = int(input("Enter C Marks: "))

# Calculate Percentage
percentage = (Java + Python + C) / 3

print("Total Percentage is:", percentage)

# Pass/Fail Condition
if Java >= 33 and Python >= 33 and C >= 33:
    print("You are Pass")
else:
    print("You are Fail")
