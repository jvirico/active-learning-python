'''
    Numeric Types, Operators, math
'''

a = 3
b = 4

print(a+1,a-1)

# print rounds off digits
print(b / (2.0 + a))
num = 1 / 3.0
# formatting
print('%4.2f = %i = %e = %f' % (num,num,num,num))

# division, floor
print(b/a)
print('floor: a/b = %f' % (b//a))

# bringing capabilities from higher python versions
#from __future__ import division # if python 2.X
print(10/4)
print()
## math, floor vs truncation
import math
print(math.floor(2.5))
print(math.trunc(2.5))
print(math.floor(-2.5))
print(math.trunc(-2.5))

## integer precision
print(100000000000000000 +1)
print(2**200)

## complex numbers
print(1j * 1j)

## Bitwise opeations
x = 1 # 1 decimal is 0001 in bits
print(x << 2) # moving 1 two positions -> 0100 is 4 in decimal
print(x | 2) # 0001 | 0010 = 0011
print(x & 1)

## Built-in numeric tools
print(math.pi)
print(math.e)

print(math.sin(2*math.pi / 180))
print((math.sqrt(144),math.sqrt(2)))
print((pow(2,4),2**4,2.0**4.0))
print((abs(-42.0),sum((1,2,3,4))))
print((min(2,3,4,5), max(9,4,3,2)))

# randomization
import random

print(random.random())
print(random.random())
print(random.random())

print(random.randint(1,10))
print(random.choice(['Maps of Meaning','10 rules for life','12 more rules for life']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)

# avoiding numeric errors with Decimal
print(0.1+0.1+0.1-0.3)

from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

# setting decimal precision
import decimal

print(decimal.Decimal(1)/decimal.Decimal(7))

decimal.getcontext().prec = 4
print(decimal.Decimal(1)/decimal.Decimal(7))

print()

# decimal local context
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal(1)/decimal.Decimal(7))
print(decimal.Decimal(1)/decimal.Decimal(7))


## Fraction type
from fractions import Fraction

x = Fraction(1,3)
y = Fraction(4,6)

print(x+y)
print(x*y)