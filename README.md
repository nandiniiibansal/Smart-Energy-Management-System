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

### 7. Load Prediction Using Random Forest Regression

The project incorporates a machine learning-based load prediction module using a **Random Forest Regressor** to estimate energy consumption based on historical consumption patterns and engineered features.

The prediction process is implemented in `predict.py`.

**Prediction workflow:**

1. Load the feature-engineered dataset using Pandas.
2. Load the previously trained Random Forest model from the `models/` directory using Joblib.
3. Select the required input features used during model training.
4. Extract the latest 24 records from the feature-engineered dataset.
5. Pass these records to the trained model using `model.predict()`.
6. Generate predicted energy consumption values.
7. Compare actual and predicted consumption values.
8. Export the prediction results into a CSV file for further analysis.

**Input Features**

The prediction script uses the following ten features:

- Hour
- Day of the week
- Month
- Lag features
- Rolling statistics
- Other engineered time-based features

The prediction inputs must follow the same feature structure and ordering used during model training.

**Prediction Output**

The script generates actual-versus-predicted consumption results and saves them in:

`results/energy_predictions.csv`

This output can be used for further analysis and visualization.

### 8. Prediction Pipeline Implementation

The prediction module is implemented separately from model training to maintain a modular machine learning workflow.

| Component | Function |
|---|---|
| `train_model.py` | Trains the Random Forest Regression model |
| `predict.py` | Loads the trained model and generates predictions |
| `create_features.py` | Generates time-based and lag-based features |
| `results/energy_predictions.csv` | Stores actual and predicted consumption values |

This separation allows the trained model to be reused for generating predictions without retraining it every time.

### 9. Generated Outputs

The project generates the following outputs:

- Trained Random Forest model stored for reuse.
- Actual and predicted energy consumption values.
- CSV file containing prediction results.
- Model evaluation metrics generated during training, including MAE, RMSE and R².

The prediction results are stored in the `results/` directory.

### 10. Current Implementation Status

The project currently includes:

- Historical energy data preprocessing.
- Exploratory Data Analysis (EDA).
- Feature engineering and creation of time-based features.
- Random Forest Regression model training.
- Model evaluation using MAE, RMSE and R².
- Model loading and prediction using `predict.py`.
- Prediction of energy consumption for the latest 24 available records.
- Comparison of actual and predicted values.
- Export of prediction results to CSV.
- Energy management simulation using solar, battery and grid supply logic.

The interactive dashboard is a separately developed team component and is not part of the core prediction script.

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
