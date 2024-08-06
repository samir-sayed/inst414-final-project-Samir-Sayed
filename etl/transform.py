import os
import pandas as pd
import matplotlib.pyplot as plt


def clean_data(data1):
    data1 = data1.dropna()
    
    #unique ID
    if 'id' not in data1.columns:
        data1['id'] = range(1, len(data1) + 1)
    
    #delete unneccesary columns that we are not interested in
    
    columns_to_drop = ['AREA', 'Date Rptd', 'DATE OCC']
    columns_to_drop = [col for col in columns_to_drop if col in data1.columns]
    data1 = data1.drop(columns=columns_to_drop)
    
    return data1
    
    
    
    
#EDA
def perform_eda(data1):
    
    #use this as a failsafe in case data is not being returned
    if data1 is None:
        print("No data for EDA.")
        return None
    print(data1.describe())
    
    
    #create a histogram for one of the columns, more will be added later
    if 'TIME OCC' in data1.columns:
        data1['TIME OCC'].hist()
        plt.title('Distribution of Time of Crimes')
        plt.xlabel('TIME')
        plt.ylabel('Frequency')
        plt.show()
        
    return data1    


#Apply cleaning fuctions and transform

def transform(data1):
    cleaned_data = clean_data(data1)
    
    perform_eda(cleaned_data)
    
    processed_data_path = os.path.join('data', 'processed', 'cleaned_data.csv')
    cleaned_data.to_csv(processed_data_path, index=False)
    return cleaned_data
    
if __name__ == "__main__":
    csv_path = "https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"
    data1 = pd.read_csv(csv_path)
    
    cleaned_data = transform(data1)
    if cleaned_data is not None:
            print(cleaned_data.head())
    else:
        print(f"File {csv_path} does not exist.") #failsafe