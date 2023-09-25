import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [2.0, 3.0],
    [2.5, 3.5],
    [3.0, 4.0],
    [4.0, 4.5],
    [8.0, 7.0],
    [9.0, 8.0],
    [8.5, 7.5],
    [9.5, 8.5],
    [5.0, 6.0],
    [5.5, 6.5]
])

k = 2

max_iterations = 100

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

initial_centers_idx = np.random.choice(data.shape[0], k, replace=False)
centers = data[initial_centers_idx]

for iteration in range(max_iterations):
    clusters = [[] for _ in range(k)]

    for point in data:
        distances = [euclidean_distance(point, center) for center in centers]
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx].append(point)

    new_centers = [np.mean(cluster, axis=0) for cluster in clusters]

    if np.all(np.array_equal(centers[i], new_centers[i]) for i in range(k)):
        break

    centers = new_centers

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for i, cluster in enumerate(clusters):
    cluster = np.array(cluster)
    plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i], label=f'Cluster {i+1}')

plt.scatter(np.array(centers)[:, 0], np.array(centers)[:, 1], c='black', marker='x', label='Centroids')
plt.title('Clustering K-Means')
plt.xlabel('Fitur 1')
plt.ylabel('Fitur 2')
plt.legend()
plt.show()
