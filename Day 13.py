#map(function,sequence)
l=[1,2,3,4,5]
def double_it(x):
    return 2*x

l1 = list(map(double_it,l))
print(l1)

#Lambda
l1=list(map(lambda x:x*2,l))
print(l1)

# filter(function,sequence)

from functools import *

l=[10,20,30,40,50]
output=reduce(lambda x,y:x+y,l)
print(output)

def fun():
    print("Hello")

print(fun)
print(id(fun))
print(type(fun))

#Doc String

def print_function():
    '''Hi, I am Vishnu Akash and I am coming from Namakkal'''
    print("This is the simple print function")

print("using__doc__")
print(print_function.__doc__)

print("using__doc__")
help(print_function)
