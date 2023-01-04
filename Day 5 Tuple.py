# tuble is immutable ordered, unchagable and allow duplicates
# in tuple round bracket is optional
t1 = (1,2,3,4,5)
print(type(t1))
print(t1)
print(t1[4])
for i in t1:
    print(i**2)

#tuple does not allow the item assignment
#t1[2]=100
#print(t1)

t2 = tuple(range(0,11))
print(t2)

#covert list into tuple 
l=[1,2,3,5]
t3 = tuple(l)
print(t3)

t4 = (111)
print(type(t4))
print(t4)

t5 = 33,
print(type(t5))
print(t5)

#packing and unpacking
#packing
a = 20
b =90
c = 40
t6=a,b,c
print(t6)

x,y,z=t6
print(x)
print(y)
print(z)
