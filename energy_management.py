import pandas as pd

# -----------------------------------------
# 1. Load predicted energy demand
# -----------------------------------------

input_path = "results/energy_predictions.csv"

df = pd.read_csv(input_path)

print("Prediction data loaded successfully!")


# -----------------------------------------
# 2. Simulated microgrid parameters
# -----------------------------------------

# Solar generation (kW)
# Temporary simulated values
df["Solar_Generation"] = 0.5

# Battery parameters
battery_capacity = 5.0       # kWh
battery_soc = 2.5            # Initial battery energy in kWh
battery_max_charge = 5.0
battery_min_soc = 0.5

# Battery charge/discharge rate
max_battery_charge = 1.0
max_battery_discharge = 1.0


# -----------------------------------------
# 3. Energy management algorithm
# -----------------------------------------

battery_energy = []
grid_energy = []
solar_used = []
battery_used = []
solar_excess = []

for _, row in df.iterrows():

    demand = row["Predicted_Active_Power"]
    solar = row["Solar_Generation"]

    # -----------------------------
    # Solar supplies load first
    # -----------------------------

    solar_to_load = min(solar, demand)

    remaining_demand = demand - solar_to_load

    excess_solar = max(0, solar - demand)

    # -----------------------------
    # Charge battery with excess solar
    # -----------------------------

    charge = min(
        excess_solar,
        max_battery_charge,
        battery_max_charge - battery_soc
    )

    battery_soc += charge

    excess_solar -= charge

    # -----------------------------
    # Battery supplies remaining load
    # -----------------------------

    discharge = min(
        remaining_demand,
        max_battery_discharge,
        battery_soc - battery_min_soc
    )

    battery_soc -= discharge

    remaining_demand -= discharge

    # -----------------------------
    # Grid supplies remaining load
    # -----------------------------

    grid = max(0, remaining_demand)

    # Store results
    solar_used.append(solar_to_load)
    battery_used.append(discharge)
    grid_energy.append(grid)
    battery_energy.append(battery_soc)
    solar_excess.append(excess_solar)


# -----------------------------------------
# 4. Add results to dataframe
# -----------------------------------------

df["Solar_Used"] = solar_used
df["Battery_Used"] = battery_used
df["Grid_Energy"] = grid_energy
df["Battery_SOC"] = battery_energy
df["Solar_Excess"] = solar_excess


# -----------------------------------------
# 5. Display results
# -----------------------------------------

print("\n========== EMS RESULTS ==========")

print(
    df[
        [
            "Timestamp",
            "Predicted_Active_Power",
            "Solar_Used",
            "Battery_Used",
            "Grid_Energy",
            "Battery_SOC"
        ]
    ].to_string(index=False)
)

print("=================================")


# -----------------------------------------
# 6. Save EMS results
# -----------------------------------------

output_path = "results/ems_results.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nEMS results saved successfully!")
print("Saved to:", output_path)