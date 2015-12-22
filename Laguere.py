import numpy as np
import matplotlib.pyplot as plt
from scipy.special import * 

x = np.linspace(-5, 10, 1000)

plt.plot(x, eval_genlaguerre(4, 0, x))
plt.xlim(-5, 10)
plt.ylim(-10, 20)
plt.grid()
plt.show()
