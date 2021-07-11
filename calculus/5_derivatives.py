from sympy import *

'''Using sympy'''
x = Symbol('x')
f = x**2 + x/2 - sin(x)/x

f_ = Derivative(f,x)

print(f_.doit())

