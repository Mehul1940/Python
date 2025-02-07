# store the multiplication table values in a table.txt 

# Get user input
num = int(input("Enter a number: "))

# Generate multiplication table and store in a list
multiplication_table = [num * i for i in range(1, 11)]

# Print the multiplication table list
print("Multiplication Table for", num, ":", multiplication_table)

# store the multiplication table values in a table.txt 
with open("table.txt", "w") as f:
    for i in multiplication_table:
        f.write(str(i) + "\n")