import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_correlations(data, output_file):
    insignificant_str = ""
    result_str = ""
    with open(output_file, 'w') as f:
        for target_feature in data.columns:
            for feature2 in data.columns:
                if feature2 != target_feature:
                    correlation_coefficient, p_value = pearsonr(data[target_feature], data[feature2])
                    if p_value < 0.05:
                        result_str += (
                            f"Correlation between '{target_feature}' and '{feature2}':\n"
                            f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                            f"P-value: {p_value:.4f}\n\n")
                    else:
                        insignificant_str += (
                            f"Correlation between '{target_feature}' and '{feature2}':\n"
                            f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                            f"P-value: {p_value:.4f}\n\n")
        f.write(f"Significant P-Values: \n {result_str}")
        f.write(f"Insignificant Features:\n {insignificant_str}")

def main():
    csv_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\Datasets\OnlyNumerical_Combined_Datasets.csv"
    output_file_path =r"C:\Users\carrie\Documents\CIS_598_Capstone\PearsonCorrelationsAndPValues\CombinedDatasets\AllCorrelations.txt"
    
    data = pd.read_csv(csv_file_path)

    calculate_correlations(data, output_file_path)
    print(f"done! results are in {output_file_path}")

main()
