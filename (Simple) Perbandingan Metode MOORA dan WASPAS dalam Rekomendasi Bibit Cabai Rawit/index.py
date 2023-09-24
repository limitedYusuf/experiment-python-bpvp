# Import library yang diperlukan
import numpy as np

alternatives = ['Alternatif A', 'Alternatif B', 'Alternatif C', 'Alternatif D']

criteria = ['Harga', 'Kualitas', 'Produktivitas', 'Resistensi Hama']

waspas_weights = [0.3, 0.2, 0.3, 0.2]

criteria_values = np.array([
    [10, 8, 9, 7],
    [8, 9, 7, 8],
    [9, 7, 8, 9],
    [7, 8, 9, 6]
])

criteria_normalized = np.zeros_like(criteria_values, dtype=float)
for i in range(len(criteria)):
    max_value = max(criteria_values[:, i])
    min_value = min(criteria_values[:, i])
    criteria_normalized[:, i] = (criteria_values[:, i] - min_value) / (max_value - min_value)

# MOORA
moora_scores = np.sum(criteria_normalized * waspas_weights, axis=1)

# WASPAS
waspas_scores = np.sum(criteria_values * waspas_weights, axis=1)

moora_ranking = [x for _, x in sorted(zip(moora_scores, alternatives), reverse=True)]
waspas_ranking = [x for _, x in sorted(zip(waspas_scores, alternatives), reverse=True)]

print("Hasil Rekomendasi dengan Metode MOORA:")
for i, alt in enumerate(moora_ranking, start=1):
    print(f"{i}. {alt}")

print("\nHasil Rekomendasi dengan Metode WASPAS:")
for i, alt in enumerate(waspas_ranking, start=1):
    print(f"{i}. {alt}")
