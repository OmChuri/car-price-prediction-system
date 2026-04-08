import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load the data
df = pd.read_csv('Car_Price_Prediction_Real.csv')

# Define features and target
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define which columns are categorical and which are numeric
categorical_cols = ['Make', 'Model', 'Fuel Type', 'Transmission', 'Owner', 'Location']
numeric_cols = ['Year', 'Engine Size', 'Mileage']

# Create preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Target transformation: Use Log for better distribution handling of prices
y_train_log = np.log1p(y_train)
y_test_log = np.log1p(y_test)

# Create a pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                          ('regressor', RandomForestRegressor(random_state=42))])

# Hyperparameter tuning for "Realistic Accuracy"
from sklearn.model_selection import GridSearchCV
param_grid = {
    'regressor__n_estimators': [100, 200],
    'regressor__max_depth': [None, 10, 20],
    'regressor__min_samples_split': [2, 5]
}

print("Starting grid search for optimal parameters...")
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train_log)

model = grid_search.best_estimator_

# Save the model
joblib.dump(model, 'car_price_model.pkl')
print(f"Model saved with best R2 score: {grid_search.best_score_:.4f}")
