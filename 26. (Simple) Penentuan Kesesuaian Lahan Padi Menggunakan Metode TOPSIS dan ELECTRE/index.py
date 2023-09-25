import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Lahan': ['Lahan A', 'Lahan B', 'Lahan C', 'Lahan D'],
    'Fasilitas Irigasi': [0.8, 0.6, 0.9, 0.7],
    'Kualitas Tanah': [0.7, 0.9, 0.6, 0.8],
    'Curah Hujan': [0.6, 0.7, 0.8, 0.5]
})

bobot = {
    'Fasilitas Irigasi': 0.4,
    'Kualitas Tanah': 0.3,
    'Curah Hujan': 0.3
}

matriks_keputusan = data[['Fasilitas Irigasi', 'Kualitas Tanah', 'Curah Hujan']].values

for i in range(matriks_keputusan.shape[1]):
    min_val = np.min(matriks_keputusan[:, i])
    max_val = np.max(matriks_keputusan[:, i])
    matriks_keputusan[:, i] = (matriks_keputusan[:, i] - min_val) / (max_val - min_val)

ideal_positif = np.max(matriks_keputusan, axis=0)
ideal_negatif = np.min(matriks_keputusan, axis=0)

jarak_positif = np.sqrt(np.sum((matriks_keputusan - ideal_positif) ** 2, axis=1))
jarak_negatif = np.sqrt(np.sum((matriks_keputusan - ideal_negatif) ** 2, axis=1))

nilai_closeness = jarak_negatif / (jarak_positif + jarak_negatif)

data['Nilai Closeness'] = nilai_closeness

alternatif_terbaik = data[data['Nilai Closeness'] == data['Nilai Closeness'].max()]

plt.figure(figsize=(8, 6))
plt.bar(data['Lahan'], data['Nilai Closeness'], color='skyblue')
plt.xlabel('Alternatif Lahan')
plt.ylabel('Nilai Closeness')
plt.title('Nilai Closeness untuk Alternatif Lahan')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

print("Hasil Penentuan Kesesuaian Lahan Padi Menggunakan Metode TOPSIS:")
print(alternatif_terbaik)
