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