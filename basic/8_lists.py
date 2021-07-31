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