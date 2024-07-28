import os
import pandas as pd

def load_data(data1):
    processed_data_path = os.path.join('data' , 'processed', 'cleaned_data.csv')
    data1.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")
    