
'''Pure python'''

# vectors
v1 = [1,2,3,4]
v2 = [3,2,0,1]

# matrix
A = [[1.0,2.0],[3.0,4.0]]
B = [[3,4,1],[-1,2,1]]

# Dot product v1.v2 = 11
v3 = sum(v1[i]*v2[i] for i in range(len(v1)))

# Matrix multiplication
C = [[0,0,0],[0,0,0]] # (2x3)
print(C)
#   rows of A
for i in range(len(A)):
    # cols of B
    for j in range(len(B[0])):
        # rows of B
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

print(C)




'''Numpy'''
import numpy as np

v4 = np.array([1,2,3,4])
v5 = np.array([5,6,7,8])

M1 = np.array([[3,4], 
                [7,8]])
M2 = np.array([[0,1],
                [1,1]])

# Dot product v4.v5 = 70
v6 = np.dot(v4,v5)
print(v6)

# Matrix addition
M3 = M1 + M2
print(M3)

# Matrix multimplication
M3 = np.matmul(M1,M2)
print (M3)


