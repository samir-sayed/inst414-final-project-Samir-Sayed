import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(cleaned_data):
    cleaned_data = cleaned_data.dropna(subset=['TIME OCC', 'Crm Cd Desc']) # Drop missing values
    
    label_encode = LabelEncoder() # Turn the descriptions into numeric codes
    cleaned_data['Crm Cd Desc Encoded'] = label_encode.fit_transform(cleaned_data['Crm Cd Desc'])
    
    X = cleaned_data[['Crm Cd Desc Encoded']] # Features
    y = cleaned_data['TIME OCC']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Split data
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Generate predictions
    y_pred = model.predict(X_test)
    
    # Print Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    # Plot predictions vs actual values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)  # Diagonal line
    plt.show()

    return model, X_test, y_test

    
