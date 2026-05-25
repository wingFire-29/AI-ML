'''
Lists are mutable
we can store similar or different types of data like str + int
we can do slicing creating sublist
'''

marks=[99, 89, 100, 65, 92]

marks_two=marks[0:3]
print(marks_two)
# cannot append like these use method append
marks[4]=90

# Lists Methods
# 1.)l.append(val) #add one element at the end
# 2.)l.insert(idx, val) #insert element at idx
# 3.)l.sort()-#arranges in increasing order
# 4.)l.reverse( )-#reverses order


marks.append(97)
marks.sort()
marks.insert(2,87)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)

# using loops on list
nums=[1,2,3,12,11,5]
x=11
idx=0
for val in nums:
    if(val==x):
        print(f"{x} found at index:{idx}")
        break
    idx+=1
