import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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


    norm_train_samples = StandardScaler().fit_transform(centers)
    pca = PCA(n_components = 2)
    principal_components = pca.fit_transform(centers)

#do PCA here before plotting

    plt.figure(figsize=(8, 6))
    plt.scatter(data.values[:, 0], data.values[:, 1], c=predictions, cmap='viridis', alpha=0.5)
    plt.scatter(principal_components[:, 0], principal_components[:, 1], marker='o', c='red', s=200)
    plt.title('KMeans Clustering with PCA')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
