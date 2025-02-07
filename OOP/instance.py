# Instance vs class attributes in python

class Emp: # A class Without Constructor
    name = "Mehul"
    sal = 50000
    language = "Python"

    def info(self):
        print(f"My Name is : {self.name}\nMy current Salary is : {self.sal}\nWhile Working on the Language of : {self.language}")

emp = Emp()
emp.language="Java" # this will change the language of the emp object because it is an instance attribute
emp.info()