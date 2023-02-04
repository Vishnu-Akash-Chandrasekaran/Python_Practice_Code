g = (x*x for x in range(100000))
print(type(g))
print(next(g))

def first_value(num):
    n = 1
    while n <= num:
        yield n
        n = n+1
values = first_value(100)
#print(type(values))
for x in values:
    print(x,end=" ")

#########################################
for i in range(1,5):
    print("*"*i)
print()
count2=1
count=1
for i in range(4,8):
    i-=count2
    print(" "*i,end=" ")
    print("*"*count)
    count+=1
    count2+=2
l = []
for i in range(100):
    l.append(i)

print(l[99])
