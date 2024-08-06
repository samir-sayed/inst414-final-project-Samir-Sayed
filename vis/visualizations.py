# vis/visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_crime_counts_by_hour(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='TIME OCC')
    plt.title('Crime Counts by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=45)
    plt.show()

def plot_crime_type_distribution(data):
    plt.figure(figsize=(12, 8))
    data['Crm Cd Desc'].value_counts().head(20).plot(kind='bar')
    plt.title('Top 20 Crime Types')
    plt.xlabel('Crime Type')
    plt.ylabel('Number of Incidents')
    plt.xticks(rotation=90)
    plt.show()

def plot_model_performance(y_true, y_pred):
    plt.figure(figsize=(10, 6))
    sns.histplot(y_true - y_pred, kde=True)
    plt.title('Residuals Distribution')
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    plt.show()

def create_visualizations(data, y_true=None, y_pred=None):
    plot_crime_counts_by_hour(data)
    plot_crime_type_distribution(data)
    if y_true is not None and y_pred is not None:
        plot_model_performance(y_true, y_pred)
