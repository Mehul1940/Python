# Sum of natural Numbers
num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print("Sum of natural numbers up to",num,"is",sum)