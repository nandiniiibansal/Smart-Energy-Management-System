import pandas as pd

# -----------------------------------------
# 1. Load cleaned dataset
# -----------------------------------------

file_path = "data/cleaned_energy_consumption.parquet"

df = pd.read_parquet(file_path)

print("Cleaned dataset loaded successfully!")

# -----------------------------------------
# 2. Make sure data is sorted by time
# -----------------------------------------

df = df.sort_values("Timestamp").reset_index(drop=True)

# -----------------------------------------
# 3. Create time-based features
# -----------------------------------------

df["hour"] = df["Timestamp"].dt.hour

df["day"] = df["Timestamp"].dt.day

df["day_of_week"] = df["Timestamp"].dt.dayofweek

df["month"] = df["Timestamp"].dt.month

df["is_weekend"] = (
    df["day_of_week"] >= 5
).astype(int)

# -----------------------------------------
# 4. Create lag features
# -----------------------------------------

# Previous hour
df["lag_1"] = df["Global_active_power"].shift(60)

# Previous day
df["lag_24"] = df["Global_active_power"].shift(1440)

# Previous week
df["lag_168"] = df["Global_active_power"].shift(10080)

# -----------------------------------------
# 5. Create rolling averages
# -----------------------------------------

# Previous hour average
df["rolling_mean_1h"] = (
    df["Global_active_power"]
    .shift(1)
    .rolling(60)
    .mean()
)

# Previous day average
df["rolling_mean_24h"] = (
    df["Global_active_power"]
    .shift(1)
    .rolling(1440)
    .mean()
)

# -----------------------------------------
# 6. Remove rows created by lagging
# -----------------------------------------

df.dropna(inplace=True)

df.reset_index(drop=True, inplace=True)

# -----------------------------------------
# 7. Display results
# -----------------------------------------

print("\nFeature engineering completed!")

print("\nNew columns:")
print(df.columns.tolist())

print("\nNew dataset shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

# -----------------------------------------
# 8. Save feature dataset
# -----------------------------------------

output_path = "data/features_energy_consumption.parquet"

df.to_parquet(
    output_path,
    index=False
)

print("\nFeature dataset saved successfully!")
print("Saved to:", output_path)