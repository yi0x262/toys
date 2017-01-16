#!/usr/bin/env python3
from sympy import *

def newtons_method(f,var,x0,times=10,show=False):
    df = diff(f,var)
    d2f = hessian(f,[var])
    d2finv = d2f.inv()
    x = x0
    for t in range(times):
        res = {var:x}
        if df.subs(res) < 1e-20:
            return x,t
        d = -d2finv[0,0]*df
        if show:
            print('t,x:',t,x)
            print('df(x_t):',df.subs(res))
            print('d2f:',d2f.subs(res))
            print('d2finv:',d2finv.subs(res))
            print('d:',d.subs(res))
        x += d.subs(res)
    print('solved t,x:',times,x,float(x))
    return x,times

if __name__ == '__main__':
    x = Symbol('x')
    f = (x-2)*(x-1)*(x+1)*(x+2)

    df = diff(f,x)
    d2f = hessian(f,[x])
    print(df)
    print(d2f)

    solve1,_ = newtons_method(f,x,Rational(2),times=1)
    solve2,_ = newtons_method(f,x,Rational(2),times=2,show=True)

    print(df.subs({x:solve1}),df.subs({x:solve2}))


    from sympy.plotting import plot
    plot(f,(x,0,2.5))
