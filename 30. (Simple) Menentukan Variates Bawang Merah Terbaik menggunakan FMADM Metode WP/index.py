import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Varietas': ['A', 'B', 'C', 'D'],
    'Produktivitas': [0.8, 0.6, 0.7, 0.9],
    'Kualitas': [0.7, 0.9, 0.8, 0.6],
    'Resistensi': [0.6, 0.7, 0.9, 0.8]
})

bobot_atribut = {
    'Produktivitas': 0.33,
    'Kualitas': 0.33,
    'Resistensi': 0.34
}

normalized_data = data.copy()
for atribut in bobot_atribut.keys():
    normalized_data[atribut] = data[atribut] / data[atribut].sum()

fuzzy_weights = normalized_data.copy()
for atribut in bobot_atribut.keys():
    fuzzy_weights[atribut] = np.power(normalized_data[atribut], bobot_atribut[atribut])

fuzzy_weights['Fuzzy_WP'] = fuzzy_weights[list(bobot_atribut.keys())].prod(axis=1)
fuzzy_weights['Fuzzy_WP'] = fuzzy_weights['Fuzzy_WP'] / fuzzy_weights['Fuzzy_WP'].sum()
fuzzy_weights['Rank'] = fuzzy_weights['Fuzzy_WP'].rank(ascending=False, method='min')

best_variety = fuzzy_weights[fuzzy_weights['Rank'] == 1]['Varietas'].values[0]

print("Hasil Fuzzy Weighted Product (FWP) dan Ranking:")
print(fuzzy_weights[['Varietas', 'Fuzzy_WP', 'Rank']])
print(f"\nVarietas terbaik adalah {best_variety} dengan peringkat teratas dalam metode FMADM.")
