import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

num_alternatives = int(input("Jumlah alternatif: "))
num_criteria = int(input("Jumlah kriteria: "))

data = np.zeros((num_alternatives, num_criteria))
for i in range(num_alternatives):
    for j in range(num_criteria):
        data[i, j] = float(input(f"Masukkan nilai Kriteria {j + 1} untuk Alternatif {i + 1}: "))

data_df = pd.DataFrame(data, columns=[f'Kriteria {i + 1}' for i in range(num_criteria)])

weights = []
for i in range(num_criteria):
    weight = float(input(f"Masukkan bobot Kriteria {i + 1} (antara 0 dan 1): "))
    weights.append(weight)

def min_max_scaling(data):
    return (data - data.min()) / (data.max() - data.min())

data_normalized = data_df.apply(min_max_scaling, axis=0)

def moora_score(data_normalized, weights):
    m, n = data_normalized.shape
    score = np.zeros(m)

    for i in range(m):
        numerator = 0
        denominator = 0
        for j in range(n):
            numerator += weights[j] * data_normalized.iloc[i, j]
            denominator += weights[j] * (data_normalized.iloc[i, j] ** 2)
        score[i] = numerator / np.sqrt(denominator)

    return score

alternatif_scores = moora_score(data_normalized, weights)

ranked_alternatives = np.argsort(alternatif_scores)[::-1] + 1

print("\nHasil Rangking Alternatif:")
for i, alternatif_index in enumerate(ranked_alternatives):
    print(f"Alternatif {alternatif_index}: {alternatif_scores[alternatif_index - 1]}")

plt.bar(range(1, num_alternatives + 1), alternatif_scores)
plt.xlabel("Alternatif")
plt.ylabel("Skor MOORA")
plt.title("Rangking Alternatif dengan Metode MOORA")
plt.show()

data_df.to_csv('data_alternatif.csv', index=False)
pd.DataFrame({'Bobot': weights}).to_csv('bobot_kriteria.csv', index=False)
pd.DataFrame({'Rangking': ranked_alternatives}).to_csv('rangking_alternatif.csv', index=False)
