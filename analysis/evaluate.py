import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def evaluate_model(y_true, y_pred):
    create_directory('data/metrics')  #makes sure directory exists
    metrics_path = 'data/metrics/regression_metrics.csv'

    #calculate metrics
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    #save metrics to csv in data/
    metrics = pd.DataFrame({
        'Metric': ['MAE', 'MSE', 'R-squared'],
        'Value': [mae, mse, r2]
    })
    metrics.to_csv(metrics_path, index=False)

    

    

    return metrics
