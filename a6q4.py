import numpy as np

# Given values
S0 = 40             # Initial stock price
r = 0.10            # Risk-free rate (annual, continuously compounded)
T = 1.0             # Time to maturity in years
F = S0 * np.exp(r * T)  # Forward price (part a)

# Part (a): Initial forward price and contract value
print("Part (a): Initial contract")
print(f"Forward Price F(0): ${F:.2f}")
print("Initial Value of Forward Contract: $0.00 (by definition)")

# Part (b): Six months later
t = 0.5             # Time elapsed in years
St = 45             # Stock price at t = 0.5

# Forward price at t = 0.5 for delivery at T = 1.0
F_t = St * np.exp(r * (T - t))

# Value of the forward contract at time t
value_forward = St - F* np.exp(-r * (T - t))

print("\nPart (b): After 6 months")
print(f"Forward Price F(0.5): ${F_t:.2f}")
print(f"Value of Forward Contract: ${value_forward:.2f}")