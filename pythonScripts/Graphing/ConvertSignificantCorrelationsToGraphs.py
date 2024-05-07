import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from matplotlib.backends.backend_pdf import PdfPages

def plot_correlations(data_file, output_path):
    with open(data_file, 'r') as f:
        lines = f.readlines()
    correlations = {}
    for line in lines:
        print(f"Processing line: {line.strip()}")
        if line.startswith("Correlation between"):
            match = re.search(r"'(.*?)' and '(.*?)':", line)
            if match:
                var1 = match.group(1)
                var2 = match.group(2)
                if var1 not in correlations:
                    correlations[var1] = []
                correlations[var1].append((var2, None, None))
        
        elif line.startswith("Pearson correlation coefficient:"):
            match_coefficient = re.search(r": ([-+]?\d*\.\d+|\d+)$", line)
            if match_coefficient:
                coefficient = float(match_coefficient.group(1))
                correlations[var1][-1] = (correlations[var1][-1][0], coefficient, None)
        
        elif line.startswith("P-value:"):
            match_pvalue = re.search(r": ([-+]?\d*\.\d+|\d+)$", line)
            if match_pvalue:
                pvalue = float(match_pvalue.group(1))
                correlations[var1][-1] = (correlations[var1][-1][0], correlations[var1][-1][1], pvalue)

    with PdfPages(output_path) as pdf:
        for variable, data in correlations.items():   
            if data:
                plt.figure(figsize=(10, 6))
                sns.set(style="whitegrid")
                correlated_features = [entry[0] for entry in data]
                coefficients = [entry[1] for entry in data]
                pvalues = [entry[2] for entry in data]

                ax = sns.barplot(x=coefficients, y=correlated_features, palette="pastel", orient="h")
                for i, pvalue in enumerate(pvalues):
                    ax.text(coefficients[i], i, f"({pvalue:.4f})", va="center", fontsize=10)
                
                plt.title(f"Significant Correlations with {variable}")
                plt.xlabel("Pearson Correlation Coefficient")
                plt.ylabel("Correlated Feature")
                plt.tight_layout()

                try:
                    pdf.savefig()
                    plt.close()
                except Exception as e:
                    print(f"Error occurred while saving plot for {variable}: {e}")
            else:
                print(f"Looks like theres nothing significant for {variable} - ya done out of luck")

def main():
    data_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\PearsonCorrelationsAndPValues\CombinedDatasets\HypertensionCorrelations.txt"
    output_file_path = r"C:\Users\carrie\Documents\CIS_598_Capstone\Graphs\AllSignificantCorrelations\HypertensionGraphed.pdf"
    plot_correlations(data_file_path, output_file_path)
    print(f"Nice :3 All plots are in {output_file_path}!")


main()