import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv("/home/cs-ai-07/Albert/exp11/Iris.csv")

print("Dataset shape:", df.shape)
print("Columns:", df.columns)

X = df.drop(columns=["Id", "Species"]).values

print("Original shape:", X.shape)

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Reduced shape:", X_reduced.shape)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
                      c=pd.factorize(df["Species"])[0], cmap="viridis", s=40)

species_labels = list(df["Species"].unique())
plt.legend(handles=scatter.legend_elements()[0], labels=species_labels, title="Species")

plt.title("PCA: Iris Dataset (2D Projection)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

