import re
x="\s"
matcher=re.finditer(x,"a7b k@9z")
for match in matcher:
    print(match.start(),".......",match.end(),"........",match.group())


def fun(x):
    x="\s"
    matcher=re.finditer(x,"a7b k@9z")
    for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())

x1="[a]"
x2="[a+]"
x3="[a*]"
x4="[a?]"
x5="[a{m}]"
x6="[a{m,n}]"
fun(x1)
fun(x2)

print()
print()


###########match##################
s=input("Enter pattern to check: ")
m=re.match(s,"abbchejde")
if m!= None:
    print("Match is available at the begining of the string")
    print("Start Index",m.start(),"End Index",match.end())
else:
    print("Match is not available at the begining of the string")
###########fullmatch##################

s=input("Enter pattern to check: ")
m=re.fullmatch(s,"abbchejde")
if m!= None:
    print("Full string matched")
else:
    print("Full string not matched")

###########SEARCH()##################
s=input("Enter pattern to check: ")
m=re.search(s,"abbchejde")
if m!= None:
    print("Match is available")
    print("First occurrence of match with start index",m.start(),"and End Index:",match.end())
else:
    print("Match is not available")

###################FINDALL()###########################

import re
l=re.findall("[0-9]","a7b9c5kz")
print(l)

###################SUB()###########################

import re
l=re.sub("[a-z]","$","a7b9c5kz")
print(l)


###################SUBN()###########################
import re
l=re.subn("[a-z]","$","a7b9c5kz")
print(l)
print(l[0])
print(l[1])















