class Test:
    def m1(self):
        a=100
        print(a)
    def m2(self):
        b=200
        print(b)

t1=Test()
t1.m1()
t1.m2()
##################

class Student:
    def __init__(self):
        self.a= 50000
    def disp(self):
        a = 900
        print(self.a)
        print(a)

s1=Student()
s1.disp()

###########################
# class Method:

class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs...".format(name,cls.legs))

Animal.walk("Dog")
Animal.walk("Cat")
##########################
#staticmethod:

class CustomMath:
    @staticmethod
    def add(x,y):
        print(x+y)
    @staticmethod
    def product(x,y):
        print(x*y)
    @staticmethod
    def sub(x,y):
        print(x-y)

CustomMath.add(100,399)
CustomMath.product(100,2)
CustomMath.sub(12,8)

###########Polymorphism##############
#operation Overloading:
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        print(id(self))
        print(id(other))
        return self.pages+other.pages
    
b_1 = Book(100)
b_2 = Book(200)
b_3 = b_1 + b_2
print(b_3)


