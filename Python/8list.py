#List

#CREATING A LIST
l1 = [12,74,96,82,25,95]
print("l1 = ",l1)

l2 = [43,68,62,97,72,15]
print("l2 = ",l2)
print(type(l2))

#ADDING TWO LIST
l1 = l1 + l2
print("ADDITION of l1 & l2",l1)

#ACCESSING LIST
for i in l2:
    print(i)

print()
print(l1[4])
print(l1[2:7])