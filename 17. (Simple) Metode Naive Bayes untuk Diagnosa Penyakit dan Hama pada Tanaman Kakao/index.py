data_latih = [
    [1, 2, 3, 0],
    [2, 3, 1, 1],
    [3, 1, 2, 1],
    [2, 2, 2, 0],
    [1, 3, 2, 2],
    [2, 1, 1, 2],
]

X = [row[:-1] for row in data_latih]
y = [row[-1] for row in data_latih]

def hitung_probabilitas_prior(y):
    probabilitas_prior = {}
    total_data = len(y)
    for kelas in set(y):
        probabilitas_prior[kelas] = y.count(kelas) / total_data
    return probabilitas_prior

def hitung_probabilitas_likelihood(X, y, kelas, nilai_fitur):
    probabilitas_likelihood = 1.0
    jumlah_fitur = len(X[0])
    for i in range(jumlah_fitur):
        jumlah_data_kelas = sum(1 for j in range(len(X)) if X[j][i] == nilai_fitur[i] and y[j] == kelas)
        jumlah_data_kelas_total = sum(1 for j in range(len(X)) if y[j] == kelas)
        probabilitas_fitur = jumlah_data_kelas / jumlah_data_kelas_total
        probabilitas_likelihood *= probabilitas_fitur
    return probabilitas_likelihood

def prediksi(X, y, data_prediksi):
    probabilitas_prior = hitung_probabilitas_prior(y)
    hasil_prediksi = []
    for data in data_prediksi:
        probabilitas_posterior = {}
        for kelas in set(y):
            probabilitas_likelihood = hitung_probabilitas_likelihood(X, y, kelas, data)
            probabilitas_posterior[kelas] = probabilitas_prior[kelas] * probabilitas_likelihood
        kelas_prediksi = max(probabilitas_posterior, key=probabilitas_posterior.get)
        hasil_prediksi.append(kelas_prediksi)
    return hasil_prediksi

data_uji = [[2, 2, 1]]

hasil_prediksi = prediksi(X, y, data_uji)

if hasil_prediksi[0] == 0:
    print("Tanaman sehat")
elif hasil_prediksi[0] == 1:
    print("Penyakit")
else:
    print("Hama")
