# self parameter is a reference to the current instance of the class. It is used to access variables that belongs to the class.
class Emp: 
    name = "Mehul"
    sal = 50000
    language = "Python"

    def info(self): # using self we can access the attributes of the class
        print(f"My Name is : {self.name}\nMy current Salary is : {self.sal}\nWhile Working on the Language of : {self.language}")

emp = Emp()
emp.info()

# Greet Class

class greet:
    name="Mehul"
    @staticmethod # staticmethod use when we don't need to access the attributes of the class and just want to greet the user using class name
    def greeting(self):
        print(f"Good Morning {self.name}")

greet.greeting(greet)
