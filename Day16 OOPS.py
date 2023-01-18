class Student: # class name, Pascal case
    def __init__(self): # constructor
        self.name = "Vishnu Akash" # instance variable
        self.age = 24
        self.mark = 99
        print("Inside: ", id(self))
    def talk(self): # object reference
        print(self.name)
        print(self.age)
        print(self.mark)

st1=Student()
st1.talk()
print("Outside: ",id(st1))

########################################
class Student: 
    def __init__(self,name,age,mark): # constructor
        self.name = name # instance variable
        self.age = age
        self.mark = mark
    def talk(self): # object reference
        print(self.name)
        print(self.age)
        print(self.mark)

st1=Student("Akash",24,100)
st1.talk()
st2=Student("Vishnu", 25,95)
st2.talk()
######################################

class Employee:
    def __init__(self):
        self.eno=100
        self.ename="Vakash"
        self.esal=200000

e=Employee()
print(e.__dict__)

################################
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t=Test()
t.m1()
print(t.__dict__)

#################################
class Student:
    school_name="SKV"

    def __init__(self):
        self.a=100

    def display(self):
        a = 200
        print(self.a)
        print(a)

std1=Student()
std1.display()
print(std1.__dict__)
print(Student.__dict__)
print(std1.school_name)






import sys
import random
import timeit
t1="string"
t2={}
t3={12:12}
t4=[]
t5=(1,2,3,32,43,543,5,545,4645,4545)
t3[12]=100
print(t3)
print(sys.getsizeof(t1))
print(sys.getsizeof(t2))
print(sys.getsizeof(t3))
print(sys.getsizeof(t4))
print(sys.getsizeof(t5))















