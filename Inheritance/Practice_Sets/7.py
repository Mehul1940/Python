# create a len method for vector

class Vector:
    def __init__(self, x, y, z):
        self.components = (x, y, z)

    def __len__(self):
        return len(self.components)

v = Vector(1, 2, 3)
print(len(v))

