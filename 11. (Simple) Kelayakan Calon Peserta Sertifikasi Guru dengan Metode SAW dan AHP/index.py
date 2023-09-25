import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_kriteria = {
    'K1': [4, 3, 5, 3],
    'K2': [3, 4, 4, 2],
    'K3': [5, 3, 5, 4],
    'K4': [2, 2, 3, 5]
}

def normalisasi(data):
    norm_data = {}
    for key, value in data.items():
        norm_value = [v / sum(value) for v in value]
        norm_data[key] = norm_value
    return norm_data

def saw(data_peserta, bobot_kriteria):
    norm_peserta = normalisasi(data_peserta)
    total_nilai = {}
    for peserta, criteria_data in data_peserta.items():
        total_nilai[peserta] = sum(criteria_data[i] * bobot_kriteria[f'K{i+1}'] for i in range(len(criteria_data)))
    return total_nilai

def ahp(data_kriteria):
    n = len(data_kriteria)
    matrix_kriteria = np.zeros((n, n))
    
    for i, (kriteria_i, nilai_i) in enumerate(data_kriteria.items()):
        for j, (kriteria_j, nilai_j) in enumerate(data_kriteria.items()):
            matrix_kriteria[i, j] = sum(np.array(nilai_i) / np.array(nilai_j))
    
    w, v = np.linalg.eig(matrix_kriteria)
    
    max_eigenvalue_index = np.argmax(w)
    max_eigenvector = v[:, max_eigenvalue_index]
    
    normalized_eigenvector = max_eigenvector / np.sum(max_eigenvector)
    
    bobot_kriteria = {}
    for i, kriteria in enumerate(data_kriteria.keys()):
        bobot_kriteria[kriteria] = normalized_eigenvector[i]
    
    return bobot_kriteria

bobot_kriteria_ahp = ahp(data_kriteria)

data_calon_peserta = {
    'Calon1': [4, 3, 5, 2],
    'Calon2': [3, 4, 3, 5],
    'Calon3': [5, 3, 5, 2],
    'Calon4': [3, 2, 4, 5]
}

hasil_saw = saw(data_calon_peserta, bobot_kriteria_ahp)
df_hasil = pd.DataFrame(list(hasil_saw.items()), columns=['Calon Peserta', 'Nilai Akhir'])

df_hasil['Peringkat'] = df_hasil['Nilai Akhir'].rank(ascending=False).astype(int)

print("Hasil Perangkingan:")
sorted_df = df_hasil.sort_values(by='Peringkat')

plt.figure(figsize=(8, 6))
plt.barh(sorted_df['Calon Peserta'], sorted_df['Nilai Akhir'], color='skyblue')
plt.xlabel('Nilai Akhir')
plt.ylabel('Calon Peserta')
plt.title('Perangkingan Calon Peserta')
plt.gca().invert_yaxis()
plt.show()
