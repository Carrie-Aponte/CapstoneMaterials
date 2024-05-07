from sklearn.neighbors import LocalOutlierFactor
import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\Users\carrie\Documents\CIS_598_Capstone\Datasets\OnlyNumerical_Combined_Datasets.csv")
output_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\LocalOutlierFactor\CombinedSet\CombinedDatasetLOF20,0.05.txt"


lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
lof.fit(data)

outlier_scores = lof.fit_predict(data)
"""
plt.figure(figsize=(10, 6))
plt.hist(outlier_scores, bins='auto', alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram of Outlier Scores')
plt.xlabel('Outlier Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
"""
outliers = data[outlier_scores < 0]

with open(output_file_path, 'w' ) as fp:

    fp.write("Identified Outliers:")
    fp.write(str(outliers))


