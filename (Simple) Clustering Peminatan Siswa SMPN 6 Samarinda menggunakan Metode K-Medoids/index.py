import numpy as np

data = np.array([
    [75, 80],   # Data siswa 1
    [85, 90],   # Data siswa 2
    [70, 75],   # Data siswa 3
    [90, 95],   # Data siswa 4
    [65, 70],   # Data siswa 5
    [80, 85]    # Data siswa 6
])

n_clusters = 2

initial_medoids_idx = np.random.choice(len(data), n_clusters, replace=False)
medoids = data[initial_medoids_idx]

def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def assign_to_clusters(data, medoids):
    clusters = [[] for _ in range(n_clusters)]
    for point in data:
        distances = [distance(point, medoid) for medoid in medoids]
        closest_medoid_idx = np.argmin(distances)
        clusters[closest_medoid_idx].append(point)
    return clusters

def calculate_total_cost(clusters, medoids):
    total_cost = 0
    for i, cluster in enumerate(clusters):
        for point in cluster:
            total_cost += distance(point, medoids[i])
    return total_cost

max_iterations = 100
for _ in range(max_iterations):
    clusters = assign_to_clusters(data, medoids)
    
    new_medoids = np.copy(medoids)
    for i, cluster in enumerate(clusters):
        cluster_costs = [calculate_total_cost([cluster], [point]) for point in cluster]
        best_medoid_idx = np.argmin(cluster_costs)
        new_medoids[i] = cluster[best_medoid_idx]
    
    if np.array_equal(medoids, new_medoids):
        break
    
    medoids = new_medoids

for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}:")
    for j, data_point in enumerate(cluster):
        print(f"  Siswa {j + 1}: {data_point}")
