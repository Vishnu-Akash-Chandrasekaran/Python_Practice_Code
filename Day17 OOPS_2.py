# Method Overloading:

def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)

add(10,12,10)
#####################################
class Test:
    def __init__(self):
        print("No arg constructor")
    def __init__(self,arg):
        print("1 arg constructor")
    def __init__(self,arg1,arg2):
        print("2 arg constructor")

t=Test(1,2)
