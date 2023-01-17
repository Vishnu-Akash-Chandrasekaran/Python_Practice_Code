f=open("new_besant_file.txt",'a')
list=["Python\n","html\n",""]
f.writelines(list)
print("List of lines written to the successfully")
f.close()

f=open("new_besant_file.txt",'r')
data=f.read()
print(data)
f.close()


f=open("new_besant_file.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()
