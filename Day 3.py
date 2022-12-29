a =22
print(type(a))
b=22.4
print(type(b))
c="Namakkal"
print(type(c))
d=True
print(type(d))
e=2+5j
print(type(e))


#***********To find immmutable**************

a = 22
print(id(a))
a = 4
print(id(a))

#
char="Bangalore"
print(char[5])

#f =
#f[0]="M"
#print(f)

print(bool(-22))

#**********************
print(int(123.45))
print(int("44"))
print(int(True))
print(int(False))

#print(int("66.66"))

print(float("123.88"))
print(float(22))
print(float(True))
print(float('123'))

#**********************

print(bool("name"))
print(bool(1+2j))
print(bool(0))
print(bool(None))
j = 0
print(bool(j))
#when it print it shows an bcz j is not defined print(bool(j))

#**********************

print(str("Vishnu"))
print(str(1))
print(str(12.7))
print(str(1+2j))

print()

z=True
print(type(z))
y = str(z)
print(type(y))

#*********************
# string_name[start:end:step]
city_name = "Namakkal"
print(city_name[2])
print(city_name[-3])
print(city_name[2:6])
print(city_name[0:7:2])
print(city_name[-6:-1])
print(city_name[1:1000000]) #it will start from index 1 and it will goes upto the end
print(city_name[::-1])# it will reverse the string




