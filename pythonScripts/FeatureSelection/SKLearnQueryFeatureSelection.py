import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression, RFE
from sklearn.linear_model import LinearRegression


data = pd.read_csv(r"C:\Users\carrie\Documents\CIS_598_Capstone\Datasets\OnlyNumerical_Combined_Datasets.csv")
output_file = r"C:\Users\carrie\Documents\CIS_598_Capstone\FeatureSelectionResults\CombinedDatasets"

X = data.drop('PercentFTFYAppliedAdmitted', axis=1)  
y = data['PercentFTFYAppliedAdmitted'] 

feature_names = X.columns.tolist()

selector_f_reg = SelectKBest(score_func=f_regression, k=5)  
FRegression_selected = selector_f_reg.fit_transform(X, y)
selected_indices_f_reg = selector_f_reg.get_support(indices=True)
selected_features_f_reg = [feature_names[i] for i in selected_indices_f_reg]
print("Selected features by f_regression:\n", selected_features_f_reg)
print("")

selector_mutual_info = SelectKBest(score_func=mutual_info_regression, k=5)  
MIRegression_selected = selector_mutual_info.fit_transform(X, y)
selected_indices_mutual_info = selector_mutual_info.get_support(indices=True)
selected_features_mutual_info = [feature_names[i] for i in selected_indices_mutual_info]
print("Selected features by mutual_info_regression:\n", selected_features_mutual_info)
print("")
estimator = LinearRegression()
selector_rfe = RFE(estimator, n_features_to_select=5)  
NFeature_selected = selector_rfe.fit_transform(X, y)
selected_indices_rfe = selector_rfe.get_support(indices=True)
selected_features_rfe = [feature_names[i] for i in selected_indices_rfe]
print("Selected features by RFE:\n", selected_features_rfe)
print("")