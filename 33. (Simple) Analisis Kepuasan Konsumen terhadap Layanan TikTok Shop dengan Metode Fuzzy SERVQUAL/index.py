import numpy as np
import matplotlib.pyplot as plt

def membership_function(x, dimension, params):
    if dimension == 'buruk':
        if x <= params['batas_bawah']:
            return 1
        elif x > params['batas_bawah'] and x < params['batas_tengah']:
            return (params['batas_tengah'] - x) / (params['batas_tengah'] - params['batas_bawah'])
        else:
            return 0
    elif dimension == 'cukup':
        if x >= params['batas_bawah'] and x <= params['batas_tengah']:
            return (x - params['batas_bawah']) / (params['batas_tengah'] - params['batas_bawah'])
        elif x > params['batas_tengah'] and x < params['batas_atas']:
            return (params['batas_atas'] - x) / (params['batas_atas'] - params['batas_tengah'])
        else:
            return 0
    elif dimension == 'baik':
        if x >= params['batas_tengah'] and x <= params['batas_atas']:
            return (x - params['batas_tengah']) / (params['batas_atas'] - params['batas_tengah'])
        elif x > params['batas_atas'] and x < params['batas_sangat_baik']:
            return (params['batas_sangat_baik'] - x) / (params['batas_sangat_baik'] - params['batas_atas'])
        else:
            return 0
    elif dimension == 'sangat baik':
        if x >= params['batas_sangat_baik']:
            return 1
        else:
            return 0

def fuzzy_inference(dimensi_values, dimensi_params):
    hasil_inference = np.ones_like(dimensi_values[0])
    
    for dimensi_val, dimensi_param in zip(dimensi_values, dimensi_params):
        fuzzy_vals = [membership_function(x, dimensi_param['nama'], dimensi_param) for x in dimensi_val]
        
        fuzzy_vals = [0 if val is None else val for val in fuzzy_vals]
        
        hasil_inference = np.minimum(hasil_inference, fuzzy_vals)
    
    return hasil_inference

dimensi_params = [
    {'nama': 'pelayanan', 'batas_bawah': 2, 'batas_tengah': 3, 'batas_atas': 4, 'batas_sangat_baik': 5},
    {'nama': 'kehandalan', 'batas_bawah': 2, 'batas_tengah': 3, 'batas_atas': 4, 'batas_sangat_baik': 5},
    {'nama': 'responsifitas', 'batas_bawah': 2, 'batas_tengah': 3, 'batas_atas': 4, 'batas_sangat_baik': 5},
    {'nama': 'jajanan', 'batas_bawah': 2, 'batas_tengah': 3, 'batas_atas': 4, 'batas_sangat_baik': 5}
]

dimensi_values = [
    np.array([4, 3, 5, 2, 4, 5, 3, 4, 2, 5]),
    np.array([4, 3, 4, 3, 5, 4, 3, 4, 3, 4]),
    np.array([3, 4, 2, 4, 5, 3, 4, 3, 4, 2]),
    np.array([4, 5, 4, 3, 2, 4, 5, 3, 4, 2])
]

fuzzified_values = [np.array([membership_function(x, dimensi_param['nama'], dimensi_param) for x in dimensi_vals]) for dimensi_param, dimensi_vals in zip(dimensi_params, dimensi_values)]

hasil_inference = fuzzy_inference(fuzzified_values, dimensi_params)

x = np.arange(1, 6, 0.1)
centroids = []

for x_val in x:
    weighted_sum = np.sum(x_val * hasil_inference)
    sum_fuzzy_values = np.sum(hasil_inference)
    
    if sum_fuzzy_values != 0:
        centroid = weighted_sum / sum_fuzzy_values
    else:
        centroid = x_val
        
    centroids.append(centroid)

print("Nilai Kepuasan Konsumen:", centroids)