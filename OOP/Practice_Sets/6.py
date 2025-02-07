# Can you change the self parameter inside a class and see the effect?

class Calculator:
    def __init__(slf,a):
        slf.a = a

    def square(slf):
        return slf.a*slf.a    

c = Calculator(4)
print(c.square())

class Calculator:
    def __init__(Mehul,a):
        Mehul.a = a

    def square(Mehul):
        return Mehul.a*Mehul.a    

c = Calculator(4)
print(c.square())