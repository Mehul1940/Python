# Exception Handling In Python

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as e:
    print("Something went wrong", e)


# Using Else Block and Finally Block

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Everything is fine", x / y)
finally:
    print("Finally")