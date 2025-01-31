li = [1,6,3,8,3]
an = li[3]
print(an)
del li[2]
print(li)
li = li + [54,86]
print(li)
li[2] = 34
print(li)
print(li.index(54))
li.extend([52,89,24,15])
print(li)
li.append(4)
print(li)
print(li.pop(4))
print(li)
del li[3],li[4]
print(li)

