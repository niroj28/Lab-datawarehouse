#6.4 Clustering Iris data using KMedoids
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.cluster import KMedoids
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

#pip install scikit-learn-extra
#Install this using cmd

iris_data=load_iris()
x=iris_data.data
y=iris_data.target
print(*x)
print("\nActual Group:\n",*y)

sc=StandardScaler()
sc.fit(x)
sx=sc.transform(x)
km=KMedoids(n_clusters=3)
km.fit(sx)
py=km.fit_predict(sx)
print("\nPredicted Group:\n",*py)

fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ["g","r","b"]
markers=["+","x","*"]

for i in range(len(sx)):
  ax.scatter(sx[i][0], sx[i][1], sx[i][2],color=colors[py[i]], marker=markers[py[i]])
plt.show()

hs=metrics.homogeneity_score(y, py)  #Homoginity Score
print("\nHomogeniety Score:",hs)
sc=metrics.silhouette_score(sx, py, metric='euclidean') #Silhouette Coefficient
print("Silhouette Coefficient:",sc)