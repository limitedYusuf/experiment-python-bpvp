import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def vikor_method(decision_matrix, weights):
    normalized_matrix = decision_matrix / np.max(decision_matrix, axis=0)

    # Positif (A+)
    a_plus = np.max(normalized_matrix, axis=0)

    # Negatif (A-)
    a_minus = np.min(normalized_matrix, axis=0)

    # Positif (S+)
    s_plus = np.sqrt(np.sum((normalized_matrix - a_plus) ** 2, axis=1))

    # Negatif (S-)
    s_minus = np.sqrt(np.sum((normalized_matrix - a_minus) ** 2, axis=1))

    r = s_minus / (s_plus + s_minus)

    ranking = np.argsort(r)

    return ranking, r

def main():
    np.random.seed(0)
    data = {
        'Nama Siswa': [f'Siswa {i}' for i in range(1, 11)],
        'Kriteria 1': np.random.randint(60, 100, 10),
        'Kriteria 2': np.random.randint(60, 100, 10),
        'Kriteria 3': np.random.randint(60, 100, 10),
        'Kriteria 4': np.random.randint(60, 100, 10),
    }

    df = pd.DataFrame(data)

    weights = np.array([0.3, 0.2, 0.25, 0.25])

    decision_matrix = df.iloc[:, 1:].values

    ranking, r = vikor_method(decision_matrix, weights)

    df['Ranking'] = ranking + 1

    print("Hasil Pemilihan Siswa Berprestasi menggunakan Metode VIKOR:")
    print(df.sort_values(by='Ranking'))

    plt.figure(figsize=(10, 6))
    plt.bar(df['Nama Siswa'], r, color='skyblue')
    plt.xlabel('Nama Siswa')
    plt.ylabel('Skor Preferensi (R)')
    plt.title('Skor Preferensi (R) Siswa')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
