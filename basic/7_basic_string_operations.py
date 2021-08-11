'''
    Some basic string operations
'''


S = 'this is a string'
print('Printing the string S: %s'% S)
print(len(S))
print(S[0])
# strings indexes behave cyclicly
print(S[-2])
# accessing substring
print(S[:7])
print()
# the following performs a full copy of the string
S_bk = S[:]
print(S_bk)
# concatenation and repetition
A = 'Brand'
RB = 'Russel' + ' ' + A
print(RB)
print(A*8)

'''Strings are immutable in Python'''
try:
    A[0]='z'
except:
    print(' Error: strings are immutable in Python!')
    print(' But..')
    a = 'z' + A[1:]
    print(' '+ a)

'''Expand and join strings'''
S = 'worm'
# expanding
L = list(S)
print(L)
L[0] = 'W'
# joining
l = ''.join(L)
print(l)

'''String operations, or object methods'''
S = 'Bambam'
print(S.find('ba')) # returns index of word or -1 for not found
print(S.replace('Bam','bam'))

'''Splitting'''
line = 'hey you, what is up?'
L = line.split(',')
print(L)

'''Upper - lowwer'''
print(line.upper())


'''Difference between singe and double quotues for text'''
single = 'this is a sentence that uses "double quotes" in it'
print(single)
double = "now, we use 'single quoutes' instead"
print(double)

'''UNICODE'''
S = 'sp\xc4m'
print(S)

'''REGEX'''
import re

list_ = ['aaa yeah', 'bbb oou yeah']

for element in list_:
    z = re.match("([a-z]\w+)\W([a-z]\w+)",element)
    if z:
        print(z.groups())


# quoutes
mantra = """Always look
on the bright
side of life ;)"""
print(mantra)

menu = (
    "Paella "       # this way
    "Valenciana "   # we can add comments
    "de la mama")   # to each separate line

print(menu)

# string repetition
print('-------- ...more... ---')
print('-' * 80)

# reading string characters
myjob = "pyhtonian"
for c in myjob:
    print(c, end=' ')

print('py' in myjob)
print(myjob[0],myjob[-2])

# extended slicing
s = 'amaasndufepll e;n)affdselfoa4'
print(s[1:18:2])

# string conversions
print((int('23'), str(32),str('text')))
print((repr(23.0),repr('23.0')))
print()

# converting binary to integer and biceversa
decimalNum = int('101010',2)
print(decimalNum)
print(bin(decimalNum))

## Strings are not editable, to modify a string we need to create a new one.
try:
    s[3] = 'x'
except:
    print('error happened')
s_new = s[0:2] + 'x' + s[3:] # new string from previous
print(s_new)

s_new = s.replace('foa', 'thisisnew')
print(s_new)

###
# String Methods
##
print('aa$bb$cc$dd'.replace('$','SPAM'))
print('the string "pll" is in the position %s of the string "%s"'% (s.find('pll'),s))
L = list(s)
print(L)
print(type(L))
l = ''.join(L) # back to a string
print(l)
print(type(l))

# 2966DAB5
print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))
line = 'aaa bbb ccc'
cols = line.split(' ')
print(cols)
print(line.upper())
print(line.endswith('cc'))

# formating expressions
print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))