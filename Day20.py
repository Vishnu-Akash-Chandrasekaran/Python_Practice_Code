######iterator
a = [0,5,10,15,20]
for i in a:
    if i%2==0:
        print(str(i)+" is an even number")
    else:
        print(str(i)+" is an odd number")

#######iterable

fruit = ["apple","mango","orange"]
fruit_it = iter(fruit)
print(type(fruit_it))
print(next(fruit_it))
print(next(fruit_it))
print(next(fruit_it))


mystr = "Namakkal"
myit  =iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#############################################

class Numbers:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x

number_class = Numbers()
number_iter = iter(number_class)
print(type(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))


class Numbers:
    def __iter__(self):
        self.a = 0 
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a +=1
            return x
        else:StopIteration
    

number_class = Numbers()
number_iter = iter(number_class)
for x in number_iter:
    print(x)























