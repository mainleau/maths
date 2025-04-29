# %%

import numpy as np
from matplotlib import pyplot as plt

x = Symbol('x')

t0 = 4
T = 40
N = 10

y0 = 0
y = np.zeros(N)

R = np.linspace(t0, t0 + T, 10000)

partition = np.linspace(t0, t0 + T, N)
h = partition[1] - partition[0]

plt.plot(R, R**3)
plt.scatter(partition, np.zeros(N), c='r')

for i in range(0, 9):
    y[i+1] = y[i] + h * 1
# %%