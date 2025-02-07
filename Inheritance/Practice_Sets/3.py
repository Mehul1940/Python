# create a class employee and add salary and increment properties to it. 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self, rate):
        self.salary += (self.salary * rate)

    def info(self):
        print(f"Employee name: {self.name}, Salary: {self.salary}")

emp1 = Employee("John", 50000)
emp1.increment(0.1)
emp1.info()