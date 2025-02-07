# write a class complex to reperesent complex number along overload operators + and * which adds and multiplies two complex numbers respectively  

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
c3 = c1 + c2
c4 = c1 * c2
print(c3)
print(c4)