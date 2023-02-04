######################File exception#####################################################

a=int(input("Enter the number: "))
print(a)


print("Hello")
print("hi")

try:
    print(10/0)
except ZeroDivisionError as e:
    print("Give number")

print("stmt-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
finally:
    print("stmt-3")


try:
    x=int(input("Enter First Number:"))
    y=int(input("Enter Second Number:"))
    print(x/y)
except ZeroDivisionError:
    print("Can't Divide with zero")
except ValueError:
    print("please provide int value only")

try:
    print("try")
except:
    print("except")
finally:
    print("finally")



try:
    print("try")
    print(10/0)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")
###########################################################################
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg = arg
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg = arg

age = int(input("Enter the age: "))
if age < 18:
    raise TooYoungException("Not Eligible")
elif age > 18:
    raise TooOldException("Eligible")
else:
    print("You will et email")


