from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


def plot(expr, x, y, var1, var2):
    X = np.linspace(int(x[0:x.find(':')]), int(x[x.find(':') + 1:]), 100)
    Y = np.linspace(int(y[0:y.find(':')]), int(y[y.find(':') + 1:]), 100)
    X, Y = np.meshgrid(X, Y)
    z = expr.substitute(X, Y, var1, var2)
    ax = plt.axes(projection='3d')
    ax.scatter(X, Y, z)# , 40, cmap='binary')
    plt.show()
