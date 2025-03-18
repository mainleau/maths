# %%

import numpy as np
from matplotlib import pyplot as plt
import time
import math

a, b = -5, 5
f = lambda x : 1/(1+x**2)

n = 10

plt.figure()
c = np.linspace(a, b, n+1)
y = list(map(f, c))

plt.scatter(c, y)
plt.plot(c, y)
plt.show()


# %%