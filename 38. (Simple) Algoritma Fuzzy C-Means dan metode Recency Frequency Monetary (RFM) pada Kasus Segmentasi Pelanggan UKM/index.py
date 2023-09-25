import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(0)

end_date = datetime(2023, 9, 25)
start_date = end_date - timedelta(days=730)  # 2 years
date_range = [start_date + timedelta(days=i) for i in range(730)]
dates = np.random.choice(date_range, size=1000)

customer_ids = np.random.randint(1, 101, size=1000)
invoice_amounts = np.random.uniform(10, 200, size=1000)

data = pd.DataFrame({'CustomerID': customer_ids, 'InvoiceDate': dates, 'TotalAmount': invoice_amounts})
data.sort_values(['InvoiceDate'], inplace=True)

data.reset_index(drop=True, inplace=True)

n_clusters = 2 
m = 2 
max_iter = 100
tolerance = 0.0001

# Extract RFM features
current_date = datetime(2023, 9, 25)
recency = (current_date - data['InvoiceDate']).dt.days
frequency = data.groupby('CustomerID')['InvoiceDate'].cumcount() + 1
monetary = data['TotalAmount']

rfm_data = pd.DataFrame({'Recency': recency, 'Frequency': frequency, 'Monetary': monetary})

rfm_scaled = (rfm_data - rfm_data.mean()) / rfm_data.std()
rfm_scaled = rfm_scaled.to_numpy()

np.random.seed(0)
centroids = np.random.rand(n_clusters, rfm_scaled.shape[1])

cluster_labels = np.full(rfm_scaled.shape[0], np.nan)

for iter in range(max_iter):
    membership_degrees = np.zeros((rfm_scaled.shape[0], n_clusters))
    for i in range(rfm_scaled.shape[0]):
        for j in range(n_clusters):
            distance_ij = np.linalg.norm(rfm_scaled[i] - centroids[j], ord=2)
            membership_degrees[i, j] = 1 / np.sum((distance_ij / np.linalg.norm(rfm_scaled[i] - centroids[j], ord=2)) ** (2 / (m - 1)))

    new_centroids = np.zeros((n_clusters, rfm_scaled.shape[1]))
    for j in range(n_clusters):
        numerator = np.sum((membership_degrees[:, j] ** m) * rfm_scaled.T, axis=1)
        denominator = np.sum(membership_degrees[:, j] ** m)
        new_centroids[j] = numerator / denominator

    if np.all(np.abs(new_centroids - centroids) < tolerance):
        break

    centroids = new_centroids

    cluster_labels = np.argmax(membership_degrees, axis=1)

data_with_labels = pd.concat([data, pd.Series(cluster_labels, name='Cluster')], axis=1)

print("Segmentation Results:")
print(data_with_labels)
