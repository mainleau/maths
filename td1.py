#%%
import matplotlib.pyplot as plt
import math

def plot(data):
    plt.plot(data)
    plt.figure()
    plt.scatter(data, [0]*len(data), 20)

def dichotomie(f, a, b, eps, maxit):
    n = 1
    hist = []

    while b-a >= eps and n <= maxit:
        if f(a)*f((a+b)/2) < 0:
            b = (a+b)/2
            hist.append(b)
        elif f(b)*f((a+b)/2) < 0:
            a = (a+b)/2
            hist.append(a)
        else:
            break
        n += 1

    return a, b, hist

#%%

p = dichotomie(lambda x : x ** 2 - 2, 1, 2, 1e-8, 27)
print(p)

#%%

def pointfixe(f, x, eps): 
    y = f(x)
    n = 0
    hist = []

    while abs(y - x) > 0.5*eps and n < 100:
        n = n + 1
        x = y
        y = f(x)
        hist.append(y)
    return x, y, hist

p = pointfixe(lambda x : math.sqrt(-x+2), 2, 1e-8)

#%%

def itere(f, li):
    for x in li:
        res = [x]
        for i in range(10):
            res.append(f(res[-1]))
        print(res)


# %%

itere(lambda x : x**2 + x - 2, [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2])
# %%

def newton(f, fp, eps):
    x = -100
    xp = -100
    n = 0
    while (abs(x-xp) >= eps or n == 0) and n <= 100:
        xp = x
        x = x - f(x)/fp(x)
        n = n + 1
    return xp, x

p = newton(lambda x : 3*x**2 + 9*x + 6, lambda x : 6*x + 9, 1e-1)

print(p)
# %%

def sec(f, x0, x1):
    x1 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    n = 0
    while n <= 210:
        x1p = x1
        x1 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1p
        n = n + 1
        print(x0, x1)
    return x0, x1

p = sec(lambda x : x**2 + x + 1, 1, 2)

print(p)
# %%
