import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

#to print empty list
l=list()
print(l)
print(type(l))
a = []
print(a)

#************************
lst = [1,2,3,"Namakkal",20.23,True]
print(lst)
print(lst[4])
v = []
for i in lst:
    v.append(i)
print(v)

#range function: range(start:end+1:step)
l1=list(range(1,11))
print(l1)

l2=list(range(1,11,2))
print(l2)

#to clear the list which mean it will empty the list

lst.clear()
print(lst)

#to delete the object which mean to delete the varible

del lst


#to print length which mean to count the number of element in the list

print(len(l1))

#to add element at end of the list

l = [1,22,3,44,5]
print(l)
l.append("Vishnu Akash")
print(l)

#to insert to new element
l.insert(2,"Good boy")
print(l)

# to update or add element in previous list
l2=["Good","classic"]
l.extend(l2)
print(l)

# to remove the element in list
l.remove(5)
print(l)

# pop: empty pop remove the last element

l.pop()
print(l)
l.pop(4)
print(l)

# reversing the element in the list
e = []
for i in range(0,11,2):
    e.append(i)
e.reverse()
print(e)

#sort the list
ele = [399,65,22,89,100,2,5]
ele.sort()
print(ele)






va = [2,55,66,77,993223,353,4]
t = reverse(va)
#t = va.reverse()
print(t)











