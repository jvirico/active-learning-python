'''
    List Comprehension Expresions:
        - Way to build a new list by running an expression on each item
        in a sequence
        - e.g. way to process structures like matrices
'''
import numpy as np

k = [-3,5]
b = [5,3]
r = [-2,-4]
g = [3,-4]

M = np.array([k,b,r,g])
print(M)

col2 = [row[1] for row in M]
print(col2)

print([row[1]+1 for row in M])
# filter out odd items
col2_odd = [row[1] for row in M if row[1] % 2 == 0]
print(col2_odd)

# extract matrix diagonal
diag = [M[i][i] for i in range(M.shape[1])]
print(diag)

# repeat characters in a string
doubles = [c*2 for c in 'python']
print(doubles)

## range
print(list(range(4)))
print(list(range(-6, 13, 2)))

multiple_values = [[x**2,x**3] for x in range(4)]
print(multiple_values)

# if filters
iff = [[x,x/2,x*2] for x in range(-6,7,2) if x>0]
print(iff)

## Generators
print(M)
G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))
print(next(G))

# same but with built-in map
print(list(map(sum,M)))