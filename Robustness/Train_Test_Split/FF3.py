# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("climate_final_with_ff5_and_excess_return.csv")

features_ff3 = ['Mkt-RF', 'SMB', 'HML']
target = 'excess_RET'

X_ff3 = df[features_ff3]
y_ff3 = df[target]

# Split the data (80% training, 20% testing)
X_train_ff3, X_test_ff3, y_train_ff3, y_test_ff3 = train_test_split(X_ff3, y_ff3, test_size=0.2, random_state=42)

# Linear Regression
lin_model_ff3 = LinearRegression()
lin_model_ff3.fit(X_train_ff3, y_train_ff3)
y_pred_lin_ff3 = lin_model_ff3.predict(X_test_ff3)
rmse_lin_ff3 = np.sqrt(mean_squared_error(y_test_ff3, y_pred_lin_ff3))
r2_lin_ff3 = r2_score(y_test_ff3, y_pred_lin_ff3)

# Ridge Regression with scaling
ridge_ff3 = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
ridge_ff3.fit(X_train_ff3, y_train_ff3)
y_pred_ridge_ff3 = ridge_ff3.predict(X_test_ff3)
rmse_ridge_ff3 = np.sqrt(mean_squared_error(y_test_ff3, y_pred_ridge_ff3))
r2_ridge_ff3 = r2_score(y_test_ff3, y_pred_ridge_ff3)

# Random Forest Regression
rf_ff3 = RandomForestRegressor(n_estimators=100, random_state=42)
rf_ff3.fit(X_train_ff3, y_train_ff3)
y_pred_rf_ff3 = rf_ff3.predict(X_test_ff3)
rmse_rf_ff3 = np.sqrt(mean_squared_error(y_test_ff3, y_pred_rf_ff3))
r2_rf_ff3 = r2_score(y_test_ff3, y_pred_rf_ff3)


print("FF3 Model Performance on Test Set:\n")
print(f"Linear Regression:     RMSE = {rmse_lin_ff3:.4f}, R^2 = {r2_lin_ff3:.4f}")
print(f"Ridge Regression:      RMSE = {rmse_ridge_ff3:.4f}, R^2 = {r2_ridge_ff3:.4f}")
print(f"Random Forest:         RMSE = {rmse_rf_ff3:.4f}, R^2 = {r2_rf_ff3:.4f}")
