import numpy as np
import pandas as pd

criteria_matrix = np.array([
    [1, 3, 5],    
    [1/3, 1, 2], 
    [1/5, 1/2, 1] 
])

alternatives_matrices = [
    np.array([
        [1, 3, 2],
        [1/3, 1, 1/2],
        [1/2, 2, 1]   
    ]),
    np.array([
        [1, 1/3, 1/5],
        [3, 1, 1/2],  
        [5, 2, 1]      
    ]),
    np.array([
        [1, 2, 1/2],  
        [1/2, 1, 1/3],
        [2, 3, 1]      
    ])
]

criteria_weights = np.mean(criteria_matrix, axis=1) / np.sum(np.mean(criteria_matrix, axis=1))

alternative_scores = []

for i, matrix in enumerate(alternatives_matrices):
    weighted_matrix = np.dot(matrix, np.diag(criteria_weights))
    alternative_scores.append(np.sum(weighted_matrix, axis=1))
    
    print(f"Nilai alternatif untuk Kafe {i + 1}:")
    print(pd.DataFrame(weighted_matrix, columns=['Kriteria 1', 'Kriteria 2', 'Kriteria 3']))

df = pd.DataFrame(alternative_scores, columns=['Kafe 1', 'Kafe 2', 'Kafe 3'])
df['Total'] = df.sum(axis=1)

best_cafe = df['Total'].idxmax() + 1
best_score = df['Total'].max()

print("\nHasil akhir:")
print(f"Kafe terbaik adalah Kafe {best_cafe} dengan nilai total {best_score}")
