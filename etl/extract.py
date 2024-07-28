import os
import pandas as pd

def extract_data():
    #csv_path = os.path.join('data' , 'extracted' , 'crime_data.csv')
    csv_path = "https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"
    data1 = pd.read_csv(csv_path) #read the csv file and assign it to a variable (data1)
    
    print('Success') #using this as an indicator if the code is running well
    return data1 

if __name__ == "__main__":
    data1 = extract_data()
    print(data1)