import numpy as np

curah_hujan = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
jadwal_tanam_padi = np.array(['Tidak Cocok', 'Tidak Cocok', 'Cocok', 'Cocok', 'Cocok',
                              'Cocok', 'Cocok', 'Cocok', 'Cocok', 'Cocok'])

curah_hujan_prediksi = np.array([75, 95, 110])

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def predict_knn(X_train, y_train, x_pred, k=3):
    distances = [euclidean_distance(x_pred, x) for x in X_train]
    k_indices = np.argsort(distances)[:k]
    k_nearest_labels = [y_train[i] for i in k_indices]
    
    k_nearest_labels_int = [1 if label == 'Cocok' else 0 for label in k_nearest_labels]
    most_common = np.bincount(k_nearest_labels_int).argmax()
    predicted_label = 'Cocok' if most_common == 1 else 'Tidak Cocok'
    return predicted_label

X_train = curah_hujan.reshape(-1, 1)
y_train = jadwal_tanam_padi

mean = np.mean(X_train)
std = np.std(X_train)
X_train = (X_train - mean) / std

prediksi_jadwal = [predict_knn(X_train, y_train, curah, k=3) for curah in curah_hujan_prediksi]

print(f'Prediksi Jadwal Tanam Padi: {prediksi_jadwal}')
