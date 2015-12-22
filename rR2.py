import numpy as np
import matplotlib.pyplot as plt
from scipy.special import *
x = np.linspace(-5, 25, 1000)
n = 3
l = 1
R = np.exp(-x/n) * ((2*x/n)**l) * eval_genlaguerre(n-l-1, 2*l+1, 2*x/n)
plt.plot(x, x**2 * R**2)
plt.xlim(0, 25)
plt.ylim(-0.1, 50)
plt.grid()
plt.show()
