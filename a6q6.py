import numpy as np
import matplotlib.pyplot as plt

# Parameters
strike_call = 45
strike_put = 40
premium_call = 3
premium_put = 4
total_premium = premium_call + premium_put

# Asset price range at expiration
S = np.linspace(30, 60, 500)

# Payoff calculations
call_payoff = np.maximum(S - strike_call, 0)
put_payoff = np.maximum(strike_put - S, 0)
total_payoff = call_payoff + put_payoff

# Profit = Payoff - Total Premium Paid
profit = total_payoff - total_premium

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(S, profit, label='Profit', color='purple')
#plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(strike_put, linestyle='--', color='r', label='Put Strike ($40)')
plt.axvline(strike_call, linestyle='--', color='b', label='Call Strike ($45)')
plt.title('Profit Diagram: Long Strangle Strategy')
plt.xlabel('Stock Price at Expiration ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.legend()
plt.show()