'''
Q5•
Create a dictionary where:
Keys=student names
Values=marks(integer)
Write a menu-based program where user presses a key ('A','B','C','D')
depending on the operation they want to perform on the dictionary:
A- Add a student
B - Update marks
C- Search for a student
D- Display all students and marks
'''

student={}

while True:
    choice=input("What operation u want to do:\nA- Add a student\nB - Update marks\nC- Search for a student\nD- Display all students and \nPress 'E' for exit\n")
    if choice=='A':
        key=input("Tell the student name:")
        value=input("Tell the student marks:")
        if key in student:
            print("Student already exist!!\n")
        else:
            student[key]=value
            print(student)
            print("Student added successfully!!\n")            
    
    elif choice=='B':
        print(student.keys())
        key=input("Which student marks u want to update:")
        
        if key in student:            
            marks=input("Enter marks:")
            student[key]=marks
            print("Marks updated!!\n")
        else:
            print("Student not found press 'A' to add this student\n")            
        
    elif choice =="C":
        key=input("Which student u want to search:")
        if key in student:
            print(f"marks of {key} is {student[key]}\n")
        else:
            print("No such student found press 'A' to add this student\n")            
        
    elif choice=="D":
        for key,value in student.items():
            print(key,':',value)
            print() 
    else:
        break    
