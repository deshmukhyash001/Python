'''
*
**
***
**** 
*****
'''

n = 5
for i in range(n):
    print()
    for j in range(i+1):
        print("*",end = " ")
print("\n\n")
 
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * *
'''

for i in range(n):
    print()
    for j in range(i,n):
        print("",end = " " )
    for k in range(i+1):
        print("*",end = " ")
print("\n\n")

'''
A
BB
CCC
DDDD
'''

list1=["A","B","C","D"]
for i in range(len(list1)):
    print()
    for j in range(i+1):
        print(list1[i], end= " ")
print("\n\n")

'''
A
AB
ABC
ABCD
'''

list1 = ['A','B','C','D']
for i in range(len(list1)):
    print()
    for j in range(i+1):
        print(list1[j],end=" ")
print("\n\n")

'''
    *
   ***
  *****
 *******
*********
'''

n = 5
m=0
for i in range(1,n+1):
    print("")
    for j in range(i,n):
        print("",end=" ")
    for k in range(i+m):
        print("*",end= "")
    m = m+1
print("\n\n")

'''
1
12
123
1234
12345
'''

n =5 
for i in range(n):
    print()
    for j in range(i+1):
        print(j+1,end = " ")
print("\n\n")

'''
1
01
001
0001
00001
'''
n = 5
for i in range(1,n+1):
    for j in range(1,i):
        print("0",end = " ")
    print("1")
print("\n\n")

'''
    *
   ***
  *****
 *******
  *****
   ***
    *
'''

n = 5
for i in range(1,n+1):
    print()
    for k in range(i,n):
        print(" ",end= " ")
    for j in range(i*2-1):
        print("*",end=" ")
for m in range(1,n):
    print()
    for p in range(m):
        print(" ",end=" ")
    for o in range((n-m)*2-1):
        print("*",end=" ")
print("\n\n")