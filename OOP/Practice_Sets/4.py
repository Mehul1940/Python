# add a static variable to the Calculator Class to greet the user

class Calculator:
    def __init__(self,a):
        self.a = a
    def square(self):
        return self.a*self.a
    def cube(self):
        return self.a*self.a*self.a
    def square_root(self):
        return self.a**0.5
    @staticmethod
    def greet():
        print("Good Morning")

c = Calculator(4)
print(c.square())
print(c.cube())
print(c.square_root())
Calculator.greet()