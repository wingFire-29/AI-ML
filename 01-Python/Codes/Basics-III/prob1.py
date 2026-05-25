'''
Given a list of tuples with info(name, subject):
->list all unique course
->list students enrolled in English
->create dictionary (student, set of course)
'''


info= [
    ("Alice", "Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
# print(info)
# course_set=set()

# a.)
# for tup in info:
#     course_set.add(tup[1])
# print(course_set)

# # b.)
# for name,course in info:
#     if(course=="English"): 
#         print(name)
        
# c.)
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)