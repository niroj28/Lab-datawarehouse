import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering



x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 20]
data = list(zip(x, y))

linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)
plt.show()

n_clusters = int(input("Enter the number of clusters to create: "))
hierarchical_cluster = AgglomerativeClustering(n_clusters, affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)
print("Labels: ", labels)
plt.scatter(x, y, c=labels)
plt.show()