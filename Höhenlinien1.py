import numpy as np
import matplotlib.pyplot as plt
from sympy import *


fig, ax = plt.subplots()

ax.set_title("")
ax.set_xlim(left=-1.2,right=1.2)
ax.set_ylim(top=1.2,bottom=-1.2)
ax.set_aspect("equal")

x = np.hstack((np.arange(-1.2, -0.005, 0.1),np.arange(0.005,1.2,0.1)))
y = np.hstack((np.arange(-1.2, -0.005, 0.1),np.arange(0.005,1.2,0.1)))
X,Y = np.meshgrid(x,y)


#U = (-2*np.cos(np.arctan(Y/X)/((X**2+X**(1.5)))))
U = -2*x**2+y**2/(X**2+Y**2)**(5/2)
#V = (-np.sin(np.arctan(Y/X)/(X**2+Y**2)))
V = -3*X*Y/(X**2+Y**2)**(5/2)


U = np.where(abs(V) > 6, 0, U)
V = np.where(abs(U) > 6, 0, V)
U = np.where(abs(U) > 6, 0, U)
V = np.where(abs(V) > 6, 0, V)


ax.set_xticks([-1.0,-0.5,0.0,0.5,1.0])
ax.set_yticks([-1.0,-0.5,0.0,0.5,1.0])
plt.quiver(X, Y, U, V,scale=100)
levels=list(np.linspace(-2,2,50))


x=np.linspace(-1.1,1.1,100)
y=np.linspace(-1.1,1.1,100)


X,Y = np.meshgrid(x,y)
Z= -X/(X**2+Y**2)**1.5

plt.contour(X,Y,Z,levels)



plt.show()


