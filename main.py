# %%
import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

lin = np.linspace(-3, 3, 100)
liny = list(map(lambda x : 1 / (1+x**2), lin))
plt.plot(lin, liny)

p0 = lambda x : (1/24)*x*(x+1)*(x-1)*(x-2)
p1 = lambda x : -(1/6)*x*(x-1)*(x+2)*(x-2)
p2 = lambda x : (1/4)*(x+1)*(x+2)*(x-1)*(x-2)
p3 = lambda x : -(1/6)*x*(x+1)*(x+2)*(x-2)
p4 = lambda x : (1/24)*x*(x+2)*(x-1)*(x+1)



lin = np.linspace(-3, 3, 100)
liny = list(map(lambda x : (1/5)*p0(x)
                + (1/2)*p1(x) + 1*p2(x)
                + (1/2)*p3(x) + (1/5)*p4(x), lin))
# %%
def reparti(a, b, n):
    li = []
    for i in range(n + 1):
        li.append(a+i*(b-a)/n)
    return li


fig = plt.figure()
re = reparti(-5, 5, 14)
plt.scatter(re, [0] * 15)
plt.scatter(re, list(map(lambda x : 1/(1+x**2), re)))

# %%
