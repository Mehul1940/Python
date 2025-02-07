# write a str method to print the vector as follows: 7i + 8j + 10k and assume that the vector dimension is 3

class Vector:
    def __init__(self, x, y, z):
        self.components = (x, y, z)

    def __add__(self, other):
        """Overloads + operator to add two vectors element-wise"""
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        """Overloads * operator for dot product (Vector * Vector) and scalar multiplication (Vector * Scalar)"""
        if isinstance(other, Vector):
            # Dot product: Sum of element-wise multiplication
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            # Scalar multiplication
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Vector can only be multiplied by a scalar or another Vector.")

    def __str__(self):
        """Returns the vector in the format: 7i + 8j + 10k"""
        x, y, z = self.components
        return f"{x}i + {y}j + {z}k"

# Example Usage
v1 = Vector(7, 8, 10)
v2 = Vector(1, 2, 3)

print("Vector 1:", v1)  # "7i + 8j + 10k"
print("Vector 2:", v2)  # "1i + 2j + 3k"
print("Sum:", v1 + v2)  # "8i + 10j + 13k"
print("Dot Product:", v1 * v2)  # (7*1) + (8*2) + (10*3) = 61
print("Scalar Multiplication:", v1 * 2)  # "14i + 16j + 20k"

    