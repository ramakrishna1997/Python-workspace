import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# load data
X = np.loadtxt('data.txt')

# fit K-Means model
kmeans = KMeans(n_clusters=3).fit(X)

# predict clusters
predictions = kmeans.predict(X)

# plot data with predicted clusters
plt.scatter(X[:,0], X[:,1], c=predictions, cmap='viridis')
plt.show()

