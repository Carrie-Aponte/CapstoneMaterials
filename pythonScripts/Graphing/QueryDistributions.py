import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_variable_distributions(data, output_folder):

    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns

    import os
    os.makedirs(output_folder, exist_ok=True)

    for col in numerical_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, f'{col}_distribution.png'))
        plt.close()

def main():
    csv_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\OnlyNumerical_Combined_Datasets.csv"
    output_folder = r'C:\Users\carrie\Documents\CIS_598_Capstone\Distributions'

    data = pd.read_csv(csv_file_path)

    plot_variable_distributions(data, output_folder)

    print(f"Done! Distribution plots saved in {output_folder}")


main()
