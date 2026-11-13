# SMART ENERGY MANAGEMENT SYSTEM

## 1. Project Overview
The **Smart Energy Management System (EMS)** is a software-based project designed to demonstrate intelligent energy monitoring, consumption prediction, and energy management using machine learning.

The system focuses on managing energy from three sources:
- Solar Energy
- Battery Storage
- Grid Supply

The project uses historical household electricity consumption data to predict future energy demand. Based on the predicted demand and simulated solar and battery parameters, an energy management algorithm determines how the available energy sources can be utilized efficiently.
The project also includes a software dashboard prototype developed to visualize energy consumption, solar utilization, battery status, and energy source allocation.
**Note:** This is a simulation-based academic prototype. It does not involve a physical microgrid or real-time hardware integration.

## 2. Project Objectives

- Analyze historical electricity consumption patterns.
- Predict energy demand using machine learning.
- Simulate the operation of solar, battery, and grid energy sources.
- Implement an energy allocation strategy to prioritize renewable energy.
- Monitor energy consumption and source utilization through a software dashboard.
- Demonstrate how predictive analytics can support efficient energy management.

## 3. Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| ML Algorithm | Random Forest Regression |
| Data Visualization | Matplotlib |
| Model Persistence | Joblib |
| Development Environment | Python / VS Code |

## 4. System Workflow

The project follows these major stages:

1. **Data Loading:** Historical electricity consumption data is loaded from a CSV file.

2. **Data Preprocessing:** Missing values are identified and handled through interpolation and forward/backward filling. Date and time information is converted into timestamps.

3. **Exploratory Data Analysis:** Electricity consumption patterns, statistical information, and daily averages are analyzed and visualized.

4. **Feature Engineering:** Time-based features, lag values, and rolling averages are generated to capture consumption patterns.

5. **Model Training:** A Random Forest Regressor is trained to predict global active power consumption.

6. **Model Evaluation:** The model is evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² score.

7. **Energy Management:** Predicted energy demand is used as input to a rule-based energy allocation algorithm involving solar, battery, and grid sources.

8. **Visualization:** The energy management results are presented through a software dashboard prototype.

## 5. Machine Learning Approach

### Random Forest Regression

Random Forest Regression is used to predict electricity consumption based on historical consumption patterns and engineered time-based features.

The model uses 100 decision trees and combines their predictions to estimate energy demand.

**Input Features:**
- Hour
- Day
- Day of Week
- Month
- Weekend Indicator
- Previous Hour Consumption (Lag 1)
- Previous Day Consumption (Lag 24)
- Previous Week Consumption (Lag 168)
- One-Hour Rolling Average
- Twenty-Four-Hour Rolling Average

**Prediction Target:**

Global Active Power (electricity consumption in kW).

The dataset is divided chronologically into 80% training data and 20% testing data to maintain the time-series order.

### Model Evaluation Metrics

The following evaluation metrics are used:

- **MAE:** Measures the average absolute difference between actual and predicted values.
- **RMSE:** Measures prediction error while giving higher weight to larger errors.
- **R² Score:** Indicates how well the model explains the variation in electricity consumption.

## 6. Energy Management Algorithm

After predicting energy demand, the system applies a rule-based energy management strategy.

The energy allocation follows this priority:

**1. Solar Energy**
- Solar energy is utilized first to meet the predicted load demand.
- Any excess solar energy is used to charge the battery.

**2. Battery Storage**
- If solar energy is insufficient, the battery supplies the remaining demand.
- Battery charging and discharging are controlled using predefined capacity and rate limits.

**3. Grid Supply**
- If solar and battery energy are insufficient, the remaining demand is supplied by the electricity grid.

The algorithm maintains simulated battery parameters such as battery capacity, state of charge, minimum charge level, and charging/discharging limits.

This approach demonstrates how renewable energy utilization and battery storage can help reduce dependence on grid electricity.

## 7. Software Dashboard

A software dashboard prototype was developed separately to provide a visual representation of the energy management system.

The dashboard focuses on displaying:
- Energy consumption and predicted demand.
- Solar energy generation and utilization.
- Battery charge status.
- Grid energy consumption.
- Energy source allocation.
- Load management status.

The dashboard demonstrates how machine learning predictions and energy management logic can be presented in an understandable format.

The dashboard is a software simulation and does not receive live readings from physical solar panels, batteries, or electrical sensors.

## 8. Repository Structure

```text
Smart-Energy-Management-System/
│
├── load_data.py
├── eda.py
├── create_features.py
├── train_model.py
├── predict.py
├── energy_management.py
├── test.py
│
├── data/
│   ├── energy_consumption.csv
│   ├── cleaned_energy_consumption.parquet
│   └── features_energy_consumption.parquet
│
├── models/
│   └── energy_prediction_model.pkl
│
└── results/
    ├── energy_predictions.csv
    └── ems_results.csv
```

*Note: The data, models, and results folders represent the expected working-directory structure. These generated files are not currently included in the public repository.*

## 9. Installation and Setup

Clone the repository:

```bash
git clone https://github.com/nandiniiibansal/Smart-Energy-Management-System.git
```

Navigate to the project directory:

```bash
cd Smart-Energy-Management-System
```

Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn matplotlib joblib pyarrow
```

Place the electricity consumption dataset inside the `data/` directory with the filename:

```text
energy_consumption.csv
```

## 10. Project Implementation Files

| File | Purpose |
|---|---|
| `load_data.py` | Loads, preprocesses and cleans electricity consumption data. |
| `eda.py` | Performs exploratory data analysis and visualizes consumption patterns. |
| `create_features.py` | Generates time-based, lag and rolling-average features. |
| `train_model.py` | Trains and evaluates the Random Forest Regression model. |
| `predict.py` | Reserved for the prediction stage; implementation is currently incomplete. |
| `energy_management.py` | Implements the simulated solar-battery-grid energy allocation algorithm. |
| `test.py` | Testing and experimentation. |

**Implementation status:** Data preprocessing, feature engineering, model training and energy management logic are present in the repository. The prediction stage and complete end-to-end execution pipeline are still being integrated.

## 11. Limitations and Future Scope

### Current Limitations
- The system is based on software simulation rather than physical microgrid hardware.
- Solar generation and battery parameters are simulated using predefined values.
- The model uses historical household electricity consumption data.
- Real-time sensor integration and actual energy source switching are not implemented.
- The dashboard is a separate prototype and is not included in this repository.

### Future Enhancements
- Integrate real-time solar generation and battery monitoring.
- Connect IoT sensors and embedded hardware for live data acquisition.
- Improve prediction accuracy using additional machine learning and deep learning approaches.
- Implement real-time energy monitoring and automated load management.
- Deploy the dashboard as a web-based application.

## 12. Learning Outcomes

Through this project, we explored:
- Data preprocessing and exploratory data analysis.
- Time-series feature engineering.
- Machine learning-based regression.
- Model training and performance evaluation.
- Rule-based energy management.
- Software simulation and dashboard-based visualization.
- Application of machine learning to renewable energy management.

---

**Project Type:** Academic / Software Simulation

**Domain:** Machine Learning | Energy Management | Renewable Energy

**GitHub Repository:** https://github.com/nandiniiibansal/Smart-Energy-Management-System
