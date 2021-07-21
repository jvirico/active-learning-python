import numpy as np
import matplotlib.pyplot as plt

# v_i = initial velocity
# x_i = initial position
# t   = time
# a   = acceleration
def getPosition(a,v_i,x_i,t):
    return ((0.5)*a * t**2 + v_i * t + x_i)

print (getPosition(1.0,1.0,0.0,10.0))

positions = np.zeros(100)
for i in range(100):
    positions[i] = getPosition(1.0,1.0,0.0,i)

#pos_round = np.around(positions,decimals=1)
print (positions.astype(int))

plt.plot(positions)
plt.show()
