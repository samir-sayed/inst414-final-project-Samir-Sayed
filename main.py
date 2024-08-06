from etl.extract import extract_data
from etl.transform import transform
from etl.load import load_data
from analysis.model import train_model
from analysis.evaluate import evaluate_model
from vis.visualizations import create_visualizations



def main():
    
    #ETL
    raw = extract_data()
    
    
    data1 = extract_data() #extract
    transformed_data = transform(raw)
    load_data(transformed_data)
    
  
  
    # Analysis
    model, X_test, y_test = train_model(transformed_data)
    y_prediction = model.predict(X_test)
    
    # Evaluate the model
    mae, mse, r2 = evaluate_model(y_test, y_prediction)
    
    # Visualization
    create_visualizations(transformed_data, y_test, y_prediction)

if __name__ == "__main__":
    main()
    