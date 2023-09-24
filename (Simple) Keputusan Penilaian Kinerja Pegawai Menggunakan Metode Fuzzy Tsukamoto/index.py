import numpy as np
import matplotlib.pyplot as plt

def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)

def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1.0
    elif c < x < d:
        return (d - x) / (d - c)

defuzzified_kinerja = np.arange(0, 101, 1)
defuzzified_disiplin = np.arange(0, 101, 1)

defuzzified_hasil = np.arange(0, 101, 1)

nilai_max_disiplin = 100
nilai_max_kinerja = 100

# Disiplin
disiplin_rendah = lambda x: triangular(x, 0, 0, 50)
disiplin_sedang = lambda x: trapezoidal(x, 30, 50, 70, 90)
disiplin_tinggi = lambda x: triangular(x, 50, 100, 100)

# Kinerja
kinerja_rendah = lambda x: triangular(x, 0, 0, 40)
kinerja_sedang = lambda x: trapezoidal(x, 30, 40, 60, 70)
kinerja_tinggi = lambda x: triangular(x, 60, 100, 100)

# Hasil
hasil_rendah = lambda x: triangular(x, 0, 0, 30)
hasil_tinggi = lambda x: triangular(x, 70, 100, 100)

output_hasil_rendah = np.zeros_like(defuzzified_hasil)
output_hasil_tinggi = np.zeros_like(defuzzified_hasil)

for i, disiplin in enumerate(defuzzified_disiplin):
    for j, kinerja in enumerate(defuzzified_kinerja):
        
        rule1 = min(disiplin_rendah(disiplin), kinerja_rendah(kinerja))
        rule2 = min(disiplin_sedang(disiplin), kinerja_sedang(kinerja))
        rule3 = min(disiplin_tinggi(disiplin), kinerja_tinggi(kinerja))
        
        inferred_rendah = min(rule1, hasil_rendah(defuzzified_hasil[i]))
        inferred_tinggi = min(rule2, rule3, hasil_tinggi(defuzzified_hasil[i]))
        
        output_hasil_rendah[i] = max(output_hasil_rendah[i], inferred_rendah)
        output_hasil_tinggi[i] = max(output_hasil_tinggi[i], inferred_tinggi)

defuzzified_result = np.zeros_like(defuzzified_hasil)
total_weight = 0

for k in range(len(defuzzified_hasil)):
    if output_hasil_rendah[k] > output_hasil_tinggi[k]:
        weight = output_hasil_rendah[k]
    else:
        weight = output_hasil_tinggi[k]
    
    defuzzified_result[k] = defuzzified_hasil[k] * weight
    total_weight += weight

if total_weight == 0:
    hasil_akhir = 0.0
else:
    hasil_akhir = sum(defuzzified_result) / total_weight

plt.figure(figsize=(10, 6))
plt.plot(defuzzified_hasil, output_hasil_rendah, label='Hasil Rendah')
plt.plot(defuzzified_hasil, output_hasil_tinggi, label='Hasil Tinggi')
plt.title('Fungsi Keanggotaan Hasil')
plt.legend()
plt.grid()

plt.figure(figsize=(10, 6))
plt.plot(defuzzified_hasil, defuzzified_result, label=f'Hasil Akhir: {hasil_akhir:.2f}')
plt.title('Hasil Akhir')
plt.legend()
plt.grid()

plt.show()

print("Hasil Akhir: {:.2f}".format(hasil_akhir))
