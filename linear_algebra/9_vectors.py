'''
    Resource:
        https://www.amazon.es/Linear-Algebra-Coding-Python-application-ebook/dp/B08CT47RL3
        page 11
'''

import numpy as np
import pandas as pd

## Exercise 1:
# computing the length of point b

b_len = (5**2+3**2)**0.5
print(round(b_len,2))

# computing distances of all points at once
k = [-3,5]
b = [5,3]
r = [-2,-4]
g = [3,-4]

P = np.array([k,b,r,g])
print(P)

D = [(P[i,0]**2+P[i,1]**2)**0.5 for i in range(4)]
print(D)
# matrix concatenation using numpy
PD = np.c_[P,D]
# row-col annotations using Pandas DataFrame
PD_ = pd.DataFrame(PD)
PD_.columns = ['x','y','distance']
PD_.index = ['k','b','r','g']
print(PD_)

