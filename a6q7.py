import numpy as np

# Given values
S = 19              # Stock price
K = 20              # Strike price
C = 1               # Call option price
r = 0.03            # Risk-free interest rate (annual)
T = 4 / 12          # Time to maturity in years

# Put-Call Parity for European options
P = C + K * np.exp(-r * T) - S

print(f"European Put Option Price: ${P:.2f}")