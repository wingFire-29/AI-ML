

'''
Docstring for assign3
q.1)check palindrome

str=input("Enter a string to check if it is a palindrome or not:")
str_rev=str[::-1]

if (str_rev==str):
    print(f"{str} is a palindrome string equal to {str_rev}")
else:
    print(f"{str} is a not a palindrome string equal to {str_rev}")
'''

'''
q.2)given a list of integers calc average of all

num=[10,20,30,40,50]
size=len(num)
print(size)
total=0
for i in num:
    total+=i
avg=total/size
print(f"{avg} is the average of all the numbers in this list")
'''

'''
q.3)input two list and merge them and then sort them
list1=[1,3,5,7,9]
list2=[2,4,6,8]

final_list=list1+list2
final_list.sort()
print(final_list)
'''

'''
q.4)with a tuple of integers create two tuples with even and odd
t1=(1,2,3,4,5,6,7,8,9)
l2=[]
l3=[]
for i in t1:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)
t_even=tuple(l2)
t_odd=tuple(l3)

print(f"Tuple of even numbers is {t_even}")
print(f"Tuple of odd numbers is {t_odd}")
'''
'''
q.6)given a list of words 
words = ["apple", "banana", "kiwi", "cherry", "mango
create a dict that maps to each word to its len...

words = ["apple", "banana", "kiwi", "cherry", "mango"]
word_dict={}
for word in words:
    length=len(word)
    word_dict[word]=length
print(word_dict)    
'''

'''
Q7. Write a program that takes a string from the user and prints the number of
spaces in the string.

# str=input("Enter any string:")
# str=input("Enter any string:")
# space_count=0
# for ch in str:
#     if ch==" ":
#         space_count+=1
# print(space_count) 
#second approach or method          
str=input("Enter any string:")
space_count=str.count(" ")
print(space_count) 
'''

'''
Q8. Write a program to check whether two lists share no common elements.
l1=[1,2,3,4]    
l2=[5,6,7,8]    

s1=set(l1)    
s2=set(l2)    

if s1.intersection(s2):
    print("These sets have common element\n")    
else:        
    print("These sets don't have common element\n")
'''

'''
q.9)Given a list, print all elements that appear more than once in the list.

lst=[1,2,3,2,4,5,1,6,3]
check=set()
duplicates=set()

for item in lst:
    if item in check:
        duplicates.add(item)
    check.add(item)
print(duplicates)    
'''  

'''
Q1O. Ask the user for a string and print:
• All unique characters
• The count of unique characters
'''  

str=input("Enter any string:")

unique=set()
for ch in str:
    unique.add(ch)
print(unique)
print(len(unique))