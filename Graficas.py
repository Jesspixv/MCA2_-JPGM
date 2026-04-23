import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Inciso A ---
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111, projection='3d')
x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

# Despejando los ecuacions:
z1 = 3 * (1 - x - 0.5*y)
z2 = 4 * (0 - 0.5*x - (1/3)*y)
z3 = 5 * (0 - (1/3)*x - 0.25*y)

ax1.plot_wireframe(x, y, z1, color='blue', label='Ecuacion 1', alpha=0.6)
ax1.plot_wireframe(x, y, z2, color='red', label='Ecuacion 2', alpha=0.6)
ax1.plot_wireframe(x, y, z3, color='yellow', label='Ecuacion 3', alpha=0.6)
ax1.set_title("Sistema A")
ax1.legend()

# Inciso B 

plt.figure(figsize=(8, 6))
x1 = np.linspace(0, 10, 100)

# Despejando los ecuacions:
y_b1 = 10 - x1 - 1 - 1
y_b2 = (20 - 1.01*x1 - 1.03*1 - 1.04*1) / 1.02
y_b3 = (30 - (1.01**2)*x1 - (1.03**2)*1 - (1.04**2)*1) / (1.02**2)
y_b4 = (40 - (1.01**3)*x1 - (1.03**3)*1 - (1.04**3)*1) / (1.02**3)

plt.plot(x1, y_b1, label='Ecuacion 1')
plt.plot(x1, y_b2, label='Ecuacion 2')
plt.plot(x1, y_b3, label='Ecuacion 3')
plt.plot(x1, y_b4, label='Ecuacion 4')
plt.title("Sistema B")
plt.legend()
plt.grid(True)


# Inciso C
plt.figure(figsize=(8, 6))
xc = np.linspace(0.9, 1.1, 400) 
yc1 = (3 - xc) / 2
yc2 = (6.0001 - 2*xc) / 4.0001

plt.plot(xc, yc1, 'r-', label='x + 2y = 3', linewidth=3)
plt.plot(xc, yc2, 'b--', label='2x + 4.0001y = 6.0001', linewidth=1)
plt.title("Sistema C")
plt.legend()
plt.grid(True)


plt.show()