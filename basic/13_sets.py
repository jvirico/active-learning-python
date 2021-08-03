'''
    SETS
'''

X = set('ham')
print(X)
Y = {'c','h','e','e','s'}
print(Y)

print((X,Y))

# intersection
print(X & Y)
# union
print(X | Y)
# difference
print(X - Y)
# superset
print(X > Y)
# set comprehension
print({n**2 for n in [1,3,2,5]})

s = set([1,1,2,2,3,3,4,5,6])
print(list(s))

# finding differences in collections
print(set('ham') - set('spam'))
print(set('scam') == set('masc'))

print('h' in X, 'p' in Y, 'ham' in ['eggs', 'spam', 'ham'])

a = 1/3
print(a)
print((2/3) + (1/2))

import decimal
d = decimal.Decimal('3.141')
print(d+1)

from fractions import Fraction
f = Fraction(2,3)
print(f+1)

print(f + Fraction(1,2))