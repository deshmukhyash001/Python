import math

#WAP to print prime no. or not
n=int(input("Enter a number: "))
i=2
isprime=True
while (i<=n/2):
    if(n%i==0):
        isprime=False
        break
    i+=1
#result = n, "is prime" if isprime==False else n, "is not prime"
print( n, "is prime" if isprime else "is not prime")