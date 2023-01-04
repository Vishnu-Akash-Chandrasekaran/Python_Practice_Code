#Dictionaries
d={}
print(type(d))
print(d)
d1 = dict()
print(d1)

d2 = {"name":"Vishnu AKash","age":24,"city":"Bangalore"}
print(d2)
#to update new key:value in existing dict
d2["salary"] = 50000
print(d2)

#to access the particular value
print(d2["name"])

#duplicate key was not allowed so last assigned value will be taken
d2["city"]="Tamil Nadu"
print(d2)

for key,value in d2.items():
    print(key,value)
print(d2.items())
print(d2.keys())
print(d2.values())

print(len(d2))
# it will through error the value is not in the dict function
#print(d2["address"])

#to get the particlar value in the dict function
value =d2.get("age")
print(value)

#it will give "None" while the key is not in the dict function
value = d2.get("address")
print(value)

#it will return the default value
value = d2.get("address","No value")
print(value)
