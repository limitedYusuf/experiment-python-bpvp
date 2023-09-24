import numpy as np

# Kolom 0: IPK
# Kolom 1: Penghasilan Orang Tua
# Kolom 2: Prestasi Akademik
# Kolom 3: Penerima Beasiswa (0 = Tidak, 1 = Ya)
data_beasiswa = np.array([
    [3.5, 4000000, 90, 1],
    [3.2, 2000000, 85, 0],
    [3.8, 6000000, 95, 1],
    [3.0, 1000000, 80, 0],
    [3.9, 8000000, 97, 1]
])

def entropy(data):
    _, counts = np.unique(data, return_counts=True)
    probabilities = counts / len(data)
    return -np.sum(probabilities * np.log2(probabilities))

def information_gain(data, feature_col, target_col):
    total_entropy = entropy(data[:, target_col])
    unique_values = np.unique(data[:, feature_col])
    weighted_entropy = 0

    for value in unique_values:
        subset = data[data[:, feature_col] == value]
        subset_entropy = entropy(subset[:, target_col])
        weighted_entropy += (len(subset) / len(data)) * subset_entropy

    return total_entropy - weighted_entropy

num_features = data_beasiswa.shape[1] - 1
gain_values = np.zeros(num_features)

for i in range(num_features):
    gain_values[i] = information_gain(data_beasiswa, i, -1)

best_feature = np.argmax(gain_values)

print("Fitur terbaik untuk pemisahan adalah Kolom:", best_feature)