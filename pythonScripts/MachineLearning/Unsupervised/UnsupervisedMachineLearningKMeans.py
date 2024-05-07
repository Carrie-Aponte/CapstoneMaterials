import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

data = pd.read_csv(r"C:\Users\carrie\Documents\CIS890_DataPractice\Dataset\numericalonly_csv_William _Duncan_Wyandotte_County_Data.csv")
output_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\UnsupervisedMachineLearningResults\kmeansHealthWageData.txt"

with open(output_file_path, 'w') as f:
    kmeans = KMeans(n_clusters=3, random_state=42).fit(data)

    predictions = kmeans.predict(data)
    kmeans.labels_
    kmeans.labels_[0:135]

    centers = kmeans.cluster_centers_

    f.write("Cluster centers: ")
    for i, center in enumerate(centers):
        f.write(f"Cluster {i+1}: {center}\n")
        print("one line down")
    f.write('\n')

#do PCA here before plotting

    plt.figure(figsize=(8, 6))
    plt.scatter(data.values[:, 0], data.values[:, 1], c=predictions, cmap='viridis', alpha=0.5)
    plt.scatter(centers[:, 0], centers[:, 1], marker='o', c='red', s=200)
    plt.title('KMeans Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
