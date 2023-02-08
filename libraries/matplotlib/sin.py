import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 300)
y = np.sin(x)

plt.plot(x , y, 'r-', label='sin(x)') # r- draws a red line
plt.ylim(-1.25, 1.25)
plt.legend()
plt.show()
