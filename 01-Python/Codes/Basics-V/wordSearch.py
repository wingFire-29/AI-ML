'''
This is a practice problem
wee will try to find the word "Python" in the search.txt file
'''
# with open("search.txt","r") as f:
#     for i in f:
#         i=f.readline()
#         if i=="Python":
#             return 

data=True# so that the loop may run for the first time
line=1# tracks the line number
word=input("Enter the word to search:")
with open("search.txt","r") as f:
   while data:#runs loop untill we have valid data from the file
        data=f.readline()
        if(word in data):
            print(f"{word} found at line no {line}")
            break
        print(data)
        line+=1

   




