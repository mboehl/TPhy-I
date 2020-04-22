import numpy as np
import matplotlib.pyplot as plt
from sympy import *


levels=list(np.linspace(1,10,20))

x = np.linspace(-1.1,1.1,200)
y = np.linspace(-1.1,1.1,200)


X,Y = np.meshgrid(x,y)
Z = 1/np.sqrt((X**2+Y**2))



fig, ax = plt.subplots()
plt.contour(X, Y, Z, levels)
ax.set_title("")
ax.set_xlim(left=-1.2, right=1.2)
ax.set_ylim(top=1.2, bottom=-1.2)

ax.set_aspect("equal")


x = np.hstack((np.arange(-1.2, -0.005, 0.1), np.arange(0.005,1.2,0.1)))
y = np.hstack((np.arange(-1.2, -0.005, 0.1), np.arange(0.005,1.2,0.1)))

X,Y = np.meshgrid(x,y)
U = -X/np.sqrt(X**2+Y**2)**3
V = -Y/np.sqrt(X**2+Y**2)**3

U = np.where(abs(V) > 6, 0, U)
V = np.where(abs(U) > 6, 0, V)
U = np.where(abs(U) > 6, 0, U)
V = np.where(abs(V) > 6, 0, V)

ax.set_xticks([-1.0,-0.5,0.0,0.5,1.0])
ax.set_yticks([-1.0,-0.5,0.0,0.5,1.0])
plt.quiver(X, Y, U, V, scale=50)
plt.show()


