'''
dictionary is key value pair data type
unique
dict={"name":"parag}
they are mutable and unordered

'''

info={
    "name":"Parag",
    "cgpa":9.2,
    "subjects":["math","Science"],
    3.14:"PI"
}
print(type(info))

'''
Methods
• d.keys()=#returns all keys

• d.values()=#returns all values

• d.items()=#returns (key, val) pairs

• d.get(val)=#returns val acc. to key

• d.update(new_item)=#adds new item to dict
'''

print(info.keys())
print(info.get("cgpa2"))
print(info.values())
print(info.items())
print(info.update(
    {"city":"Chandigarh"}
))
print(info.items())
