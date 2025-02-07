# ***
# * *
# ***

size = 3  # Number of rows

for i in range(size):
    if i == 0 or i == size - 1:  
        print("*" * size)  # Print full row of stars for first & last row
    else:
        print("*" + " " * (size - 2) + "*")  # Print '*' with spaces in between
