'''
Docstring for inherit2
there are three types of inheritance
single level inheritance
multi-level inheritance
multiple inheritance-shown in this code below

'''

class Teacher:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,gpa):
        self.gpa=gpa        

class TA(Teacher,Student):
    def __init__(self, salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name=name
ta1=TA(15_00_000,9.3,"Parag")        
print(ta1.name,ta1.gpa,ta1.salary)