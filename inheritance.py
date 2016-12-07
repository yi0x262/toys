class myfloat(float):
    def __new__(self,*args):
        return float.__new__(self,sum(args))

class meta(type):
    def __new__(cls,*cls_bases,**cls_dicts):
        print('meta.__new__')
        return super().__new__(cls,*cls_bases,**cls_dicts)

class mycls(object,metaclass=meta):
    pass

class call_meta(type):
    def __new__(cls,*cls_bases,**cls_dicts):
        print(cls,*cls_bases,**cls_dicts)
        return super().__new__(cls,*cls_bases,**cls_dicts)
    def __setattr__(cls,*cls_bases,**cls_dicts):
        print(cls,cls_bases,cls_dicts)
        return super().__setattr__(cls,*cls_bases,**cls_dicts)
    def __getattr__(cls,*cls_bases,**cls_dicts):
        print(cls,cls_bases,cls_dicts)
        return super().__getattr__(cls,*cls_bases,**cls_dicts)

class myint(int,metaclass=call_meta):
    value = 0
    pass


if __name__ == '__main__':
    i = myfloat(5,10,15)
    j = 10

    print(i)
    print(j)

    i += j

    print(i)

    print('def mycls')
    my = mycls()

    i = myint(4)
    i.value = 3
    print(i.value)
