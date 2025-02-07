# Walrus In Python

# Walrus operator is a new assignment expression introduced in Python 3.8.
# It allows you to assign values to variables based on the result of an expression.

# Using Walrus Operator

x = 0
while (x := x + 1) < 10:  
    print(x)

print(x)

