import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('student_data.csv')

# Display basic statistics
print("Data Summary:\n", data.describe())

# Check for missing values
print("Missing Values:\n", data.isnull().sum())

# Fill missing values (if any) with the mean of the column
data.fillna(data.mean(), inplace=True)

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.drop(['mental_health', 'academic_performance', 'physical_health'], axis=1))

# Convert scaled features back to a DataFrame
scaled_data = pd.DataFrame(scaled_features, columns=data.columns[:-3])

# Add the outcome columns back to the scaled DataFrame
scaled_data[['mental_health', 'academic_performance', 'physical_health']] = data[['mental_health', 'academic_performance', 'physical_health']]

# Split the data into training and testing sets
train_data, test_data = train_test_split(scaled_data, test_size=0.3, random_state=42)

# Separate features and targets
X_train = train_data.drop(['mental_health', 'academic_performance', 'physical_health'], axis=1)
Y_train = train_data[['mental_health', 'academic_performance', 'physical_health']]
X_test = test_data.drop(['mental_health', 'academic_performance', 'physical_health'], axis=1)
Y_test = test_data[['mental_health', 'academic_performance', 'physical_health']]

# Add a constant to the model (for the intercept)
X_train_const = sm.add_constant(X_train)
X_test_const = sm.add_constant(X_test)

# Fit the model for mental health
model_mental_health = sm.OLS(Y_train['mental_health'], X_train_const).fit()
print("Mental Health Model Summary:\n", model_mental_health.summary())

# Fit the model for academic performance
model_academic_performance = sm.OLS(Y_train['academic_performance'], X_train_const).fit()
print("Academic Performance Model Summary:\n", model_academic_performance.summary())

# Fit the model for physical health
model_physical_health = sm.OLS(Y_train['physical_health'], X_train_const).fit()
print("Physical Health Model Summary:\n", model_physical_health.summary())

# Predictions
Y_pred_mental_health = model_mental_health.predict(X_test_const)
Y_pred_academic_performance = model_academic_performance.predict(X_test_const)
Y_pred_physical_health = model_physical_health.predict(X_test_const)

# Evaluate the model
def evaluate_model(Y_true, Y_pred, label):
    mse = np.mean((Y_true - Y_pred) ** 2)
    print(f"{label} MSE: {mse}")

evaluate_model(Y_test['mental_health'], Y_pred_mental_health, "Mental Health")
evaluate_model(Y_test['academic_performance'], Y_pred_academic_performance, "Academic Performance")
evaluate_model(Y_test['physical_health'], Y_pred_physical_health, "Physical Health")

# Plotting predictions vs actuals
def plot_predictions(Y_true, Y_pred, label):
    plt.figure(figsize=(10, 6))
    plt.scatter(Y_true, Y_pred)
    plt.plot([Y_true.min(), Y_true.max()], [Y_true.min(), Y_true.max()], 'k--', lw=2)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title(f'{label} - Actual vs Predicted')
    plt.show()

plot_predictions(Y_test['mental_health'], Y_pred_mental_health, "Mental Health")
plot_predictions(Y_test['academic_performance'], Y_pred_academic_performance, "Academic Performance")
plot_predictions(Y_test['physical_health'], Y_pred_physical_health, "Physical Health")
