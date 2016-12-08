class auto_property(type):
    def __new__(metacls,name,args,keys):
        print("meta_class",name,args,keys)

        t = type.__new__(metacls,name,args,keys)
        print(t)

        return t


class MyInt(int,metaclass=auto_property):
    pass

if __name__ == '__main__':
    i = MyInt(0,key = 10)
