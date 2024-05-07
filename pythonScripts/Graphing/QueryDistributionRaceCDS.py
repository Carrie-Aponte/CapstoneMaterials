import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_percentage_distributions(data, percentage_columns, output_filepath):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    plt.figure(figsize=(10, 6))
    for col in percentage_columns:
        sns.histplot(data[col], kde=True, label=col)

    plt.title("Distribution of Race Variables")
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_filepath)
    plt.show()

def main():
    csv_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\Datasets\Final_CDS_By_State.csv"
    output_filepath = r"C:\Users\carrie\Documents\CIS_598_Capstone\Graphs\RacePercentages"

    data = pd.read_csv(csv_file_path)

    percentage_columns = [
        'PercentNonResidentUndergrad',
        'PercentHispanicUndergrad',
        'PercentBlackUndergrad',
        'PercentWhiteUndergrad',
        'PercentNativeAmericanUndergrad',
        'PercentAsianUndergrad',
        'PercentPacificIslanderUndergrad'
    ]

    plot_percentage_distributions(data, percentage_columns, output_filepath)

    print(f"Done! Percentage distribution plot saved at {output_filepath}")

main()
