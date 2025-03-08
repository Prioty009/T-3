import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp
def f(y,t):
    return 1+(t-y)**2
def exact_solution(t):
    return t+(1/(1-t))
y0 = 1
t = np.linspace(2, 3, 11)
y_odeint = odeint(f, y0, t).flatten()
solution = solve_ivp(lambda t, y: f(y,t), [2,3], [1], t_eval=t)
y_solve_ivp = solution.y.flatten()
y_exact = exact_solution(t)
error_odeint = np.abs(y_exact - y_odeint)
error_solve_ivp = np.abs(y_exact - y_solve_ivp)
print('t_n   y_n(odeint)    y_n(solve_ivp)   Exact y_n  Error(odeint)  Error(solve_ivp)')
for i in range(len(t)):
    print(f"{t[i]:.1f}     {y_odeint[i]:.5f}       {y_solve_ivp[i]:.5f}          {y_exact[i]:.5f}     {error_odeint[i]:.5f}    {error_solve_ivp[i]:.5f}")
plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
plt.plot(t, y_exact, 'k--', label='Exact solution')
plt.plot(t, y_odeint, 'r--', label='odeint solution')
plt.plot(t, y_solve_ivp, 'b-', label='solve_ivp solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Solutions')
plt.subplot(1, 2, 2)
plt.plot(t, error_odeint, 'r--', label='odeint error')
plt.plot(t, error_solve_ivp, 'b-', label='solve_ivp error')
plt.xlabel('t')
plt.ylabel('Error')
plt.legend()
plt.title('Errors')
plt.show()