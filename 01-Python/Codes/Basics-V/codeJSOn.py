'''import json

json_str='{"name":"Parag","isStudent":"null"}'

py_obj=json.loads(json_str)

print(type(py_obj),py_obj)
'''

'''
to load data from a string use these:
• json.loads( )-read
• json.dumps( )-write

to load data from json file use these:
• json.load( )-read
• json.dump( )-write
'''

'''#to read the json data in the file
import json
with open("data.json","r") as f:
    py_obj=json.load(f)
    print(py_obj)
'''
#now if we want to  overwrite in the json format 

import json

data={
    "name":"Parag the don",
    "age":21,
    }

with open("data.json","w") as f:
    py_obj=json.dump(data,f,indent=4,sort_keys=True)
    print(py_obj)