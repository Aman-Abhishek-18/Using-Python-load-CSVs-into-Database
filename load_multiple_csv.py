import pandas as pd
from sqlalchemy import create_engine

# Define your connection string with the ODBC driver name
conn_string = (
    "mssql+pyodbc://username:password@localhost/databaseName"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

try:
    # Create an engine
    engine = create_engine(conn_string)

    # List of files to load
    files = ['artist.csv', 'canvas_size.csv', 'image_link.csv', 
             'museum_hours.csv', 'museum.csv', 'product_size.csv', 
             'subject.csv', 'work.csv']

    # Iterate through each file
    for file in files:
        # Construct the full path to each CSV file
        file_path = fr'C:\Users\amana\OneDrive\Desktop\Python-MS SQL Server\SQL Case Study - Datasets\{file}'

        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Extract table name from file name (remove .csv extension)
        table_name = file.split('.')[0]

        # Write data to SQL Server
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        print(f"Data from {file} loaded successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
