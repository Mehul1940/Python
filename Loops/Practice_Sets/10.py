# Reverse Multiplication Table of a Given Number

num = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(num,"x",i,"=",num*i)