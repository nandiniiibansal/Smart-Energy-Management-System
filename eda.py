import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# 1. Load cleaned dataset
# -----------------------------------------

file_path = "data/cleaned_energy_consumption.parquet"

df = pd.read_parquet(file_path)

print("Cleaned dataset loaded successfully!")

# -----------------------------------------
# 2. Basic information
# -----------------------------------------

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

# -----------------------------------------
# 3. Statistical summary
# -----------------------------------------

print("\nStatistical summary:")
print(df.describe())

# -----------------------------------------
# 4. Energy consumption information
# -----------------------------------------

print("\nGlobal Active Power statistics:")

print("Minimum:",
      df["Global_active_power"].min(), "kW")

print("Maximum:",
      df["Global_active_power"].max(), "kW")

print("Average:",
      df["Global_active_power"].mean(), "kW")

# -----------------------------------------
# 5. Plot energy consumption
# -----------------------------------------

plt.figure(figsize=(12, 5))

plt.plot(
    df["Timestamp"].iloc[:1440],
    df["Global_active_power"].iloc[:1440]
)

plt.xlabel("Time")
plt.ylabel("Global Active Power (kW)")
plt.title("Energy Consumption - First 24 Hours")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# -----------------------------------------
# 6. Daily average consumption
# -----------------------------------------

df["Date_only"] = df["Timestamp"].dt.date

daily_average = (
    df.groupby("Date_only")["Global_active_power"]
    .mean()
)

print("\nDaily average consumption:")
print(daily_average.head(10))

# -----------------------------------------
# 7. Plot daily average
# -----------------------------------------

plt.figure(figsize=(12, 5))

plt.plot(daily_average.index, daily_average.values)

plt.xlabel("Date")
plt.ylabel("Average Power (kW)")
plt.title("Daily Average Energy Consumption")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()