class Employee:
    start_time="10am"
    end_time="6pm"

class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject
class Admin(Employee):
    def __init__(self,role):
        self.role=role

t1=Teacher("Math")        
st1= Admin("Manager")
print(t1.subject,t1.start_time,t1.end_time)
print(st1.role,st1.start_time,st1.end_time)