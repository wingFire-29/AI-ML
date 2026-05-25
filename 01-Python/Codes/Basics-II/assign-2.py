'''
Q 1. Write a program that takes salary as input. Using conditional statements,
calculate the final tax rate based on these rules:
• If salary < 30,000 5%
• If salary is +
•v If salary > 70,000 25%


salary=int(input("Enter your salary: "))
# print(type(salary))

if(salary<30000):
    tax_rate=(5/100)*salary
    print(tax_rate)

elif(salary>=30000 and salary<70000):
    tax_rate=(15/100)*salary
    print(tax_rate)

elif(salary>=70000):
    tax_rate=(25/100)*salary
    print(tax_rate)
else:
    print("Enter salary properly")   
f_salary=salary-tax_rate
print(f_salary)     
'''
'''
Q2. Write a function that takes two integers a and
and b prints all even numbers between them (inclusive).
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

for i in range(a,b+1):
    if(i%2==0):
        print(i)
    else:
        continue        
'''
'''
Q3. Write a function that prints the digits of a number,n
For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.

def print_digits(n):
    n=str(n)
    for digits in n:
        print(digits)
num=int(input("Enter any number: "))
print_digits(num)
'''
'''
Q4. Write a function to return the count the number of digits in a number, n

def print_digits(n):
    n=str(n)
    count=0
    for digits in n:
        count=count+1
    print(count)
num=int(input("Enter any number: "))
print_digits(num)
'''
'''
Q5. Write a function to return the sum of digits of a number,n
def sum_digits(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    return total      
        
num=int(input("Enter any number: "))
print(sum_digits(num))
'''
'''
Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
def print_div():
    for i in range(1,101):
        if(i%3==0 and i%5==0):
            print(i)    
print_div()
'''
'''
Q7. Design a program to continuously input a number n
from user & print if it is positive or negative until the user enters "Quit".
         
while True:        
    n=input("Enter any number:")
    if(n=='Quit'):
        break
    else:
        n=int(n)
        if(n>0):
            print("The Number is positive")
        elif(n<0):
            print("The Number is Negative")
        else:
            print("You entered 0")
'''

'''
Q.8 create a simple calculator function
i will create it using a match case
def calculator(a,b):
    while True:        
        operation=input("Enter what operation u want to perform or Exit to exit:")
        
        if operation=='exit':
            break
        match operation:
            case '+':
                add=a+b
                print(add)
            case '-':
                sub=a-b
                print(sub)
            case '*':
                Prod=a*b
                print(Prod)                
            case '/':
                if(a>b):
                    div=a/b
                else:
                    div=b/a    
                print(div)
            case _:
                print("Invalid operation. Please enter +, -, *, / or Quit.")

a=int(input("Enter First num:"))
b=int(input("Enter Second num:"))
calculator(a,b)
'''
'''
Q9. Write a function
otherwise, using a loop.
if n is a prime number return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = int(input("Enter a number: "))
if is_prime(x):
    print(x, "is a prime number")
else:
    print(x, "is not a prime number")

'''
'''
Q1O. Let's create a "Number Guessing Game". Given a secret number (already
decided by you), write a program that asks the user to guess it and prints:
"Too high",if the guess is above the number
"Too low", if the guess is below
"Correct !", if the guess matches

correct=69
while True:
    guess=int(input("Guess the two digit number:"))
    if (correct<guess):
        print("Too high")
    elif (correct>guess):
        print("Too low")        
    else:
        print("Hooray!!! you guessed it right")
        break
'''