def Palindrome(a):
    b = str(a)
    c = b[::-1]
    if b == c:
        return True
    else:
        return False
    
a = 12324
res = Palindrome(a)
if res is True:
    print("Palindrome")
else:
    print("Not a Palindrome")