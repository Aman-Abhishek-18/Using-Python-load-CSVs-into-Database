import pandas as pd
from sqlalchemy import create_engine

# Define your connection string with the ODBC driver name
conn_string = (
    "mssql+pyodbc://sa:test123@localhost/SQLCaseStudyDB"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)
try:
    # Create an engine
    engine = create_engine(conn_string)
    
    # Load your CSV file
    df = pd.read_csv(r'C:\Users\amana\OneDrive\Desktop\Python-MS SQL Server\SQL Case Study - Datasets\artist.csv')

    # Example operation: Writing data to SQL Server
    df.to_sql('artist', con=engine, if_exists='replace', index=False)

    print("Data loaded successfully.")
    print(df.info)

except Exception as e:
    print(f"An error occurred: {str(e)}")
