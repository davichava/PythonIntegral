# from matplotlib.pyplot import *
# from numpy import *
# x=arange(0,10,0.001)
# f=x*2+4*x
# g=2*x-5
# xlim(0,8)
# ylim(0,15)
# plot(x,f,x,g)
# fill_between(x,f,g, where=(0<=x)&(x<=4),color='b')
# grid()
# from sympy import *
# x=symbols('x')
# f=x*2-4*x
# g=2*x+5
# h=g-f
# res=integrate(h,(x,0,4))
# print(f'la respuesta es {res}')
# show()

# from matplotlib.pyplot import *
# from numpy import *
# x=arange(0,8,0.001)
# f=5*x-6*2
# g=4*x-6
# xlim(-1,15)
# ylim(-13,30)
# plot(x,f,x,g)
# fill_between(x,f,g, where=(-5<=x)&(x<=6), color=('b'))
# grid()
# from sympy import *
# x=symbols('x')
# f=5*x-6*2
# g=4*x-6
# h=g-f
# res=integrate(h,(x,-5,6))
# print(f' La respuesta es: {res}')
# show()

import matplotlib.pyplot as plot
import numpy as np 

def f(x):
    return 1/x**2+1

x = np.linspace(-10,10,100)
x1 = np.linspace(10,10,100)
fig, ax = plot.subplots()
ax.plot(x, f(x))
ax.fill_between(x1, 10, f(x1), color='b')
ax.grid()
ax.set_title('f(x):1/x**2+1')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

# def f(x):
#     return 1/x**2+1

# x = np.linspace(0,5,100)
# x1 = np.linspace(2,4,100)
# fig, ax = plot.subplots()
# ax.plot(x, f(x))
# ax.fill_between(x1, 0, f(x1), color='b')
# ax.grid()
# ax.set_title('f(x):1/x**2+1')
# ax.set_xlabel('Eje X')
# ax.set_ylabel('Eje Y')

# from sympy import *
# x=symbols('x')
# f = 1/x**2+1
# res=integrate(f,(x,-2,2))
# print(f'La respuesta es: {res}')
# plot.show()