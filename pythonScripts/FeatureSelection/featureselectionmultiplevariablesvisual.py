import matplotlib.pyplot as plt

features_preemption = [
    "Current Minimum Wage",
    "Median Wage",
    "Infant Mortality",
    "Cost of Living Index",
    "Multiple Chronic Conditions",
    "Hypertension",
    "Cardiovascular Disease"
]

outliers_removed_scores_preemption = [
    -0.58602,
    -0.538624,
    0.511136,
    -0.481738,
    0.421694,
    0.419647,
    0.411489
]

plt.figure(figsize=(10, 6))
index = range(len(features_preemption))

plt.bar(index, outliers_removed_scores_preemption, color='r', align='center')

plt.xlabel('Feature')
plt.ylabel('Score')
plt.title('Feature Selection Results for Preemption')
plt.xticks(index, features_preemption, rotation=45, ha='right')

plt.tight_layout()
plt.show()
