import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
sns.set()

data = pd.read_csv(r"C:\Users\carrie\Documents\CIS890_DataPractice\Dataset\numericalonly_csv_William _Duncan_Wyandotte_County_Data.csv")
output_file_path = r"C:\Users\carrie\Documents\CIS890_DataPractice\UnsupervisedMachineLearning\FullSetHealthDataKmeansClustering"

#data.head()

with open(output_file_path, 'w') as f:
    scaler = StandardScaler()
    segmented_data = scaler.fit_transform(data)

    pca = PCA()
    pca.fit(segmented_data)

    variance_ratio = pca.explained_variance_ratio_

    num_features = len(data.columns)

    variance_ratio = variance_ratio[:num_features]

    """
    plt.figure(figsize =(10,8))
    plt.plot(range(1,num_features+1), variance_ratio.cumsum(), marker='o', linestyle = "--")
    plt.title('Explained variance by components')
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative explained variance")
    plt.show()"""

    pca = PCA(n_components = 5)

    pca.fit(segmented_data)

    #pca.transform(segmented_data)

    scores_pca = pca.transform(segmented_data)