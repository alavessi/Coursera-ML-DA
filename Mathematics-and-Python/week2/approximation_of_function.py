import math
import numpy as np
from scipy import linalg
from matplotlib import pyplot as plt

def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

x1 = [1, 15]
A1 = [[1, x1[i]] for i in range(2)]
b1 = list(map(f, x1))
sol1 = linalg.solve(A1, b1)
plt.plot(list(map(f, np.arange(1, 16))))

x2 = [1, 8, 15]
A2 = [[1, x2[i], x2[i] ** 2] for i in range(3)]
b2 = list(map(f, x2))
sol2 = linalg.solve(A2, b2)
plt.plot(list(map(lambda x: sol2[0] + sol2[1] * x + sol2[2] * x ** 2, np.arange(1, 16))))

x3 = [1, 4, 10, 15]
A3 = [[1, x3[i], x3[i] ** 2, x3[i] ** 3] for i in range(4)]
b3 = list(map(f, x3))
sol3 = linalg.solve(A3, b3)
plt.plot(list(map(lambda x: sol3[0] + sol3[1] * x + sol3[2] * x ** 2 + sol3[3] * x ** 3, np.arange(1, 16))))