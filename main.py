from etl.extract import extract_data
from etl.transform import transform
from etl.load import load_data


def main():
    
    #ETL
    raw = extract_data()
    
    
    data1 = extract_data() #extract
    transformed_data = transform(raw)
    load_data(transformed_data)
    
  


if __name__ == "__main__":
    main()
    