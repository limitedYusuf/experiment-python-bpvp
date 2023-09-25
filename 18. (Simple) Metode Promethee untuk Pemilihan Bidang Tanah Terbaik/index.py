import numpy as np

kriteria = ['Harga', 'Luas', 'Jarak ke Pusat Kota']
alternatif = ['Tanah A', 'Tanah B', 'Tanah C', 'Tanah D']

preferensi = np.array([
    # Harga    Luas    Jarak ke Pusat Kota
    [0,        1/3,    1/2],  # Tanah A
    [1,        0,      1],    # Tanah B
    [1/2,      1,      0],    # Tanah C
    [1/3,      1/2,    0],    # Tanah D
])

matriks_pref_alternatif = np.zeros((len(alternatif), len(alternatif)))

for i in range(len(alternatif)):
    for j in range(len(alternatif)):
        if i != j:
            matriks_pref_alternatif[i][j] = np.sum(preferensi[i] - preferensi[j])

pn = np.sum(matriks_pref_alternatif, axis=1)
pp = np.sum(matriks_pref_alternatif > 0, axis=1)
pn = np.sum(matriks_pref_alternatif < 0, axis=1)

phi = pp - pn

peringkat = np.argsort(phi)[::-1]

print("Hasil Peringkat:")
for i, idx in enumerate(peringkat):
    print(f"{i + 1}. {alternatif[idx]}")

alternatif_terbaik = alternatif[peringkat[0]]
print(f"Alternatif Terbaik adalah {alternatif_terbaik}")
