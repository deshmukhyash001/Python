#WAP to print factorial of a no.
n = int(input("Enter a no.: "))
i=1
fact=1
while (i<=n):
    fact = fact * i
    i+=1
print("Factorial of",n,"is",fact)
