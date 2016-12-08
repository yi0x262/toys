def descripter(func):
    def printreturn(*args,**keys):
        ret = func(*args,**keys)
        print(ret)
        return ret
    return printreturn

@descripter
def add2(a,b):
    return a+b
@descripter
def add3(a,b,c):
    return a+b+c

add2(1,2)
add3(3,3,4)    
