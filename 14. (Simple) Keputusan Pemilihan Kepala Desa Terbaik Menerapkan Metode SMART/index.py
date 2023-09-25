pemohon = {
    'A': [90, 80, 85, 70, 75],
    'B': [80, 85, 90, 75, 80],
    'C': [85, 70, 80, 90, 85],
}

bobot = [0.25, 0.2, 0.15, 0.2, 0.2]

def normalisasi_matriks(matriks):
    matriks_normalisasi = {}
    for nama, nilai in matriks.items():
        total = sum(nilai)
        matriks_normalisasi[nama] = [nilai[i] / total for i in range(len(nilai))]
    return matriks_normalisasi

matriks_normalisasi = normalisasi_matriks(pemohon)

def nilai_total_smart(matriks_normalisasi, bobot):
    nilai_total = {}
    for nama, nilai in matriks_normalisasi.items():
        total = sum([nilai[i] * bobot[i] for i in range(len(nilai))])
        nilai_total[nama] = total
    return nilai_total

nilai_total = nilai_total_smart(matriks_normalisasi, bobot)

pemenang = max(nilai_total, key=nilai_total.get)

print("Hasil Keputusan Pemilihan Kepala Desa Terbaik dengan Metode SMART:")
for nama, nilai in nilai_total.items():
    print(f"{nama}: {nilai}")

print(f"Kepala Desa Terbaik: {pemenang}")
