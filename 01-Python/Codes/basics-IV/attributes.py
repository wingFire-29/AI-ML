class Student:    
        college_name = "ABC college" #class// basically made for global values that will be common for all the objects

        def __init__ (self, name, gpa):
            self. name= name #instance
            self.gpa=gpa


stu1=Student("Rahul",9.0)

print(Student.college_name)