import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("climate_final_with_ff5_and_excess_return.csv")

features = ['Overall_ESG_Exposure', 'Overall_ESG_Sentiment', 'Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA']
target = 'excess_RET'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred_lin = lin_model.predict(X_test)
rmse_lin = np.sqrt(mean_squared_error(y_test, y_pred_lin))
r2_lin = r2_score(y_test, y_pred_lin)

# Ridge Regression with scaling
ridge = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)
rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
r2_ridge = r2_score(y_test, y_pred_ridge)

# Random Forest Regression
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
r2_rf = r2_score(y_test, y_pred_rf)

print("Model Performance on Test Set:\n")
print(f"Linear Regression:     RMSE = {rmse_lin:.4f}, R^2 = {r2_lin:.4f}")
print(f"Ridge Regression:      RMSE = {rmse_ridge:.4f}, R^2 = {r2_ridge:.4f}")
print(f"Random Forest:         RMSE = {rmse_rf:.4f}, R^2 = {r2_rf:.4f}")

