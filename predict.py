import pandas as pd
import joblib

# -----------------------------------------
# 1. Load feature dataset
# -----------------------------------------

data_path = "data/features_energy_consumption.parquet"

df = pd.read_parquet(data_path)

print("Feature dataset loaded successfully!")


# -----------------------------------------
# 2. Load trained model
# -----------------------------------------

model_path = "models/energy_prediction_model.pkl"

model = joblib.load(model_path)

print("Trained model loaded successfully!")


# -----------------------------------------
# 3. Define features
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


# -----------------------------------------
# 4. Select recent data
# -----------------------------------------

prediction_data = df.tail(24).copy()

X_prediction = prediction_data[features]


# -----------------------------------------
# 5. Generate predictions
# -----------------------------------------

predictions = model.predict(X_prediction)


# -----------------------------------------
# 6. Display predictions
# -----------------------------------------

prediction_data["Predicted_Active_Power"] = predictions

print("\n========== ENERGY PREDICTIONS ==========")

print(
    prediction_data[
        [
            "Timestamp",
            "Global_active_power",
            "Predicted_Active_Power"
        ]
    ].to_string(index=False)
)

print("=========================================")


# -----------------------------------------
# 7. Save predictions
# -----------------------------------------

output_path = "results/energy_predictions.csv"

prediction_data[
    [
        "Timestamp",
        "Global_active_power",
        "Predicted_Active_Power"
    ]
].to_csv(
    output_path,
    index=False
)

print("\nPredictions saved successfully!")
print("Saved to:", output_path)
