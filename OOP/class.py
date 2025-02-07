# Classes In Python

# A simple class in python is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together.

# Without Constructor

class Emp: # A class Without Constructor
    name = "Mehul"
    sal = 50000
    language = "Python"

    def info(self):
        print(f"My Name is : {self.name}\nMy current Salary is : {self.sal}\nWhile Working on the Language of : {self.language}")

emp = Emp()
emp.info()

# default Constructor

class Student:
    def __init__(self): # constructor with only one argument
        self.name = "Mehul"
        self.roll = 101
        self.language = "Python"

    def info(self):
        print(f"My Name is : {self.name}\nMy current Roll no. is : {self.roll}\nAnd i love the Language : {self.language}")

stud = Student()
stud.info()

# paramitize constructor

class Employee:
    def __init__(self,name,sal,language): # constructor with more then one arguments
        self.name = name
        self.sal = sal
        self.language = language
    
    def info(self): 
        print(f"My Name is : {self.name}\nMy current Salary is : {self.sal}\nWhile Working on the Language of : {self.language}")

emp1 = Employee("Mehul",50000,"Python") # object creation
emp1.info()

