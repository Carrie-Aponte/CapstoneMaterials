import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
import os

def calculate_correlations(data, output_file):
    
    insignificant_str = ""
    result_str = ""
    new_data = data

    with open(output_file, 'w') as f:
        for feature in data:
            target = feature
            new_feature_list = new_data.drop(target, axis = 1)
            for feature2 in new_feature_list:
            #for i in range(len(features)):
                #feature1 = feature
                #feature2 = features[i]
                #for j in range(i + 1, len(features)):
                #    feature1 = features[i]
                #    feature2 = features[j]
                    
                correlation_coefficient, p_value = pearsonr(data[target], data[feature2])
                
                if p_value < 0.05:
                    result_str = (
                        f"Correlation between '{target}' and '{feature2}':\n"
                        f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                        f"P-value: {p_value:.4f}\n\n"
                    )
                else:
                    insignificant_str += (
                        f"Correlation between '{target}' and '{feature2}':\n"
                        f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                        f"P-value: {p_value:.4f}\n\n"
                    )
            new_data = data
                
            f.write(f"Significant P-Values: \n {result_str}")
        f.write(f"Insignificant Features: {insignificant_str}")

    
def main():
    csv_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\Datasets\OnlyNumerical_Combined_Datasets.csv"
    output_file_path =r"C:\Users\carrie\Documents\CIS_598_Capstone\PearsonCorrelationsAndPValues\CombinedDatasetsAllPearsonCorrelationAndPValues.txt"

    data = pd.read_csv(csv_file_path)
    #X = data.drop('Preemption', axis=1)  
    #y = data['Preemption'] 
    
    calculate_correlations(data, output_file_path)
    print(f"done! results are in {output_file_path}")

main()
 