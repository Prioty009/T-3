import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols,diff,sin,cos
x,y=symbols('x y')
T=3*x**2*y
gradT=sp.Matrix([diff(T,x),diff(T,y)])
gradT0=gradT.subs({x:-1,y:3/2})
print("gradient:")
sp.pprint(gradT0)
v0=sp.Matrix([-1,-1/2])
v0=v0/v0.norm()
dir_div=gradT0.dot(v0)
print("directional derivative:")
sp.pprint(dir_div)
#plot


dir_div=gradT.dot(v0)
dir_div_np=sp.lambdify((x,y),dir_div,'numpy')
x_vals=np.linspace(-2,0,100)
y_vals=np.linspace(0,2,100)
X,Y=np.meshgrid(x_vals,y_vals)
D_val=dir_div_np(X,Y)

fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111,projection='3d')
ax.plot(X,Y,D_val,color='g')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('value')
plt.show()


fig=plt.figure(figsize=(10,8))
ax2=fig.add_subplot(122)
ax2.contour(X,Y,D_val,color='b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.tight_layout()

plt.show()

