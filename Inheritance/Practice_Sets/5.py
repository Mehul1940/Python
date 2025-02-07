# write a class vector reperesenting n dimension overload the + and * operators which calculates the sum and the dot product. 

class Vector:
    def __init__(self, *args):
        self.components = args
    
    def __add__(self, other):
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, other):
        return Vector(*[a * other for a in self.components])
    
    def __str__(self):
        return f"Vector({self.components})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 * 5)