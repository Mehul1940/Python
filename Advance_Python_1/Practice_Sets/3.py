# write a comprehension to print a list of a multiplication table values of enter user number.

# Get user input
num = int(input("Enter a number: "))

# Generate multiplication table and store in a list
multiplication_table = [num * i for i in range(1, 11)]

# Print the multiplication table list
print("Multiplication Table for", num, ":", multiplication_table)
