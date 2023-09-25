import matplotlib.pyplot as plt

wisata = {
    'Objek 1': {'Harga': 100, 'Jarak': 5, 'Popularitas': 8},
    'Objek 2': {'Harga': 50, 'Jarak': 2, 'Popularitas': 7},
    'Objek 3': {'Harga': 150, 'Jarak': 10, 'Popularitas': 9},
    'Objek 4': {'Harga': 80, 'Jarak': 3, 'Popularitas': 6},
}

bobot = {'Harga': 0.4, 'Jarak': 0.3, 'Popularitas': 0.3}

def hitung_skor(objek, bobot):
    skor = 0
    for atribut, nilai in objek.items():
        skor += nilai * bobot[atribut]
    return skor

def rekomendasikan_objek(wisata, bobot):
    skor_objek = {}
    for nama_objek, atribut_objek in wisata.items():
        skor = hitung_skor(atribut_objek, bobot)
        skor_objek[nama_objek] = skor

    objek_terbaik = max(skor_objek, key=skor_objek.get)
    return objek_terbaik

rekomendasi = rekomendasikan_objek(wisata, bobot)
print(f"Objek wisata terbaik untuk direkomendasikan adalah: {rekomendasi}")

skor_objek = {}
objek = []
for nama_objek, atribut_objek in wisata.items():
    skor = hitung_skor(atribut_objek, bobot)
    skor_objek[nama_objek] = skor
    objek.append(nama_objek)

skor = list(skor_objek.values())

plt.figure(figsize=(10, 6))
plt.barh(objek, skor, color='skyblue')
plt.xlabel('Skor SMART')
plt.ylabel('Objek Wisata')
plt.title('Rekomendasi Objek Wisata Berdasarkan Metode SMART')
plt.gca().invert_yaxis()
plt.show()
