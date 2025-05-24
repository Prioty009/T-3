import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.model_selection import learning_curve

# Generate dataset with non-linear relationship
np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = X * np.sin(X) + np.random.normal(scale=0.5, size=X.shape)

# Map features to polynomial terms (degree 5)
poly = PolynomialFeatures(degree=5)
X_poly = poly.fit_transform(X)

# Implement regularized linear regression
def train_polynomial_regression(X_poly, y, alpha):
    model = Ridge(alpha=alpha)
    model.fit(X_poly, y)
    return model

# Plot learning curves
def plot_learning_curve(X_poly, y, alpha):
    train_sizes, train_scores, cv_scores = learning_curve(
        Ridge(alpha=alpha), X_poly, y, cv=5, scoring="neg_mean_squared_error"
    )
    plt.plot(train_sizes, -np.mean(train_scores, axis=1), label="Training Error")
    plt.plot(train_sizes, -np.mean(cv_scores, axis=1), label="Cross-validation Error")
    plt.xlabel("Training set size")
    plt.ylabel("Error")
    plt.title(f"Learning Curve (alpha={alpha})")
    plt.legend()
    plt.show()

# Vary regularization parameter to observe bias-variance trade-off
alphas = [0.001, 0.01, 0.1, 1, 10]
for alpha in alphas:
    model = train_polynomial_regression(X_poly, y, alpha)
    plot_learning_curve(X_poly, y, alpha)

# Plot polynomial regression fit
plt.scatter(X, y, label="True Data")
plt.plot(X, model.predict(X_poly), color="red", label="Polynomial Regression Fit")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Polynomial Regression Fit")
plt.show()