import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import symbols,sin,cos,exp,diff
t=symbols('t')

r=sp.Matrix([sp.exp(t),sp.exp(t)*sp.cos(t),sp.exp(t)*sp.sin(t)])
r_p=r.diff(t)
r_pp=r_p.diff(t)
r_ppp=r_pp.diff(t)
norm_rp=sp.sqrt(r_p.dot(r_p))
T=r_p/norm_rp
sp.pprint(T)


T_p=T.diff(t)
norm_Tp=sp.sqrt(T_p.dot(T_p))
N=T_p/norm_Tp
print("Normal")
sp.pprint(N)
B=T.cross(N)
print("Bionormal")
sp.pprint(B)
k=norm_Tp/norm_rp
print("Kappa")
sp.pprint(k)
crossing=r_p.cross(r_pp)
norm_crossing=sp.sqrt(crossing.dot(crossing))
teu=crossing.dot(r_ppp)/norm_crossing
print("teu")
sp.pprint(teu)
teu0=teu.subs({t:0})
sp.pprint(teu0)

#plot
t1=np.linspace(0,2*np.pi,100)
k_np=sp.lambdify(t,k,'numpy')
k1=k_np(t1)
plt.plot(t1,k1)
plt.xlabel("t")
plt.ylabel("curvative")
plt.show()

