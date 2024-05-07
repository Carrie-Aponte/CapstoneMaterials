import matplotlib.pyplot as plt

features = [
    "Cardiovascular Disease",
    "Multiple Chronic Conditions",
    "Infant Mortality",
    "Food Insecurity",
    "Percent Black",
    "Median Wage",
    "Child Mortality",
    "Cost of Living Index"
]


outliers_removed_scores = [
    0.8873,
    0.868,
    0.7579,
    0.6862,
    0.6197,
    -0.6179,
    0.5586,
    -0.5211
]

plt.figure(figsize=(12, 8))
bar_width = 0.35
index = range(len(features))

plt.bar(index, outliers_removed_scores, width=bar_width, color='r', align='edge')

plt.xlabel('Feature')
plt.ylabel('Score')
plt.title('Feature Selection Results on Hypertension')
plt.xticks(index, features, rotation=45, ha='right')
plt.legend()

plt.tight_layout()
plt.show()
