'''
Docstring for fileIO
we will study abt the operations on files
reading is default mode

r->#reading [default]
w->#writing, truncates file first//exisdting file me overwriting krni h to yh
x->#creates new & open for writing//new file bnani h  to use this unknoqingly changes ni krta existing file m
a->#writing, appends at end
b->#binary mode
t->#text mode [default]
+->#opens disk file for update(r & w)

#to open a file
f=open("sample.txt","r")
print(f.read())
print(f.readline())
f.close()

f=open("sample.txt","w")
f.write("TEXT WILL BE OVERWRITTEN")
f.close()
'''


'''
To avoid any errors we have to explicitly close the file so that pur file is safe
bnut sometimes it can be hectic so we use the
'with' keyword that will do this job automatically
'''
# with open('sample.txt','r') as f:
#     data=f.read()
#     print(data)

# with open("sample3.txt","r") as d:
#     d.write("This is a third sample file")
#     # data=d.read()
#     # print(data)

import os
# os.remove("sample3.txt")
os.remove("sample2.txt")