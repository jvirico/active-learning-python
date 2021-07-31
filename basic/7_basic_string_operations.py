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

list = ['aaa yeah', 'bbb oou yeah']

for element in list:
    z = re.match("([a-z]\w+)\W([a-z]\w+)",element)
    if z:
        print(z.groups())