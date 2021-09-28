from sympy import *

'''Using sympy'''
x = Symbol('x')
f = x**2 + x/2 - sin(x)/x

f_ = Derivative(f,x)

print(f_.doit())


# Now we solve first derivative at x=2 for a new function
x = Symbol('x')
f2 = x**4 - 8*x**2 + 356

f2_ = Derivative(f2,x)
f2_lb = lambdify(x, f2)

print(f2_.doit())
print(f2_lb(2))

