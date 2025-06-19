import sympy as sp
from sympy import symbols,cos,sin,diff
x=symbols('x')
y=symbols('y')
f=y**2*sp.cos(x-y)
fx=sp.diff(f,x)
fxx=sp.diff(fx,x)
fy=sp.diff(f,y)
fyy=sp.diff(fy,y)
fxy=sp.diff(fx,y)
fyx=sp.diff(fy,x)
u=f
v=0
ux=sp.diff(u,x)
uy=sp.diff(u,y)
vx=sp.diff(v,x)
vy=sp.diff(v,y)
print("fxx:",fxx)
print("fyy:",fyy)
laplaci=sp.simplify(fxx+fyy)
if laplaci==0:
    print("satisfies laplace equation")
else:
    print(" not satisfies laplace equation")

cr1=sp.simplify(ux-vy)
cr2=sp.simplify(uy+vx)    
if cr1==0 and cr2==0:
    print("satisfies CRE")
else:
    print(" not satisfies CRE")
print("fxy:",fxy) 
print("fyx:",fyx) 
if sp.simplify(fxy-fyx)==0:
    print("fxy and fyx is equal")  
else:
    print("fxy and fyx is not equal")  



