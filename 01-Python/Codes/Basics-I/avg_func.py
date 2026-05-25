def avg(a,b,c):
    sum=a+b+c
    return sum/3

print(avg(3,3,3))

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    return fact
n=  int(input("Enter no:"))  
print(fact(n))