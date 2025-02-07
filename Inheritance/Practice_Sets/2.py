# crete a class pet from a class animals and furthur create class dog from pets add method bark in the class dog 

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"{self.name} makes a sound.")
    
    def info(self):
        print(f"{self.name} is {self.age} years old.")

class Pet(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def info(self):
        super().info()
        print(f"Breed: {self.breed}")
    
    def speak(self):
        super().speak()

class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, breed)
        self.color = color
    
    def info(self):
        super().info()
        print(f"Color: {self.color}")
    def bark(self):
        print(f"{self.name} barks.")

dog = Dog("Buddy", 3, "Labrador", "Brown")
dog.info()
dog.speak()
dog.bark()