# Reference: https://github.com/hbeychaner/common/blob/master/notebooks/Specter%20Clustering%20Analysis.ipynb

import pandas as pd
import umap
from sklearn.cluster import KMeans

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
pd.set_option("max_colwidth", 800)

metadata = pd.read_csv("data/metadata.csv", low_memory=False)

embeddings = pd.read_csv("data/cord_19_embeddings_4_24.csv", header=None, low_memory=False) 
embeddings.rename(columns={0:"cord_uid"}, inplace=True)
embeddings = embeddings.set_index("cord_uid")

# Cluster the embeddings
kmeans = KMeans(n_clusters=7, init='k-means++', random_state=42)
cluster_predictions = kmeans.fit_predict(embeddings.values)

# Project embeddings to 2D space using UMAP
reducer = umap.UMAP(n_components=2)
projection = reducer.fit_transform(embeddings.values)
projection = pd.DataFrame(projection, columns=["z1", "z2"])
projection.index = embeddings.index
projection['cluster'] = cluster_predictions

# Merge metdata with projections
metadata_cols = ['cord_uid', 'title', 'authors', 'url']
merged = pd.merge(metadata[metadata_cols], projection, left_on="cord_uid", right_index=True)

print(merged.head(3))

# Write compressed CSV
save_path = "cord19_projections.csv.gz"
merged.to_csv(save_path, index=False, compression='gzip')
print(f"Done, saved to {save_path}")
