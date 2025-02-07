# wtite a Program to Display where a and b are integer if b=0 display infinite by handling the ZERODIVISIONERROR Exception.

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(x / y)