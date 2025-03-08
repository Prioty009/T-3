import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint,solve_ivp
def f(y,t):
    return t*np.exp(3*t)-2*y
def exact_solution(t):
    return (1/5)*t*np.exp(3*t)-(1/25)*np.exp(3*t)+(1/25)*np.exp(-2*t)
t=np.linspace(0,1,11)
y0=0
y_odeint=odeint(f,y0,t).flatten()
solution=solve_ivp(lambda t,y:f(y,t),[0,1],[0],t_eval=t)
y_solve_ivp=solution.y.flatten()
exact=exact_solution(t)
Error_y_odeint=np.abs(exact-y_odeint)
Error_y_solve_ivp=np.abs(exact-y_solve_ivp)
print('t         y_odeint     y_solve_ivp      exact    Error_y_odeint     Error_y_solve_ivp ')
for i in range(len(t)):
    print(f'{t[i]:.1f}      {y_odeint[i]:.5f}      {y_solve_ivp[i]:.5f}           {exact[i]:.5f},          {Error_y_odeint[i]:.5f}        {Error_y_solve_ivp[i]:.5f}')
fig=plt.figure(figsize=(12,10))
plt.subplot(1,2,1)
plt.plot(t,exact,'k--',label='Exact Solution')
plt.plot(t,y_odeint, 'r',label='odeint Solution')
plt.plot(t,y_solve_ivp, 'b',label='solve ivp')
plt.xlabel('t')
plt.ylabel('solution')
plt.legend()
plt.subplot(1,2,2)
plt.plot(t,Error_y_odeint, 'r--',label='Error odeint Solution')
plt.plot(t,Error_y_solve_ivp, 'b',label='Error solve ivp')
plt.xlabel('t')
plt.ylabel('Error')
plt.legend()
plt.show()



     