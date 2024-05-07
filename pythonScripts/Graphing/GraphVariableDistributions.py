import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\carrie\Documents\CIS890_DataPractice\Dataset\onlypreemptedstates_numericalonly_yearsadded_csv_William _Duncan_Wyandotte_County_Data.csv")

#columns_to_visualize = ['CurrentMinimumWage', 'Preemption', 'Hypertension', 'CardiovascularDisease', 'AvoidedCareDueToCost', 'DrugDeaths', 'Suicide', 'HighCholesterol', 'DepressionWomen', 'MultipleChronicConditions', 'IncomeInequality', 'ViolentCrimeRate', 'ChildMortality', 'InfantMortality', 'PercentBlack', 'PercentWhite', 'MedianWage', 'CostOfLivingIndex', 'HousingInsecurity','FoodInsecurity']
columns_to_visualize = ['YearPreempted']

for column in columns_to_visualize:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True, color='skyblue')
    plt.title(f'Distribution of {column}', fontsize=16)
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)
    plt.show()
