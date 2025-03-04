#%%
import numpy as np
from matplotlib import pyplot as plt

def evclassique(seq, x):
    r = 0
    for i in range(len(seq)):
        r += seq[i] * x**i
    return r

def evhorner(seq, x):
    r = 0
    for i in range(len(seq) - 1, -1, -1):
        r = x * r + seq[i]
    return r

seq = np.random.randint(-10, 10, 5)
evc = evclassique(seq, 4)
evh = evhorner(seq, 4)
print(seq, evc, evh)

#%%
def lagrange(seq):
    n = len(seq)
    X = np.polynomial.Polynomial((0, 1))

    base = []

    for i in range(n):
        p = 1

        for j in range(n):
            if i != j:
                p *= (X-seq[j])/(seq[i]-seq[j])
        base.append(p)

    return base

def lagrange(x, y):
    n = len(x)
    X = np.polynomial.Polynomial((0, 1))

    s = 0

    for i in range(n):
        p = 1

        for j in range(n):
            if i != j:
                p *= (X-x[j])/(x[i]-x[j])
        s += y[i] * p

    return s

def coordnewton(c,y):
    l = len(c)
    coord = []
    y_old = y
    coord.append(y_old[0])

    for i in range(l-1):
        y_new = []
        for j in range(len(y_old)-1):
            y_new.append((y_old[j+1]-y_old[j])/(c[j+i+1]-c[j]))

        y_old = y_new
        coord.append(y_old[0])

    return coord

def coordnewtonlo(x, y):
    n = len(x)

    coords =  [x[0]]

    for i in range(n):
        pass

def interpolnewton(c, y):
    X = np.polynomial.Polynomial(coef=(0,1))
    n = len(c)
    coord = coordnewton(c,y)

    p = coord[n-1]
    if n > 1:
        for i in range(n-1, -1, -1):
            p = coord[i] + (X-c[i])*p
    return p

def newton(x, y):
    n = len(x)
    for h in range (1, n):
        x0 = x[1:h]
        y0 = y[1:h]
        a = y0[:]
        if h > 1:
            for i in range(1, h):
                for j in range(0, h-i):
                    a[j] = (a[j+1] - a[j])/(x0[j+i] - x0[j])
            print(a[0])


x, y = [-1, 0, 1, 2], [-1, 1, 0, 0]

x0 = np.array(x)
y0 = np.array(y)

x1 = np.linspace(-2, 3, 50)
y1 = lagrange(x, y)(x1)

plt.plot(x0, y0, '.', x1, y1, '-')
plt.ylim(-10, 10)

# %%

interpolnewton([-1, 0, 1, 2], [-1, 1, 0, 0])

# %%
