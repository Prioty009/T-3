import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from scipy.optimize import minimize
np.random.seed(0)
m = 100
X = np.random.uniform(-1, 1, (m, 2))
y = ((X[:,0]**2 + X[:,1]**2 + 0.3*np.random.randn(m)) < 0.8).astype(int)
poly = PolynomialFeatures(6)
X_poly = poly.fit_transform(X)
def sigmoid(z): return 1 / (1 + np.exp(-z))
def cost(theta, X, y, l):
    h = sigmoid(X @ theta)
    reg = (l / (2 * len(y))) * np.sum(theta[1:]**2)
    return -np.mean(y*np.log(h) + (1-y)*np.log(1-h)) + reg
def grad(theta, X, y, l):
    h = sigmoid(X @ theta)
    g = X.T @ (h - y) / len(y)
    g[1:] += (l / len(y)) * theta[1:]
    return g
lambdas = [0, 1, 100]
thetas = [minimize(cost, np.zeros(X_poly.shape[1]), args=(X_poly, y, l), jac=grad, method='TNC').x for l in lambdas]

def plot_boundary(theta, X, y, poly, l):
    u = v = np.linspace(-1.5, 1.5, 300)
    Z = np.array([poly.transform([[x, y]]) @ theta for x in u for y in v]).reshape(len(u), len(v)).T
    plt.contourf(u, v, Z > 0, cmap='RdYlGn', alpha=0.7)
    plt.contour(u, v, Z, levels=[0], colors='k', linewidths=0.7)
    plt.scatter(X[y==0][:,0], X[y==0][:,1], c='r', label='Fail')
    plt.scatter(X[y==1][:,0], X[y==1][:,1], c='g', label='Pass')
    plt.title(f"Lambda = {l}")
    plt.xlabel('Test 1'); plt.ylabel('Test 2')
    plt.legend()
    plt.xlim(-1.5, 1.5); plt.ylim(-1.5, 1.5)
plt.figure(figsize=(15, 4))
for i, l in enumerate(lambdas):
    plt.subplot(1, 3, i+1)
    plot_boundary(thetas[i], X, y, poly, l)
plt.tight_layout()
plt.show()

print("\n--- Discussion of Results ---\n"
      "We trained logistic regression with polynomial features of degree 6.\n"
      "Models were trained with regularization lambdas 0, 1, and 100.\n\n"
      "1. Lambda = 0 (No Regularization):\n"
      "   - Complex boundary, overfitting training data.\n"
      "2. Lambda = 1 (Moderate Regularization):\n"
      "   - Smooth boundary, good balance of fit and generalization.\n"
      "3. Lambda = 100 (High Regularization):\n"
      "   - Very simple boundary, underfitting the data.\n\n"
      "Regularization helps prevent overfitting by penalizing large coefficients.\n"
      "Choosing the right lambda balances bias and variance.")