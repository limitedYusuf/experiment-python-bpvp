import numpy as np
import matplotlib.pyplot as plt

def fuzzy_membership_berat_badan(x):
    underweight = np.maximum(0, np.minimum((5 - x) / 5, 1))
    normal = np.maximum(0, np.minimum((x - 0) / 5, 1))
    return underweight, normal

def fuzzy_membership_tinggi_badan(x):
    short = np.maximum(0, np.minimum((50 - x) / 50, 1))
    average = np.maximum(0, np.minimum((x - 30) / 20, 1))
    tall = np.maximum(0, np.minimum((x - 50) / 50, 1))
    return short, average, tall

def fuzzy_mamdani_inference(berat_badan, tinggi_badan):
    berat_underweight, berat_normal = fuzzy_membership_berat_badan(berat_badan)
    tinggi_short, tinggi_average, tinggi_tall = fuzzy_membership_tinggi_badan(tinggi_badan)

    rule1 = np.minimum(berat_underweight, tinggi_short)
    rule2 = np.minimum(berat_normal, tinggi_average)
    rule3 = np.minimum(berat_normal, tinggi_tall)

    aggregated = max(rule1, rule2, rule3)

    return aggregated

berat_balita = 4
tinggi_balita = 60

aggregated_mamdani = fuzzy_mamdani_inference(berat_balita, tinggi_balita)

print("Hasil Agregasi (Fuzzy Mamdani):", aggregated_mamdani)

x_berat = np.linspace(0, 10, 400)
underweight, normal = fuzzy_membership_berat_badan(x_berat)
plt.figure(figsize=(8, 4))
plt.plot(x_berat, underweight, label='Underweight')
plt.plot(x_berat, normal, label='Normal')
plt.title('Fungsi Keanggotaan Berat Badan')
plt.xlabel('Berat Badan (kg)')
plt.ylabel('Keanggotaan')
plt.legend()
plt.show()

x_tinggi = np.linspace(0, 100, 400)
short, average, tall = fuzzy_membership_tinggi_badan(x_tinggi)
plt.figure(figsize=(8, 4))
plt.plot(x_tinggi, short, label='Short')
plt.plot(x_tinggi, average, label='Average')
plt.plot(x_tinggi, tall, label='Tall')
plt.title('Fungsi Keanggotaan Tinggi Badan')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Keanggotaan')
plt.legend()
plt.show()
