class Parent:
    a = 10
    def __init__(self):
        self.b=10
    def m1(self):
        print("Instance method")
    @classmethod
    def m2(cls):
        print("Class method")
    @staticmethod
    def m3():
        print("Static method")

class Child(Parent):
    pass


c=Child()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()

####################################

class Parent:
    a = 10
    def __init__(self):
        self.b=10
    def m1(self):
        print("Instance method")
    def m2(self):
        print("Class method")
    @staticmethod
    def m3():
        print("Static method")

class Child(Parent):
    pass


c=Child()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()

###################Single level inheritance#####################################

class Parent:

    def m1(self):
        print("First method")
class Child(Parent):
    def m1(self):
        print("Child m1 method")
    def m2(self):
        print("Second method")

t=Child()
t.m1()
t.m2()

####################Multilevel inheritance###################3

class Parent:
    def m1(self):
        print("Parnet method Vishnu Akash")
class Child1(Parent):
    def m2(self):
        print(" child Navinnn")
class Child2(Child1):
    def m3(self):
        print("sub child Johnson VJ")

c=Child2()
c.m1()
c.m2()
c.m3()

##############################Hierarchical inheritance##################################


class Parent:
    def m1(self):
        print("Parnet method Vishnu Akash")
class Child1(Parent):
    def m2(self):
        print("child1 Navinnn")
class Child2(Parent):
    def m3(self):
        print("child2 Johnson VJ")

c1=Child1()
c1.m1()
c1.m2()
c2=Child2()
c2.m1()
c2.m3()

##########################Multiple Inheritance####################################

class Parent:
    def m1(self):
        print("First Parent")
class Parent2:
    def m2(self):
        print("Second parent")

class Child(Parent,Parent2):#---> method resolution order
    def m3(self):
        print("child method")

c=Child()
c.m1()
c.m2()
c.m3()



class Parent:
    def m1(self):
        print("First Parent")
class Parent2:
    def m2(self):
        print("Second parent")
    def m1(self):
        print("Parent2 m2")
class Child(Parent2,Parent):#---> method resolution order
    def m3(self):
        print("child method")

c=Child()
c.m1()
c.m2()
c.m3()


######################super() Method####################################

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self,name,age,rollno,mark):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark

    def display(self):
        super().display()
        print(self.rollno)
        print(self.mark)
        
s1=Student("Vishnu Akash",24,146,99)
s1.display()


























