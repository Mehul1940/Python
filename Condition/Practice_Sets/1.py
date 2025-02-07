# Gretest of Four Numbers Entered By User

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
d=int(input("Enter Fourth Number:"))

if a>=b and a>=c and a>=d:
    print("Gretest Number is: A Which is",a)
elif b>=a and b>=c and b>=d:
    print("Gretest Number is: B Which is",b)
elif c>=a and c>=b and c>=d:
    print("Gretest Number is: C Which is",c)
else:
    print("Gretest Number is: D Which is",d)