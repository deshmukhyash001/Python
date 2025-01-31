x = int(input("Enter a number to check whether the number is palindrome or not: "))
y = str(x)
a = []
for i in y:
    a.append(i)
print(a)
copy_a = a.copy()
print(copy_a)
copy_a.reverse()
if copy_a == a:
    print("Palindrome")
else:
    print("Not Palindrome")