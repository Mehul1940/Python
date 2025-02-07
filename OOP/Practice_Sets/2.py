# Calculator Class That finds Square , Cube and Square Root

class Calculator:
    def __init__(self,a):
        self.a = a
    def square(self):
        return self.a*self.a
    def cube(self):
        return self.a*self.a*self.a
    def square_root(self):
        return self.a**0.5

c = Calculator(4)
print(c.square())
print(c.cube())
print(c.square_root())