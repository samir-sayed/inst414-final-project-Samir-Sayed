import os
import pandas as pd
import matplotlib.pyplot as plt


def clean_data(data1):
    print(data1.isnull().mean() * 100)  # Check NaN distribution

    #drop rows
    data1 = data1.dropna(subset=['Rpt Dist No', 'Part 1-2'])  # Adjust according to your needs

    #assign id
    if 'id' not in data1.columns:
        data1.loc[:, 'id'] = range(1, len(data1) + 1)
    
    #drop uneeded columns
    columns_to_drop = ['AREA', 'Date Rptd', 'DATE OCC']
    data1 = data1.drop(columns=[col for col in columns_to_drop if col in data1.columns])
    
    return data1
    
    
    
    
#EDA
def perform_eda(data1):
    
    #use this as a failsafe in case data is not being returned
    if data1 is None:
        print("No data for EDA.")
        return None
    print(data1.describe())
    
    
    #create a histogram TIME OCC vs frequence
    if 'TIME OCC' in data1.columns:
        data1['TIME OCC'].hist()
        plt.title('Distribution of Time of Crimes')
        plt.xlabel('TIME')
        plt.ylabel('Frequency')
        plt.savefig('data/charts/time_of_crime.png')
        plt.close()
        
        
    return data1    






#Apply cleaning fuctions and transform

def transform(data1):
    print(f"Initial data rows: {data1.shape[0]}")  #check for how many rows are in the initial dataset
    print(f"Cleaned data rows: {cleaned_data.shape[0]}")  # check after cleaning

    perform_eda(cleaned_data)

    processed_data_path = os.path.join('data', 'processed', 'cleaned_data.csv')
    cleaned_data.to_csv(processed_data_path, index=False)
    print(f"Data saved to {processed_data_path} with {cleaned_data.shape[0]} rows.")  #logging to show data as been saved
    return cleaned_data
    
    
    
    
    
    
if __name__ == "__main__":
    csv_path = "https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"
    data1 = pd.read_csv(csv_path)
    
    cleaned_data = transform(data1)
    if cleaned_data is not None:
            print(cleaned_data.head())
    else:
        print(f"File {csv_path} does not exist.") #failsafe