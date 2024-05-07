import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
import os


def calculate_pairwise_correlations(data, target_feature, output_file):

    features = [feat for feat in data.columns if feat != target_feature] #and feat == 'PercentBlack' or feat == 'CurrentMinimumWage' or feat == 'MedianWage' or feat == 'CostOfLivingIndex' or feat == 'PercentBlackUndergrad' or feat == 'HighCholesterol' or feat == 'FoodInsecurity' or feat == 'Hypertension' or feat == 'MedianWage' or feat == 'InfantMortality' or feat == 'ChildMortality' or feat == 'PercentUndergradOnCampus' or feat == 'PercentUndergradOffCampus' or feat == 'AvgNeedBasedScholarshipAmount' or feat == 'TotalNonNeedScholarship' or feat == 'Hypertension' or feat == 'CardiovascularDisease' or feat == 'AvoidedCareDueToCost' or feat == 'MultipleChronicConditions']
    insignificant_str = ""
    result_str = ""
    with open(output_file, 'w') as f:
        for feature2 in features:
            correlation_coefficient, p_value = pearsonr(data[target_feature], data[feature2])
            
            if p_value < 0.05:
                result_str += (
                    f"Correlation between '{target_feature}' and '{feature2}':\n"
                    f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                    f"P-value: {p_value:.4f}\n\n"
                )
            else:
                insignificant_str += (
                    f"Correlation between '{target_feature}' and '{feature2}':\n"
                    f"Pearson correlation coefficient: {correlation_coefficient:.4f}\n"
                    f"P-value: {p_value:.4f}\n\n"
                )

        f.write(f"Significant P-Values: \n {result_str}")
        f.write(f"Insignificant Features: {insignificant_str}")

def main():
    csv_file_path = r"C:\Users\carrie\Documents\CIS890_DataPractice\Dataset\numericalonly_csv_William _Duncan_Wyandotte_County_Data.csv"
    output_file_path =r"C:\Users\carrie\Documents\CIS890_DataPractice\CorrelationResultsByVariable\MedianWageCorrelations.txt"

    data = pd.read_csv(csv_file_path)

    
    target = 'MedianWage'
    calculate_pairwise_correlations(data, target, output_file_path)
    print(f"done! results are in {output_file_path}")

main()
