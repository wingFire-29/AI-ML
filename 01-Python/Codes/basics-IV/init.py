class Student:                                          #making of class
    def __init__(self):
        print("Constructor is called///")               # default constructor
    
    def __init__(self,name,cgpa):                       #parameterized constructor ,"self" is a object createion
        print("Constructor is called...")               #constructor object value assigninng
        self.name=name
        self.cgpa=cgpa
    # def get_cgpa(self):                                 # anotherr method to get cgpa
    #     return self.cgpa

stu1=Student("Rahul",9.0)
stu2=Student("Urvashi",8.9)
stu3=Student("Parag",9.2)

# print(stu1.name)
# print(stu2.name)
# print(stu3.name)
print(f"{stu3.name} has cgpa={stu3.cgpa}")


'''
but in python we cant call multiple constructor in a single class but it isallowed in otyher languages

'''