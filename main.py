from etl.extract import extract_data
from etl.transform import transform
from etl.load import load_data
from analysis.model import train_model
from analysis.evaluate import evaluate_model
from vis.visualizations import create_visualizations
import logging

#logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info('Starting ETL process...')
        raw = extract_data()  #EXTRACT
        if raw is None or raw.empty:
            logging.error("No data extracted. Terminating process.")
            return
        logging.info(f'Extracted data with {raw.shape[0]} rows.')

        transformed_data = transform(raw)  #TRANSFORM
        if transformed_data is None or transformed_data.empty:
            logging.error("Data transformation failed. Terminating process.")
            return
        logging.info(f'Transformed data with {transformed_data.shape[0]} rows.')

        load_data(transformed_data)  #LOAD

        
        
        #MODEL / EVALUATION
        logging.info('Training model...')
        model, X_test, y_test = train_model(transformed_data)
        if model is None:
            logging.error("Model training failed. Terminating process.")
            return

        y_prediction = model.predict(X_test)
        logging.info('Evaluating model...')
        metrics = evaluate_model(y_test, y_prediction) 

        logging.info('Creating visualizations...')
        create_visualizations(transformed_data, y_test, y_prediction)

        logging.info('Process completed successfully.')

    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
