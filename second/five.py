import math 

height = float(input('enter a height'))
radius = float(input('enter a radius'))\
#2π r h + 2π r²

print('volume of cylender is: ',math.pi*(radius**2)*height)
print('surface area of cylender is: ', (2*math.pi*radius*height)+(2*math.pi*radius**2))
