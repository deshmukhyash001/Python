'''
Lambda function :- Lambda function is an anonymous function. It can take any number of arguments but can have only one expression 
    that is seperated by a colon (:). It is useful when you have to write a function for single operation to be performed
syntax :-
    lambda(arguments : expression)
'''

x = lambda a,b,c : a+b+c
print(x(4,2,7))