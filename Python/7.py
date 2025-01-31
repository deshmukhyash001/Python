list1 = [1,2,5,3,7,5,9,8,4,6]
a = []
list_1 = len(list1)
for i in range(list_1-1,-1,-1):
    a.append(list1[i])
print(a)
print(type(list1))

list2 = [23,65,86,93,63,12,56]
b = []
for i in range(len(list2)-1,-1,-1):
    b.append(list2[i])
print(b)
print(type(list2))

list3 = [54,76,24,83,14,15,84]
rev = reversed(list3)
print(list(rev))

