# Does Directly use the object.a  changes the value of a.

class a:
    def __init__(self,a):
        self.a = a
    def square(self):
        return self.a*self.a
a1 = a(4)
a1.a=0
print(a1.square())
print(a1.a)


# the Answer is 0 so it changes the value of a.