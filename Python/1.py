#WAP to Print your name
print("My name is Anish")

tup = 1,2,4
print(type(tup))

a = 101
b = 110
print(a & b)
print(a | b)
print( ~a)

a = list(input("Enter numbers for the list[, separated values]: ").split(","))
print(a)

b = int('101',2)
print(b)

c = [1,2,3,2,1]
# d = c.copy()
# d.reverse()
d = list(reversed(c))
print(list(d))
print(c)
if c == d:
    print("Palindrome")
else:
    print("Not a Palindrome")