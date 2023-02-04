##generator
def sq_numbers(n):
    for i in range(1,n+1):
        yield i*i

a = sq_numbers(3)
print(next(a))
print(next(a))
print(next(a))
print(type(a))
