# Arithmetic Operators : +,-,*,/,%,**,//
# Assignment Operators :=,+=,-=,*=,/=,%=,//=,**=
# Comparison Operators : <,>,<=,>=,==,!=
# Logical Operators : and,or,not
# Identity Operators : is,is not
# Member Operators : in,not in
# Bitwise Operators : &,|,^,~,<<,>>

# Arithmetic Operators
a=10
b=20
print("Addition is:",a+b)
print("Subtraction is:",a-b)
print("Multiplication is:",a*b)
print("Division is:",a/b)
print("Modulus is:",a%b)
print("Exponentiation is:",a**b)
print("Floor Division is:",a//b)

# Assignment Operators
a=10
b=20
a = b
print("Assignment Operator (=) is:", a)
a += b
print("Addition Assignment Operator (+=) is:", a)
a -= b
print("Subtraction Assignment Operator (-=) is:", a)
a *= b
print("Multiplication Assignment Operator (*=) is:", a)
a /= b
print("Division Assignment Operator (/=) is:", a)
a %= b
print("Modulus Assignment Operator (%=) is:", a)
a **= b
print("Exponentiation Assignment Operator (**=) is:", a)
a //= b
print("Floor Division Assignment Operator (//=) is:", a)

# Comparison Operators
a=10
b=20
print("Comparison Operator (==) is:",a==b)
print("Comparison Operator (!=) is:",a!=b)
print("Comparison Operator (<) is:",a<b)
print("Comparison Operator (>) is:",a>b)
print("Comparison Operator (<=) is:",a<=b)
print("Comparison Operator (>=) is:",a>=b)

# Logical Operators
a=True
b=False
print("Logical Operator (and) is:",a and b)
print("Logical Operator (or) is:",a or b)
print("Logical Operator (not) is:",not a)

# Identity Operators
a=10
b=10
print("Identity Operator (is) is:",a is b)
print("Identity Operator (is not) is:",a is not b)

# Member Operators
a=[1,2,3,4,5]
b=5
print("Member Operator (in) is:",b in a)
print("Member Operator (not in) is:",b not in a)

# Bitwise Operators
a=10
b=20
print("Bitwise Operator (&) is:",a&b)
print("Bitwise Operator(|) is:",a|b)
print("Bitwise Operator(^) is:",a^b)
print("Bitwise Operator(~) is:",~a)
print("Bitwise Operator (<<) is:",a<<2)
print("Bitwise Operator (>>) is:",a>>2)
