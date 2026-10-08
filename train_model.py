import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# -----------------------------------------
# 1. Load feature dataset
# -----------------------------------------

file_path = "data/features_energy_consumption.parquet"

df = pd.read_parquet(file_path)

print("Feature dataset loaded successfully!")
print("Dataset shape:", df.shape)


# -----------------------------------------
# 2. Define input features and target
# -----------------------------------------

features = [
    "hour",
    "day",
    "day_of_week",
    "month",
    "is_weekend",
    "lag_1",
    "lag_24",
    "lag_168",
    "rolling_mean_1h",
    "rolling_mean_24h"
]

target = "Global_active_power"

X = df[features]
y = df[target]


# -----------------------------------------
# 3. Time-series train/test split
# -----------------------------------------

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# -----------------------------------------
# 4. Train Random Forest
# -----------------------------------------

print("\nTraining model...")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Model training completed!")


# -----------------------------------------
# 5. Make predictions
# -----------------------------------------

y_pred = model.predict(X_test)


# -----------------------------------------
# 6. Evaluate model
# -----------------------------------------

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

r2 = r2_score(y_test, y_pred)


print("\n========== MODEL PERFORMANCE ==========")

print("MAE :", mae)
print("RMSE:", rmse)
print("R²  :", r2)

print("=======================================")
# -----------------------------------------
# 7. Save trained model
# -----------------------------------------

model_path = "models/energy_prediction_model.pkl"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Saved to:", model_path)