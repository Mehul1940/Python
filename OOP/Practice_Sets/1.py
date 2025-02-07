# Information about 5 programmers working at Microsoft

class Programmer:
    def __init__(self,name,company,language,sal):
        self.name=name
        self.company=company
        self.language=language
        self.sal=sal
    def info(self):
        print(f"Name : {self.name}\nCompany : {self.company}\nLanguage : {self.language}\nSalary : {self.sal}")


p1=Programmer("Mehul","Microsoft","Python",50000)
p2=Programmer("Chirag","Microsoft","Java",50000)
p3=Programmer("Rohan","Microsoft","Javascript",50000)
p4=Programmer("Sujal","Microsoft","Ruby",50000)
p5=Programmer("Harsh","Microsoft","C++",50000)

l=[p1,p2,p3,p4,p5]
for i in l:
    i.info()