import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def plot_crime_type_distribution(data1):
    create_directory('data/charts')
    plt.figure(figsize=(12, 8))
    data1['Crm Cd Desc'].value_counts().head(20).plot(kind='bar')
    plt.title('Top 20 Crime Types')
    plt.xlabel('Crime Type')
    plt.ylabel('Number of Incidents')
    plt.xticks(rotation=90)
    plt.savefig('data/charts/crime_type_distribution.png')
    plt.close()
    
    
def plot_residuals(y_true, y_pred):
    create_directory('data/charts')
    residuals = y_true - y_pred
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.hlines(y=0, xmin=y_pred.min(), xmax=y_pred.max(), colors='red', linestyles='dashed')
    plt.xlabel('Predicted TIME OCC')
    plt.ylabel('Residuals')
    plt.title('Residuals vs Predicted TIME OCC')
    plt.savefig('data/charts/residuals_vs_predicted_time_occ.png')
    plt.close()

def plot_model_performance(y_true, y_pred):
    create_directory('data/charts')
    plt.figure(figsize=(10, 6))
    sns.histplot(y_true - y_pred, kde=True)
    plt.title('Residuals Distribution for TIME OCC Predictions')
    plt.xlabel('Residuals (Actual - Predicted TIME OCC)')
    plt.ylabel('Frequency')
    plt.savefig('data/charts/model_performance.png')
    plt.close()


def create_visualizations(data1, y_true=None, y_pred=None, classes=None):
    plot_crime_type_distribution(data1)
    if y_true is not None and y_pred is not None:
        plot_model_performance(y_true, y_pred)
        plot_residuals(y_true, y_pred)
        

