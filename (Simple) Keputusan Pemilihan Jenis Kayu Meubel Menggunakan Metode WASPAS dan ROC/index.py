import numpy as np

# Data
kriteria = np.array([
    [500, 4, 9],  # Kayu A
    [600, 7, 6],  # Kayu B
    [700, 8, 7],  # Kayu C
])

# Bobot
bobot = np.array([0.4, 0.3, 0.3])

# WASPAS
def waspas(data, bobot):
    normalized_data = data / np.max(data, axis=0)
    weighted_data = normalized_data * bobot
    score = np.sum(weighted_data, axis=1)
    return score

waspas_scores = waspas(kriteria, bobot)

# ROC
def roc(data):
    ranks = np.argsort(data, axis=0)
    centroid = np.mean(ranks, axis=1)
    return centroid

roc_scores = roc(kriteria)

print("Hasil Metode WASPAS:")
for i, score in enumerate(waspas_scores):
    print(f"Kayu {chr(65+i)}: {score:.2f}")

print("\nHasil Metode ROC:")
roc_rankings = np.argsort(roc_scores)
for i, rank in enumerate(roc_rankings):
    print(f"Kayu {chr(65+rank)}: Ranking {i+1}")
