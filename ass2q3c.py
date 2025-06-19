import sympy as sp
import numpy as np
from sympy  import symbols,cos,sin,tan,diff
x,y,z,theta,X,Y,Z=symbols('x,y,z,theta,X,Y,Z')
w=sp.sqrt(X**2+Y**2+Z**2)
w_x=w.diff(X)
w_y=w.diff(Y)
w_z=w.diff(Z)
x=sp.cos(theta)
y=sp.sin(theta)
z=sp.tan(theta)
xtheta=x.diff(theta)
ytheta=y.diff(theta)
ztheta=z.diff(theta)
w_xtheta=w_x.subs({X:x,Y:y,Z:z})
w_ytheta=w_y.subs({X:x,Y:y,Z:z})
w_ztheta=w_z.subs({X:x,Y:y,Z:z})
cf=w_xtheta*xtheta+w_ytheta*ytheta+w_ztheta*ztheta
sp.pprint(cf)
cf_np=sp.lambdify(theta,cf,'numpy')
derivative=cf_np(np.pi/4)
print("dw/dtheta:",derivative)


