# %%
from matplotlib import pyplot as plt 
import numpy as np

def moindres_carres(X, Y, m):
    C = np.vander(X, m+1, increasing=True)
    tC = C.transpose()

    V = np.linalg.solve(tC @ C, tC @ Y)
    
    return np.polynomial.Polynomial(V)

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

X = np.array((-1, 0, 1, 2))
Y = np.array((-2, 1, 3, 1))
plt.scatter(X, Y, label="Nuage de points")


L = np.linspace(-2, 3, 1000)

B = lagrange(X, Y)
plt.plot(L, B(L), label=f"Interpolation de Lagrange")

o = 2
pol = moindres_carres(X, Y, o)
plt.plot(L, pol(L), label=f"Moindres carrés d'ordre {o}")

plt.legend()
# %%