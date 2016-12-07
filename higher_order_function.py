def twice(func):
    def func2(x):
        return func(func(x))
    return func2
def add1(x):
    return x+1
def sub1(x):
    return x-1

x = 0
add2 = twice(add1)
print(x,add2(x))
sub2 = twice(sub1)
print(x,sub2(x))
