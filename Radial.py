import numpy as np
import matplotlib.pyplot as plt
from scipy.special import * 
x = np.linspace(-5, 20, 1000)
n = 3
l = 2
R = np.exp(-x/n) * ((2*x/n)**l) * eval_genlaguerre(n-l-1, 2*l+1, 2*x/n)
plt.plot(x, R)
plt.xlim(0, 20)
plt.ylim(-1, 4)
plt.grid()
plt.show()
