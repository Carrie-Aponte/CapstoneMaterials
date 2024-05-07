import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\carrie\Documents\CIS_598_Capstone\OnlyNumerical_Combined_Datasets.csv")

target_column = 'CardiovascularDisease'
X = df.drop(columns=[target_column])  
y = df[target_column]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    'Random Forest': RandomForestRegressor(),
    'KNN (7 neighbors)': KNeighborsRegressor(n_neighbors=7),
    'Linear Regression': LinearRegression(),
    'Zero-R (Baseline)': DummyRegressor(strategy='mean')
}

results = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    results[model_name] = score

plt.figure(figsize=(10, 6))
plt.bar(results.keys(), results.values(), color='skyblue')
plt.title('Performance of Machine Learning Models')
plt.xlabel('Model')
plt.ylabel('Score (R-squared)')
plt.ylim(0, 1)  
plt.xticks(rotation=45, ha='right')
plt.show()

for model_name, score in results.items():
    print(f"{model_name}: Score (R-squared) = {score}")
