import os
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')




def create_directory(path):
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        
        
def extract_data():
    try:
        data_dir = 'data/raw'
        create_directory(data_dir)
        csv_path = os.path.join(data_dir, 'crime_data.csv')
        
        
        csv_path = "https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"
        data1 = pd.read_csv(csv_path)
        data1.to_csv(csv_path, index=False)
        logging.info(f"Data extracted successfully with {data1.shape[0]} rows and {data1.shape[1]} columns.")
        return data1
    except Exception as e:
        logging.error(f"Failed to load data: {str(e)}")
        return None

if __name__ == "__main__":
    data1 = extract_data()
    print(data1)