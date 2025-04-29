#%%
import matplotlib.pyplot as plt
import numpy as np
from functions import euler_explicite

f = lambda t, y : np.cos(t)

plt.figure()

for i in range(1, 10):
    x, y = euler_explicite(f, y0=0, t0=0, t0T=5, h=1/i)
    plt.plot(x, y, c='b')

plt.plot(x, y, c='r')
plt.plot(x, np.sin(x), c='g')
plt.show()
# %%
