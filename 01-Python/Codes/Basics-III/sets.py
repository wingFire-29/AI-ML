'''
collection of unique elements
we cxannot write list and dictonary bcz they are mutable
python sets apne ap m mutable h but uske elements immutable hona chiye
string and tuples are allowed as they are immutable
no order
mutable

'''
s={1,2,3,3}
print(s)
print(type(s))
print(len(s))
# to add value in set
s.add(4)
print(s)
empty_set=set()
print(type(empty_set))


'''
s.add(val)=#adds a val

s.remove(val)=#removes a val

s.clear( )=#empties the set

s.pop( )=#removes a random val

s.union(set2)=#returns new union

s.intersection(set2)=#returns new intersection

'''

s.remove(1)
print(s)
s.pop()
print(s)

# s.clear()
print(s)