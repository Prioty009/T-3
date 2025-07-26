import numpy as np
F0=60
K=60
sigma=0.3
r=0.08
T=0.5
n=2
dt=T/n
u=np.exp(sigma*np.sqrt(dt))
d=1/u
p=(np.exp(r*dt)-d)/(u-d)
discount=np.exp(-r*dt)
Fuu=F0*u**2
Fud=F0*u*d
Fdd=F0*d**2
Cuu=max(Fuu-K,0)
Cud=max(Fud-K,0)
Cdd=max(Fdd-K,0)
Cu=discount*(p*Cuu+(1-p)*Cud)
Cd=discount*(p*Cud+(1-p)*Cdd)
C=discount*(p*Cu+(1-p)*Cd)
print(f'European call:{C:.2f}')
print("if the call were American it is exercising early")

