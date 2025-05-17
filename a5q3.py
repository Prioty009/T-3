import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
m = 90
X = np.column_stack((np.random.randint(30, 100, m), np.random.randint(30, 100, m)))
y = ((0.5*X[:,0] + 0.7*X[:,1] + 5*np.random.randn(m)) > 80).astype(int)
X_norm = (X - X.mean()) / X.std()
X_b = np.c_[np.ones(m), X_norm]


def sigmoid(z): return 1/(1+np.exp(-z))
def cost(X,y,theta): return -np.mean(y*np.log(sigmoid(X@theta)) + (1-y)*np.log(1-sigmoid(X@theta)))
def grad_desc(X,y,theta,a,iters):
    for _ in range(iters):
        theta -= a * X.T @ (sigmoid(X@theta)-y)/m
    return theta
theta = np.zeros(X_b.shape[1])
theta = grad_desc(X_b, y, theta, 0.1, 1000)
print("Optimal theta:", theta)


x1_range = np.linspace(X[:,0].min()-5, X[:,0].max()+5, 300) 
x2_range = np.linspace(X[:,1].min()-5, X[:,1].max()+5, 300)
xx1, xx2 = np.meshgrid(x1_range, x2_range)
grid = np.c_[xx1.ravel(), xx2.ravel()]
grid_norm = (grid - X.mean()) / X.std()
grid_b = np.c_[np.ones(grid.shape[0]), grid_norm]
probs = sigmoid(grid_b @ theta).reshape(xx1.shape)


plt.contourf(xx1, xx2, probs >= 0.5, cmap='RdYlGn', alpha=0.7)
plt.contour(xx1, xx2, probs, levels=[0.5], colors='k', linewidths=1.5)
plt.scatter(X[y==0][:,0], X[y==0][:,1], c='r', label='Not Admitted')
plt.scatter(X[y==1][:,0], X[y==1][:,1], c='g', label='Admitted')
plt.xlabel('Exam 1 Score'); plt.ylabel('Exam 2 Score')
plt.legend(); plt.show()
preds = (sigmoid(X_b @ theta) >= 0.5).astype(int)
print(f"Training Accuracy: {np.mean(preds == y)*100:.2f}%") 