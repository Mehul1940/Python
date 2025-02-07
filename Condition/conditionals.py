# Condition In Python

# if condition:
#     do something
# else:
#     do something else

a=int(input("Enter Your Age:"))

# if elsif else  ladder

if a>=3 and a<=10:
    print("You are a Child") 
elif a<=17  and a>=10:
    print("You are a Teenager")
elif a<=65 and a>=18:
    print("You are an Adult")
elif a>65:
    print("You are a Senior Citizen") 
else:
    print("You are a Baby")


# Ternary Operator
c=5
d=10
print(c if c>d else d)  # 10

# Nested If
a=int(input("Enter Your Age:"))
if a>=3 and a<=10:
    print("You are a Child") 
else:
    if a<=17  and a>=10:
        print("You are a Teenager")
    else:
        if a<=65 and a>=18:
            print("You are an Adult")
        else:
            if a>65:
                print("You are a Senior Citizen") 
            else:
                print("You are a Baby")

# Even And Odd
a=int(input("Enter Your Number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")

