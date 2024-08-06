
from etl.extract import extract_data
from etl.transform import transform
from etl.load import load_data
from analysis.model import train_model
from analysis.evaluate import evaluate_model
from vis.visualizations import create_visualizations
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # ETL
        logging.info('Starting ETL process...')
        raw = extract_data()  # Extract data
        transformed_data = transform(raw)  # Transform data
        load_data(transformed_data)  # Load data
        
        # Analysis
        logging.info('Training model...')
        model, X_test, y_test = train_model(transformed_data)
        y_prediction = model.predict(X_test)
        
        # Evaluate the model
        logging.info('Evaluating model...')
        mae, mse, r2 = evaluate_model(y_test, y_prediction)
        
        # Visualization
        logging.info('Creating visualizations...')
        create_visualizations(transformed_data, y_test, y_prediction)
        
        logging.info('Process completed successfully.')
    
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
