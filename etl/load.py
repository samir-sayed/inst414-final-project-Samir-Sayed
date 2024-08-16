import os
import pandas as pd



def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def load_data(data1):
    processed_data_dir = 'data/processed'
    create_directory(processed_data_dir) 
    processed_data_path = os.path.join(processed_data_dir, 'cleaned_data.csv')
    data1.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")
    