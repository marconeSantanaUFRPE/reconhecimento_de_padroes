import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()