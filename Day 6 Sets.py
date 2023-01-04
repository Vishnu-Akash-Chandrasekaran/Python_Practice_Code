#sets

s = set()
print(type(s))

s = {1,2,3,4,5,6,1,2,3,9,10}
print(s)

#range fun
s1 = set(range(0,11,2))
print(s1)

s2 = set([1,2,3,4,5,7,8,1,2,3])
print(s2)

d = {1:222,2:33,3:55,4:56,5:98}
s = set(d.values())
print(s)

#adding element
s3 = {1,2,3,4,5,6,7,9,10}
s3.add(23)
print(s3)
#update

l=[1,2,3,4,5]
t=(111,222,333)
s={777,888,999}
s1=set()
s1.update(l,t,s)
print(s1)
