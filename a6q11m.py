import numpy as np

# Parameters
S0 = 484            # Initial index level
K = 480             # Strike price
r = 0.10            # Risk-free rate
q = 0.03            # Dividend yield
sigma = 0.25        # Volatility
T = 2 / 12          # Time to expiry in years (2 months)
N = 4               # Number of steps
dt = T / N          # Time per step

# Binomial model parameters
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp((r - q) * dt) - d) / (u - d)
discount = np.exp(-r * dt)

# Initialize stock price tree
stock_tree = np.zeros((N+1, N+1))
for j in range(N+1):
    for i in range(j+1):
        stock_tree[i, j] = S0 * (u**(j - i)) * (d**i)

# Initialize option value tree
option_tree = np.zeros((N+1, N+1))

# Set terminal payoffs at maturity for American put
for i in range(N+1):
    option_tree[i, N] = max(K - stock_tree[i, N], 0)

# Backward induction with early exercise for American put
for j in reversed(range(N)):
    for i in range(j+1):
        hold = discount * (p * option_tree[i, j+1] + (1 - p) * option_tree[i+1, j+1])
        exercise = K - stock_tree[i, j]
        option_tree[i, j] = max(hold, exercise)

# Final result
print(f"Estimated American Put Option Value: ${option_tree[0, 0]:.2f}")
