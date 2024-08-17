import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(data1):
    #drop rows with missing values in columns of interest
    cleaned_data = data1.dropna(subset=['TIME OCC', 'Crm Cd Desc', 'Vict Age', 'AREA NAME'])

    #encoding for cateorical features
    label_encode_crm = LabelEncoder()
    label_encode_area = LabelEncoder()

    cleaned_data['Crm Cd Desc Encoded'] = label_encode_crm.fit_transform(cleaned_data['Crm Cd Desc'])
    cleaned_data['AREA NAME Encoded'] = label_encode_area.fit_transform(cleaned_data['AREA NAME'])

    #set x as the features after they have been encoded , and y as TIME OCC
    X = cleaned_data[['Crm Cd Desc Encoded', 'Vict Age', 'AREA NAME Encoded']]
    y = cleaned_data['TIME OCC']
    
    #split data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    #generate
    y_pred = model.predict(X_test)
    
    #calculate MSE
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    #Plot pred vs actual
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.xlabel('Actual TIME OCC')
    plt.ylabel('Predicted TIME OCC')
    plt.title('Actual vs Predicted TIME OCC')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)  # Diagonal line
    plt.show()

    return model, X_test, y_test
