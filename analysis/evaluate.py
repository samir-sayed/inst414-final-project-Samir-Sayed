from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def evaluate_model(y_true, y_pred):
    #calculate metrics
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    print(f'Mean Absolute Error (MAE): {mae:.2f}')
    print(f'Mean Squared Error (MSE): {mse:.2f}')
    print(f'R-squared: {r2:.2f}')
    
    
    metrics = pd.DataFrame({
            'Metric': ['MAE', 'MSE', 'R-squared'],
            'Value': [mae, mse, r2]
        })
    metrics_path = 'data/metrics/regression_metrics.csv'
    metrics.to_csv(metrics_path, index=False)
    
    
    
    #plot
    plt.figure(figsize=(10, 6))
    residuals = y_true - y_pred
    sns.histplot(residuals, kde=True)
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    plt.title('Residuals Distribution')
    plt.savefig('data/charts/residuals_distribution.png')
    plt.show()
    plt.close()
    
    #plot prediction vs actual
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values')
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)  # Diagonal line
    plt.show()

    return mae, mse, r2
