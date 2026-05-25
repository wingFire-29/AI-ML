squares=[]

for i in range(6):
    squares.append(i*i)
print(squares)


'''
simple way to this is top use a list comprehenson
'''
sq=[i*i for i in range(6) if i%2!=0]
print(sq)

nums=[-1,-8,10,7,-2,3]
nums=[0 if val < 0 else val for val in nums]
print(nums)

words=["hello","python","parag"]
words=[val.upper() for val in words]
print(words)