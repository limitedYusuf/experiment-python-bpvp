import numpy as np
import matplotlib.pyplot as plt

def update_centers(data, u, m):
    um = u ** m
    new_centers = np.dot(data.T, um) / np.sum(um, axis=0, keepdims=True)
    return new_centers.T

def calculate_membership(data, centers, m):
    distances = np.linalg.norm(data[:, np.newaxis, :] - centers, axis=2)
    return 1.0 / np.sum((distances[:, :, np.newaxis] / distances[:, np.newaxis, :]) ** (2 / (m - 1)), axis=2)

def calculate_fuzzy_criterion(data, centers, u, m):
    distances = np.linalg.norm(data[:, np.newaxis, :] - centers, axis=2)
    return np.sum((u ** m) * distances)

data = np.array([[x, y] for x, y in zip(np.random.rand(100) * 10, np.random.rand(100) * 10)])

n_clusters = 3
m = 2
max_iters = 100
epsilon = 0.01

min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)
centers = np.random.rand(n_clusters, data.shape[1]) * (max_values - min_values) + min_values

for iteration in range(max_iters):
    u = calculate_membership(data, centers, m)
    
    new_centers = update_centers(data, u, m)
    criterion = np.linalg.norm(new_centers - centers)
    
    if criterion < epsilon:
        break
    
    centers = new_centers

labels = np.argmax(u, axis=1)

plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='o', c='red', s=100)
plt.title('Clustering Mutu CPO dengan FCM')
plt.show()

print("Pusat Cluster:")
print(centers)
