####### list comprehension ########

in_list = [1,2,3,4,5,6,7,8,10]
l = []
for i in in_list:
    if i%2 == 0:
        l.append(i)
print(l)

in_list = [1,2,3,4,5,6,7,8,10]
new_list = [i for i in in_list if i%2==0]
print(new_list)

####### Dict comprehension ########

in_list = [1,2,3,4,5,6,7,8,10]
d = {}
for i in in_list:
    if i%2 == 0:
        d[i] = i ** 2
print(d)

new_dict = {i:i**2 for i in in_list}
print(new_list)

####### set comprehension ########

in_list = [1,2,3,4,5,6,6,6,7,7,8,10]
s = set()
for i in in_list:
    if i%2 == 0:
        s.add(i)
print(s)

new_set= set(i for i in in_list if i%2==0)
print(new_set)

##nested list:
