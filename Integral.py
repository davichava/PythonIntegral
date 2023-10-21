# from matplotlib.pyplot import *
# from numpy import *

# x=arange(-3,4,0.001)
# f=2*x+4
# plot(x,f)
# fill_between(x,f, where=(-2<=x)&(x<=3),color='b')
# grid()
# from sympy import *
# x=symbols('x')
# f=2*x+4
# res=integrate(f,(x,-2,3))
# print(f'la respuesta es {res}')
# show()

# from matplotlib.pyplot import *
# from numpy import *
# x=arange(-3,4,0.001)
# xlim(0,3)
# ylim(0,15)
# y1=2*x**2+3*x-2
# plot(x,y1)
# fill_between(x,y1, where=(1<=x)&(x<=2),color='b')
# grid()

# from sympy import *
# x=symbols('x')
# y1=2*x**2+3*x-2
# res1=integrate(y1,(x,1,2))
# print(f'la respuesta es {res1}')
# show()

# Èjercicio 1.

from matplotlib.pyplot import *
from numpy  import *
x=arange(0,10,0.001)
f=x**2-2*x
g=5*x-6
xlim(0,8)
ylim(-5,40)
plot(x,g,x,f)
fill_between(x,f,g, where=(1<=x)&(x<=6),color='b')
grid()

from sympy import *
x=symbols('x')
f=x**2-2*x
g=5*x-6
h=g-f
res=integrate(h,(x,1,6))
print(f'la respuesta es {res}')
show()