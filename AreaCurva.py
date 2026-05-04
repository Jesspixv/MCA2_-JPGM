import numpy as np
import matplotlib.pyplot as plt

# Ejercicio1
plt.figure(figsize=(10, 5))

#Intervalos 
x1 = np.linspace(-np.pi/3, np.pi/3, 500)

y_superior = 8 * np.cos(x1)
y_inferior = 1 / (np.cos(x1)**2) 

plt.subplot(1, 2, 1)
plt.plot(x1, y_superior, 'b-', label=r'$y = 8\cos(x)$')
plt.plot(x1, y_inferior, 'y-', label=r'$y = \sec^2(x)$')


plt.fill_between(x1, y_inferior, y_superior, color='gray', alpha=0.3, label='Área en el intervalo')

plt.title(' (Ejercicio 1 )  Área entre curvas')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# ................ #

# Ejercicio2
a = 1 
t = np.linspace(0, 2 * np.pi, 1000)

# Ecuaciones
x_p = a * (2 * np.cos(t) - np.cos(2*t))
y_p = a * (2 * np.sin(t) - np.sin(2*t))

plt.subplot(1, 2, 2)
plt.plot(x_p, y_p, 'g-', label='Cardiode')


t_superior = np.linspace(0, np.pi, 500)
x_fill = a * (2 * np.cos(t_superior) - np.cos(2*t_superior))
y_fill = a * (2 * np.sin(t_superior) - np.sin(2*t_superior))
plt.fill_between(x_fill, 0, y_fill, color='green', alpha=0.2, label='Área (0 a $\pi$)')

plt.axhline(0, color='black', linewidth=1) 
plt.axvline(0, color='black', linewidth=1) 
plt.title(' (Ejercicio 2 ) Cardiode ')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.legend()
plt.axis('equal') 
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()