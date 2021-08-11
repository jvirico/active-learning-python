'''
    Playing with Lists
        - Reminiscent of arrays in other languages, 
        but tend to be more powerfull.
        - No type restriction
'''


L = ['mama','ferran']
print(L+ [1.0,4.0,-1.2])
print(L*2)

# removing value
L.append('Sonia')
print(L)

print(L.pop(0))
print(L)
L.append('Raquel')
L.sort()
print(L)
L.reverse()
print(L)

'''Nesting objects'''
m1 = [1,2,3]
m2 = [3,4,5]
m3 = [5,6,7]
M = [m1,m2,m3]
print(M)
print(M[0][1])

n1 = {'key':'value'}
print(n1)
N = [m1,n1,3.999]
print(N)

## Tuples
#   - Integrity constrain that differentiates them from lists,
#   it may be needed an inmutable list to pass around.

T = (1,2,3,4)
print(T)
print(T + (5,6))
print(T.index(4))
print(T.count(4))
# Tuples can not be changed
# T[0] = 2 => error!!
T2 = (2,) + T[1:]
print(T2)
# accept multiple types like lists and dictionaries
T3 = ('spam', 3.0, [1,2,3])
print(T3)
# parenthesis can be ommited
T4 = 1.0, 2.0, 'aserejé'
print(T4)

res = [c * 2 for c in 'This is a string']
print(res)

# mapping a function across a sequence
L1 = list(map(abs,[1,-2,-3,4]))
print(L1)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0][1])
matrix[0][0] = 9
print(matrix)

# replacement, insertion, deletion
L1[1:2] = [4,5] # replacement
print(L1)
L1[3:3] = [6,7]
print(L1)
L1[5:] = []
print(L1)

L1 = [1]
L1[:0] = [-2,-1,0]
print(L1)
L1[len(L1):] = [2,3]
print(L1)

# list methods
L2 = [3,1,4,5]
L2.sort()
print(L2)
print(L2.pop())
print(L2)
L2.reverse()
print(L2)
L2.reverse()
print(list(reversed(L2)))
L2.append(6)
print(L2)
