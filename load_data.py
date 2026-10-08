import pandas as pd

# -----------------------------------------
# 1. Load dataset
# -----------------------------------------

file_path = "data/energy_consumption.csv"

df = pd.read_csv(
    file_path,
    sep=";",
    low_memory=False
)

print("Dataset loaded successfully!")
print("Original shape:", df.shape)


# -----------------------------------------
# 2. Replace missing-value markers
# -----------------------------------------

df.replace("?", pd.NA, inplace=True)


# -----------------------------------------
# 3. Create timestamp
# -----------------------------------------

df["Timestamp"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    dayfirst=True
)


# -----------------------------------------
# 4. Convert electrical columns to numeric
# -----------------------------------------

numeric_columns = [
    "Global_active_power",
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# -----------------------------------------
# 5. Check missing values
# -----------------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# -----------------------------------------
# 6. Handle missing values
# -----------------------------------------

df[numeric_columns] = df[numeric_columns].interpolate(
    method="linear"
)

df[numeric_columns] = df[numeric_columns].ffill()
df[numeric_columns] = df[numeric_columns].bfill()


# -----------------------------------------
# 7. Remove unnecessary Date and Time
# -----------------------------------------

df.drop(columns=["Date", "Time"], inplace=True)


# -----------------------------------------
# 8. Sort according to time
# -----------------------------------------

df.sort_values("Timestamp", inplace=True)

df.reset_index(drop=True, inplace=True)


# -----------------------------------------
# 9. Final checks
# -----------------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal shape:")
print(df.shape)

print("\nFirst 5 cleaned rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)
# -----------------------------------------
# 10. Save cleaned dataset
# -----------------------------------------

output_path = "data/cleaned_energy_consumption.parquet"

df.to_parquet(
    output_path,
    index=False
)

print("\nCleaned dataset saved successfully!")
print("Saved to:", output_path)