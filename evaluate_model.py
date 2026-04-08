import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load the model
model = joblib.load('car_price_model.pkl')

# Load the test data
df = pd.read_csv('Car_Price_Prediction_Real.csv')
X = df.drop('Price', axis=1)
y = df['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict (Log-scale)
y_pred_log = model.predict(X_test)

# Convert back to actual Price
y_pred = np.expm1(y_pred_log)

# Calculate metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Realistic Model Accuracy (R2 Score): {r2:.4f}")
print(f"Mean Absolute Error (MAE): ₹{mae:,.2f}")
print(f"Root Mean Squared Error (RMSE): ₹{rmse:,.2f}")
