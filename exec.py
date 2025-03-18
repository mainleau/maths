# %%
import numpy as np
from matplotlib import pyplot as plt
from functions import moindres_carres, lagrange

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