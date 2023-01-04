#Dictionaries, it was the fast datastructure:

d = {"name":"Vishnu Akash","age":24,"city":"Tamil Nadu","vehicle":"Hero Honda"}
print(d)
#popitem
d.popitem()
print(d)

#copy
d1=d
print(d1)
d2=d.copy()
print(d2)

#del
del d2["city"]
print(d2)

#setdefault
d2 = {1:23,2:45}
v = d2.setdefault(1,111)
print(v)

v=d.setdefault(5,111)
print(v)
print(d)
print(d2)
#########################
d1 = {"name":"Vishnu Akash","age":24}
print(d1)
d2 = {"city":"Tamil Nadu","vehicle":"Hero Honda"}
print(d2)
d1.update(d2)
print(d1)
