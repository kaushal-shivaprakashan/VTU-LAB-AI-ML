import numpy as np
import matplotlib.pyplot as plt

def local_regression(x0, X, Y, tau):
    x0 = [1, x0]   
    X = [[1, i] for i in X]
    X = np.asarray(X)
    xw = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau))
    beta = np.linalg.pinv(xw @ X) @ xw @ Y @ x0  
    return beta    

def draw(tau):
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
    plt.plot(X, Y, 'o', color='black')
    plt.plot(domain, prediction, color='red')
    plt.show()

X = np.linspace(-3, 3, num=1000)
domain = X
Y = np.log(np.abs(X ** 2 - 1) + .5)

draw(10)
draw(0.1)
draw(0.01)
draw(0.001)
____________________________________________________________________________________________

methord 2



import numpy as np
import math
x = np.linspace(0, 2 * math.pi, 100)
y = np.sin(x) + 0.3 * np.random.randn(100)

import statsmodels.api as sm
lowess = sm.nonparametric.lowess(y, x, frac=.3)
lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]

from scipy.interpolate import interp1d
f = interp1d(lowess_x, lowess_y, bounds_error=False)

xnew = [i/10. for i in range(100)]
ynew = f(xnew)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.plot(xnew, ynew)
plt.show()
