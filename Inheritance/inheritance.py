# Inheritance In Python

# Inheritance is a way of creating new classes from existing classes.
# The new class has all the variables and functions of the existing class.
# The new class is called the derived class, the existing class is called the base class.
# The derived class can have new variables and functions, and override the base class variables and functions.
# The base class is not modified.
# The derived class can be used where the base class is used.

# Single Inheritance using super()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def greet(self):
        super().greet()
        print(f"I am studying {self.course}.")

s = Student("John", 20, "Computer Science")
s.greet()

# Multiple Inheritance using super()

class Animal:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        print(f"{self.sound} makes a sound.")

class Owner:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Dog(Animal, Owner):
    def __init__(self, name,sound):
        Animal.__init__(self, sound)
        Owner.__init__(self, name)
    def info(self):
        print(f"Hello, {self.name} Your dog is so cute when he say like {self.sound}.")


d = Dog("Mehul","Woof")
d.info()

# Multilevel Inheritance

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.make} {self.model} (Year: {self.year})")

class Truck(Vehicle):
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Load Capacity: {self.load_capacity}")

class Car(Truck):
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year, load_capacity)

    def display_info(self):
        super().display_info()
        print(f"Load Capacity: {self.load_capacity}")
        
c = Car("Toyota", "Corolla", 2020, 1000)    
c.display_info()

# class method 

# class method can be used to create new objects from existing objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    @classmethod
    def create_from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)
        
p = Person.create_from_birth_year("Mehul", 2005)
p.greet()

# static method can be used to create new objects from existing objects.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def greet(name, age):
        print(f"Hello, my name is {name} and I am {age} years old.")
    

Person.greet("Mehul", 20)
