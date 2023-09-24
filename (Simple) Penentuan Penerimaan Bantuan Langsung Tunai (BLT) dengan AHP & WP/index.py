import numpy as np

kriteria = ["Pendapatan", "Tanggungan Keluarga", "Usia"]
bobot_kriteria = [0.4, 0.3, 0.3]

alternatif = ["Alternatif 1", "Alternatif 2", "Alternatif 3"]
nilai_kriteria = np.array([
    [3000000, 5, 30],
    [2500000, 4, 25],
    [3500000, 6, 35]
])

nilai_kriteria_normalisasi = nilai_kriteria / nilai_kriteria.sum(axis=0)

bobot_prioritas_kriteria = nilai_kriteria_normalisasi.mean(axis=1)

skor_weighted_product = np.prod(np.power(nilai_kriteria_normalisasi, bobot_prioritas_kriteria), axis=1)

threshold = np.median(skor_weighted_product)
penerimaan_blt = [alternatif[i] for i, skor in enumerate(skor_weighted_product) if skor >= threshold]

print("Bobot Prioritas Kriteria:")
for i, k in enumerate(kriteria):
    print(f"{k}: {bobot_prioritas_kriteria[i]}")

print("\nSkor Weighted Product:")
for i, alt in enumerate(alternatif):
    print(f"{alt}: {skor_weighted_product[i]}")

print("\nPenerimaan BLT:")
for alt in penerimaan_blt:
    print(alt)

