#1 Write a program that asks the user for their name and age , then prints a sentence like:
Name=(input("Enter your Name:"))
age=int(input("Enter your age:"))
print("Hiah",Name,"you are",age,"yrs old")


#2 Take two numbers as input from the user and print their.sum,difference,product,and quotient
Num1=int(input("Enter 1st num:"))
Num2=int(input("Enter 2nd num:"))
sum=int(Num1+Num2)
print(sum)
diff=int(Num1-Num2)
print(diff)
prod=int(Num1*Num2)
print(prod)
div=int(Num1/Num2)
print(div)

# 3
Num1=int(input("Enter 1st num:"))
Num2=int(input("Enter 2nd num:"))
Num3=float(input("Enter 3rd num:"))

Num1=float(Num1)
Num2=float(Num2)

avg=float(Num1+Num2+Num3)/3
print(avg)



#4
str_num=input("Enter a num:")
con_int=int(str_num)
print(con_int)
con_flo=float(con_int)
print(con_flo)
str=str(con_flo)
print(str)

#5
x =10+3*2**2
print(x)

#6
a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
print("Before Swapping")
print(a)
print(b)
c=a
a=b
b=c
print("After Swapping")
print(a)
print(b)


#7
c_temp=float(input("Enter Temp in celsius:"))
f_temp=(c_temp*(9/5)+32)
print(f_temp)

#8
rad=int(input("Enter Radius:"))
Area=3.14*(rad**2)
print(Area)

#9
P=float(input("Enter principal:"))
R=float(input("Enter Rate:"))
T=float(input("Enter Time:"))
SI=(P*R*T)/100
print(SI)


#10
a=float(input("Enter 1st num:"))
num=int(a)
dec=a-num
print(num)
print(dec)

