import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaababa")

for match in matcher:
    count+=1
    print(match.start(),".......",match.end(),"........",match.group())

print("The number of occurrences: ",count)


import re
count=0
matcher=re.finditer("ab","abaababa")

for match in matcher:
    count+=1
    print(match.start(),".......",match.end(),"........",match.group())

print("The number of occurrences: ",count)

print()
print()
print()

#####################REGEX SETS###############################
import re

x = "[^abc]"
matcher=re.finditer(x,"a7b@k9z")
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())

print()
print()
x = "[abc]"
matcher=re.finditer(x,"a7b@k9z")
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())


print()
print()
x = "[a-z]"
matcher=re.finditer(x,"a7b@k9zqwieoccoan")
print(matcher)
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())

print()
print()
x = "[A-Z]"
matcher=re.finditer(x,"a7b@k9zqwieoccoanASDFGHJWERTYU")
print(matcher)
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())


print()
print()
x = "[a-zA-Z]"
matcher=re.finditer(x,"a7b@k9zqwieoccoanASDFGHJWERTYU")
print(matcher)
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())


print()
print()
x = "[0-9]"
matcher=re.finditer(x,"a7b@k9zqwieoccoanASDFGHJWERTYU")
print(matcher)
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())


print()
print()
x = "[a-zA-Z0-9]"
matcher=re.finditer(x,"a7b@k9zqwieoccoanASDFGHJWERTYU")
print(matcher)
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())


print()
print()
x = "[^a-zA-Z0-9]"
matcher=re.finditer(x,"a7b@k9%$zqwieoccoanASDFGHJWERTYU")
print(matcher)
for match in matcher:
        print(match.start(),".......",match.end(),"........",match.group())


####################REGEX SPECIAL SEQUENCE################################
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


        
