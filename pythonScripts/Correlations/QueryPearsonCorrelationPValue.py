import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
import os


def calculate_pairwise_correlations(data, target_feature, output_file):

    features = [feat for feat in data.columns if feat != target_feature] #and feat == 'PercentBlack' or feat == 'CurrentMinimumWage' or feat == 'MedianWage' or feat == 'CostOfLivingIndex' or feat == 'PercentBlackUndergrad' or feat == 'HighCholesterol' or feat == 'FoodInsecurity' or feat == 'Hypertension' or feat == 'MedianWage' or feat == 'InfantMortality' or feat == 'ChildMortality' or feat == 'PercentUndergradOnCampus' or feat == 'PercentUndergradOffCampus' or feat == 'AvgNeedBasedScholarshipAmount' or feat == 'TotalNonNeedScholarship' or feat == 'Hypertension' or feat == 'CardiovascularDisease' or feat == 'AvoidedCareDueToCost' or feat == 'MultipleChronicConditions']
    significant_correlations = []
    insignificant_str = ""
    result_str = ""
    with open(output_file, 'w') as f:
        for feature2 in features:

            correlation_coefficient, p_value = pearsonr(data[target_feature], data[feature2])
            
            if p_value < 0.05:
                result_str = (
                    f"Correlation between '{target_feature}' and '{feature2}':\n"
                    f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                    f"P-value: {p_value:.4f}\n\n"
                )
                significant_correlations.append((feature2, correlation_coefficient, p_value))
            else:
                insignificant_str += (
                    f"Correlation between '{target_feature}' and '{feature2}':\n"
                    f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                    f"P-value: {p_value:.4f}\n\n"
                )
                
            f.write(f"Significant P-Values: \n {result_str}")
        f.write(f"Insignificant Features: {insignificant_str}")

def calculate_correlations(data, output_file):
    
    insignificant_str = ""
    result_str = ""
    new_data = data
    with open(output_file, 'w') as f:
        for target_feature in data.columns:
            f.write(f"Correlations with Feature of Interest: {target_feature}\n\n")
            for feature2 in data.columns:

                correlation_coefficient, p_value = pearsonr(data[target_feature], data[feature2])
                
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
        f.write(f"Insignificant Features:\n {insignificant_str}")

def main():
    csv_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\Datasets\OnlyNumerical_Combined_Datasets.csv"
    output_file_path =r"C:\Users\carrie\Documents\CIS_598_Capstone\PearsonCorrelationsAndPValues\CombinedDatasets"

    data = pd.read_csv(csv_file_path)

    target = 'Suicide'
    calculate_pairwise_correlations(data, target, output_file_path)
    print(f"done! results are in {output_file_path}")

main()
