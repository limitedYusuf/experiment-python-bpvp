import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Nama": ["Atlet A", "Atlet B", "Atlet C", "Atlet D", "Atlet E"],
    "Usia": [25, 28, 22, 30, 24],
    "Teknik": [85, 90, 80, 88, 78],
    "Fisik": [75, 80, 70, 85, 72],
    "Mental": [90, 85, 95, 92, 88]
}

df = pd.DataFrame(data)

bobot = {"Usia": 0.1, "Teknik": 0.4, "Fisik": 0.3, "Mental": 0.2}

def normalize(df):
    result = df.copy()
    for feature_name in df.columns[1:]:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

normalized_df = normalize(df)

def calculate_roc_score(row):
    return sum([row[kriteria] * bobot[kriteria] for kriteria in bobot.keys()])

normalized_df["ROC_Score"] = normalized_df.apply(calculate_roc_score, axis=1)

def calculate_wp_score(row):
    return np.prod([row[kriteria] ** bobot[kriteria] for kriteria in bobot.keys()])

normalized_df["WP_Score"] = normalized_df.apply(calculate_wp_score, axis=1)

sorted_df_roc = normalized_df.sort_values(by="ROC_Score", ascending=False)
sorted_df_wp = normalized_df.sort_values(by="WP_Score", ascending=False)

print("Hasil Pengambilan Keputusan (Berdasarkan ROC):")
print(sorted_df_roc[["Nama", "ROC_Score"]])

print("\nHasil Pengambilan Keputusan (Berdasarkan WP):")
print(sorted_df_wp[["Nama", "WP_Score"]])

atlet_terpilih_roc = sorted_df_roc.iloc[0]
atlet_terpilih_wp = sorted_df_wp.iloc[0]

print(f"\nAtlet yang terpilih untuk kenaikan sabuk hitam (ROC): {atlet_terpilih_roc['Nama']} (Skor ROC: {atlet_terpilih_roc['ROC_Score']})")
print(f"Atlet yang terpilih untuk kenaikan sabuk hitam (WP): {atlet_terpilih_wp['Nama']} (Skor WP: {atlet_terpilih_wp['WP_Score']}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.barh(sorted_df_roc["Nama"], sorted_df_roc["ROC_Score"], color='b', alpha=0.7)
plt.xlabel('Skor ROC')
plt.title('Peringkat Atlet berdasarkan ROC')
plt.gca().invert_yaxis()

plt.subplot(1, 2, 2)
plt.barh(sorted_df_wp["Nama"], sorted_df_wp["WP_Score"], color='g', alpha=0.7)
plt.xlabel('Skor WP')
plt.title('Peringkat Atlet berdasarkan WP')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()
