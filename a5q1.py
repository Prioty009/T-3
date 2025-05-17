import numpy as np
data = np.loadtxt('ex2data1.txt', delimiter=',')
X, y = data[:, 0], data[:, 2]
m = len(y)
X_norm = (X - X.mean()) / X.std()
X_b = np.c_[np.ones(m), X_norm]
theta = np.zeros(2)
alpha, iterations = 0.01, 1500
def compute_cost(X, y, theta):
    errors = X @ theta - y
    return np.dot(errors, errors) / (2 * m)
def gradient_descent(X, y, theta, alpha, iterations):
    for _ in range(iterations):
        theta -= alpha * (X.T @ (X @ theta - y)) / m
    return theta
theta = gradient_descent(X_b, y, theta, alpha, iterations)
print("Learned theta:", theta)