import numpy as np
import matplotlib.pyplot as plt

def linear_regression(X, y):
    n = len(X)
    
    mean_x = np.mean(X)
    mean_y = np.mean(y)
    
    num = 0
    den = 0
    for i in range(n):
        num += (X[i] - mean_x) * (y[i] - mean_y)
        den += (X[i] - mean_x) ** 2
    
    b = num / den
    a = mean_y - b * mean_x
    
    return a, b

def predict(a, b, X_new):
    return a + b * X_new

X = np.array([1, 2, 3, 4, 5]) 
y = np.array([10, 15, 20, 25, 30]) 

X_train, X_test = X[:3], X[3:]
y_train, y_test = y[:3], y[3:]

a, b = linear_regression(X_train, y_train)

y_pred = [predict(a, b, x) for x in X_test]

mean_y_test = np.mean(y_test)
sst = sum((y_test - mean_y_test) ** 2)
sse = sum((y_test - y_pred) ** 2)
r_squared = 1 - (sse / sst)

print(f"Koefisien a: {a}")
print(f"Koefisien b: {b}")
print(f"R-squared: {r_squared}")

plt.scatter(X, y, label='Data Penjualan')
plt.plot(X, a + b * X, color='red', label='Garis Regresi')
plt.xlabel('Harga Kopi Aren')
plt.ylabel('Penjualan Kopi Aren')
plt.legend()
plt.show()
