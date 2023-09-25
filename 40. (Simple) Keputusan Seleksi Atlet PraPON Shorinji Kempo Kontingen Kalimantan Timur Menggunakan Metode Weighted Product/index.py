import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nama Atlet': ['Atlet A', 'Atlet B', 'Atlet C', 'Atlet D'],
    'Usia': [25, 27, 24, 26],
    'Prestasi': [90, 88, 85, 92],
    'Pengalaman': [5, 6, 4, 7]
}

bobot = {
    'Usia': 0.3,
    'Prestasi': 0.4,
    'Pengalaman': 0.3
}

df = pd.DataFrame(data)

def normalize_data(df):
    df_norm = df.copy()
    for column in df_norm.columns[1:]:
        min_val = df_norm[column].min()
        max_val = df_norm[column].max()
        df_norm[column] = (df_norm[column] - min_val) / (max_val - min_val)
    return df_norm

df_normalized = normalize_data(df)

def weighted_product(row):
    return np.prod(np.power(row[1:], [bobot[col] for col in df_normalized.columns[1:]]))

df_normalized['Weighted Product'] = df_normalized.apply(weighted_product, axis=1)

best_atlet = df_normalized[df_normalized['Weighted Product'] == df_normalized['Weighted Product'].max()]

print("Hasil Seleksi Atlet PraPON Shorinji Kempo Kontingen Kalimantan Timur:")
print(df_normalized)
print("\nAtlet Terbaik:")
print(best_atlet[['Nama Atlet', 'Weighted Product']])

plt.figure(figsize=(10, 6))
plt.bar(df_normalized['Nama Atlet'], df_normalized['Weighted Product'], color='skyblue')
plt.xlabel('Nama Atlet')
plt.ylabel('Weighted Product')
plt.title('Hasil Seleksi Atlet PraPON Shorinji Kempo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
