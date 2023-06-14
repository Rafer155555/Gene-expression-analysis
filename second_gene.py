import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# Load the data
data = pd.read_csv('data/gene_expression.csv')
# Preprocess the data
data = data.dropna()
data = data.astype('float64')
# Reduce the dimensionality of the data
pca = PCA(n_components=2)
pca.fit(data)
data = pca.transform(data)
# Cluster the data
kmeans = KMeans(n_clusters=5)
kmeans.fit(data)
labels = kmeans.predict(data)
# Visualize the results
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.show()
