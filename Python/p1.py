#Practical 2
#WAP for indian rupees to US dollar conversion
rs = float(input("Enter Rupees: "))
usd = rs / 83.88
print("The indian rupees to US dollar is: {:.2f}".format(usd))

#WAP for convertion of bits to Megabytes, Gigabytes and Terabytes
bits = int(input("Enter bits: "))
megabits = bits / 1000000 
gigabits = bits / 1000000000 
terabits = bits / 1000000000000 
print("The bits to Megabytes is: {:.2f}".format(megabits))
print("The bits to Gigabytes is: {:.2f}".format(gigabits))
print("The bits to Terabytes is: {:.2f}".format(terabits))

#WAP to find square root of no.
import math
num = int(input("Enter a number: "))
sqrt1 = math.sqrt(num)
print("The square root of the number is: {:.2f}".format(sqrt1))

#WAP for finding area of rectangle 
_len = int(input("Enter Length: "))
_wid = int(input("Enter Width: "))
print("Area of Rectangle is: ",_len * _wid)

#WAP for perimeter and area of square
sqr = int(input("Enter side for square: "))
per = sqr * 4
area = sqr * sqr
print("Perimeter of Square is: ",per)
print("Area of Square is: ",area)
print("Area of Square (by func) is: ",pow(sqr,2))

#WAP to swap the value of two variables
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
temp = a
a = b
b = temp
print("Value of a is: ",a)
print("Value of b is: ",b)