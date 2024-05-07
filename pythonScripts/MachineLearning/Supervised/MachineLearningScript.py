import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.dummy import DummyRegressor

data = pd.read_csv(r"C:\Users\carrie\Documents\CIS_598_Capstone\Datasets\OnlyNumerical_Combined_Datasets.csv")
output_file = r"C:\Users\carrie\Documents\CIS_598_Capstone\MachineLearningResults\Combined_Datasets\PercentMenEnrolled.txt"

target_column = 'PercentMenEnrolled'
extra_column = 'PercentWomenEnrolled'
X = data.drop(target_column, axis=1)  
X = X.drop(extra_column, axis=1)  
y = data[target_column]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
with open(output_file, 'w') as f:
    f.write("Training Random Forest Regression...\n")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_predictions = rf_model.predict(X_test)
    rf_mse = mean_squared_error(y_test, rf_predictions)
    f.write(f"Random Forest MSE:\n {rf_mse}")
    rf_correlation_coefficient = np.corrcoef(y_test, rf_predictions)[0, 1]
    f.write(f"\nCorrelation Coefficient Random Forest:\n {rf_correlation_coefficient}\n\n")

    f.write("Training Linear Regression...\n")
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_predictions = lr_model.predict(X_test)
    lr_mse = mean_squared_error(y_test, lr_predictions)
    f.write(f"Linear Regression MSE:\n {lr_mse}")
    lr_correlation_coefficient = np.corrcoef(y_test, lr_predictions)[0, 1]
    f.write(f"\nCorrelation Coefficient Linear Regression:\n {lr_correlation_coefficient}\n\n")

    f.write("Training k-Nearest Neighbors Regression...\n")
    knn_model = KNeighborsRegressor(n_neighbors=7)
    knn_model.fit(X_train, y_train)
    knn_predictions = knn_model.predict(X_test)
    knn_mse = mean_squared_error(y_test, knn_predictions)
    f.write(f"k-Nearest Neighbors Regression (k=7) MSE:\n {knn_mse}")
    knn_correlation_coefficient = np.corrcoef(y_test, knn_predictions)[0, 1]
    f.write(f"\nCorrelation Coefficient KNN:\n {knn_correlation_coefficient}\n\n")

    f.write("Training ZeroR Regression...\n")
    zeroR_model = DummyRegressor(strategy='mean') 
    zeroR_model.fit(X_train, y_train)
    zeroR_predictions = zeroR_model.predict(X_test)
    zeroR_mse = mean_squared_error(y_test, zeroR_predictions)
    f.write(f"ZeroR Regression MSE:\n {zeroR_mse}")
    zr_correlation_coefficient = np.corrcoef(y_test, zeroR_predictions)[0, 1]
    f.write(f"\nCorrelation Coefficient ZeroR:\n {zr_correlation_coefficient:.16f}")
