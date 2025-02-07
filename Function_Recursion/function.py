def add(a, b):
    return a + b

print(add(3, 4))

def sub(a, b):
    return a - b

print(sub(3, 4))

def mul(a, b):
    return a * b

print(mul(3, 4))

def div(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

print(div(3, 4))

def mod(a, b):
    return a % b

print(mod(3, 4))

def power(a, b):
    return a ** b

print(power(3, 4))

def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a-1)

print(fact(4))

def fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibo(a-1) + fibo(a-2)

print(fibo(4))

def prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

print(prime(4))

def armstrong(a):
    num_str = str(a)
    return a == sum(int(digit) ** len(num_str) for digit in num_str)

print(armstrong(153))
print(armstrong(4))

def palindrome(a):
    a = str(a)  # Convert to string to handle both numbers and strings
    return a == a[::-1]

print(palindrome("madam"))
print(palindrome(121))

def avg(a):
    return sum(a) / len(a) if len(a) > 0 else "List is empty"

print(avg([1, 2, 3, 4, 5]))
print(avg([]))  # Edge case for an empty list
