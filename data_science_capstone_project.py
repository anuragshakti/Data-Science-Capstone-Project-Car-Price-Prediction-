# -*- coding: utf-8 -*-
"""Data Science Capstone Project_Anshu Priya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Q99R1S9xG0rTgGQT1W2y79rHk74j9uR
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Loading the Data set"""

df = pd.read_csv('/content/CAR DETAILS (1).csv')

"""Understand the data"""

# Display the first few rows of the dataset
print(df.head())

# Get an overview of the dataset
print(df.info())

# Check the statistical summary of numerical columns
print(df.describe())

"""Data Cleaning (if required)"""

# Handle missing values, duplicates, or any other data quality issues
# For example, to drop duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values
df.dropna(inplace=True)

"""Performing data analysis and visualization

Count of cars by fuel type
"""

plt.figure(figsize=(10, 6))
sns.countplot(x='fuel', data=df)
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()

"""Distribution of car prices

"""

plt.figure(figsize=(10, 6))
sns.histplot(df['selling_price'])
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

"""Average price by car transmission type

"""

plt.figure(figsize=(10, 6))
sns.barplot(x='transmission', y='selling_price', data=df)
plt.title('Average Price by Transmission Type')
plt.xlabel('Transmission Type')
plt.ylabel('Average Price')
plt.show()

"""Correlation heatmap of numerical features

"""

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""Applying varius Machine Learning techniques"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

"""Spliting the dataset into features (X) and target variable (y)

"""

df.head()

# Select the relevant features and target variable
columns_to_drop = ['name', 'selling_price']
X = df.drop(columns_to_drop, axis=1)
y = df['selling_price']

# Perform one-hot encoding on categorical variables
categorical_columns = ['fuel', 'seller_type', 'transmission', 'owner']
X_encoded = pd.get_dummies(X, columns=categorical_columns, drop_first=True)

"""Split the dataset into training and testing sets"""

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

"""Regression Models"""

linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)
linear_regression_predictions = linear_regression.predict(X_test)
linear_regression_mse = mean_squared_error(y_test, linear_regression_predictions)
linear_regression_mae = mean_absolute_error(y_test, linear_regression_predictions)
linear_regression_r2 = r2_score(y_test, linear_regression_predictions)

"""Decision Tree Regression"""

decision_tree = DecisionTreeRegressor()
decision_tree.fit(X_train, y_train)
decision_tree_predictions = decision_tree.predict(X_test)
decision_tree_mse = mean_squared_error(y_test, decision_tree_predictions)
decision_tree_mae = mean_absolute_error(y_test, decision_tree_predictions)
decision_tree_r2 = r2_score(y_test, decision_tree_predictions)

"""Random Forest Regression"""

random_forest = RandomForestRegressor()
random_forest.fit(X_train, y_train)
random_forest_predictions = random_forest.predict(X_test)
random_forest_mse = mean_squared_error(y_test, random_forest_predictions)
random_forest_mae = mean_absolute_error(y_test, random_forest_predictions)
random_forest_r2 = r2_score(y_test, random_forest_predictions)

"""Print the evaluation metrics"""

# Print the evaluation metrics
print("Linear Regression:")
print("Mean Squared Error (MSE):", linear_regression_mse)
print("Mean Absolute Error (MAE):", linear_regression_mae)
print("R-squared Score:", linear_regression_r2)
print()

print("Decision Tree Regression:")
print("Mean Squared Error (MSE):", decision_tree_mse)
print("Mean Absolute Error (MAE):", decision_tree_mae)
print("R-squared Score:", decision_tree_r2)
print()

print("Random Forest Regression:")
print("Mean Squared Error (MSE):", random_forest_mse)
print("Mean Absolute Error (MAE):", random_forest_mae)
print("R-squared Score:", random_forest_r2)

"""Saving the best model and Loading the model."""

import pickle

# Random Forest Regression (best model)
random_forest = RandomForestRegressor()
random_forest.fit(X_train, y_train)

# Save the model to a file
filename = 'random_forest_model.pkl'
pickle.dump(random_forest, open(filename, 'wb'))

# Load the model from the file
loaded_model = pickle.load(open(filename, 'rb'))

# Now you can use the loaded model for predictions
predictions = loaded_model.predict(X_test)

"""Applying the saved model on the same Dataset and test the model."""

import random
import numpy as np

# Randomly select 20 data points from the dataset
np.random.seed(42)  # Set a seed for reproducibility
random_data = df.sample(n=20)

# Randomly select 20 data points from the dataset
np.random.seed(42)  # Set a seed for reproducibility
random_data = df.sample(n=20)

# Load the saved model
try:
    loaded_model = pickle.load(open('random_forest_model.pkl', 'rb'))
except FileNotFoundError:
    print("Error: Model file not found.")
    exit()

# Preprocess the random data
random_features = random_data[['year', 'km_driven', 'seller_type', 'transmission', 'owner']]
random_features_encoded = pd.get_dummies(random_features)

# Make predictions using the loaded model
try:
    predictions = loaded_model.predict(random_features_encoded)
except ValueError:
    print("Error: Incompatible feature names. Please ensure the loaded model matches the feature names used during training.")
    exit()

# Display the actual selling prices and predicted prices
print("Actual Selling Prices:")
print(random_data['selling_price'])
print("\nPredicted Prices:")
print(predictions)
