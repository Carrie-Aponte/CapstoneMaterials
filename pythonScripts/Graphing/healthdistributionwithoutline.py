import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_percentage_distributions(data, percentage_columns, output_filepath):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    plt.figure(figsize=(12, 8))
    ax = plt.gca()

    num_cols = len(percentage_columns)
    base_color = sns.color_palette("viridis", num_cols)

    palette = [(*base_color[i], 0.7) for i in range(num_cols)]

    for index, col in enumerate(percentage_columns):
        counts = data[col].value_counts(normalize=True).sort_index()

        ax.bar(counts.index + 0.1 * index, counts.values, width=0.1, label=col, color=palette[index])

    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.title("Distribution of Health Variables")

    plt.legend()

    plt.savefig(output_filepath)
    plt.show()

def main():
    csv_file_path = r"C:\Users\carrie\Documents\CIS890_DataPractice\Dataset\csv_William _Duncan_Wyandotte_County_Data.csv"
    output_filepath = r'C:\Users\carrie\Documents\CIS_598_Capstone\Percentage_Health_Distribution2\percentage_distribution2.png'

    data = pd.read_csv(csv_file_path)

    percentage_columns = [
        'Hypertension',
        'CardiovascularDisease',
        'AvoidedCareDueToCost',
        'HighCholesterol',
        'DepressionWomen',
        'MultipleChronicConditions',
        'FoodInsecurity'
    ]

    plot_percentage_distributions(data, percentage_columns, output_filepath)

    print(f"Done! Percentage distribution plot saved at {output_filepath}")

main()
