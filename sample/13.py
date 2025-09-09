import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv("exp13/Mall_Customers.csv")

# Select features for clustering (Annual Income & Spending Score)
X = df[['Annual Income (k$)', 'Spending Score (1-100)']].values

# Fit KMeans
kmeans = KMeans(n_clusters=5, n_init=10, random_state=0)  # try 5 clusters
kmeans.fit(X)

# Get labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Print centroid positions
for i, centroid in enumerate(centroids):
    print(f'Centroid {i + 1}: {centroid}')

# Define custom colors for clusters
colors = ['blue', 'orange', 'green', 'purple', 'brown']
cluster_colors = [colors[label] for label in labels]

# Plot clusters
plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], X[:, 1], c=cluster_colors, s=50, alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='red', label='Centroids')

# Adding custom legends
for i, color in enumerate(colors[:len(centroids)]):
    plt.scatter([], [], c=color, label=f'Cluster {i + 1}')

# Labels
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('K-means Clustering of Mall Customers')
plt.legend()
plt.show()
