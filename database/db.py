# database/db.py
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///hospital.db')

# Load Excel data
df_Physicians = pd.read_excel("Xyris HIS_data.xlsx", sheet_name="Physicians")
df_Schedules = pd.read_excel("Xyris HIS_data.xlsx", sheet_name="Schedules")
df_Specialities = pd.read_excel("Xyris HIS_data.xlsx", sheet_name="Specialities")
df_Pricelist = pd.read_excel("Xyris HIS_data.xlsx", sheet_name="Pricelist")
df_Policy = pd.read_excel("Xyris HIS_data.xlsx", sheet_name="Policy")

# Insert data into tables
df_Physicians.to_sql('Physicians', con=engine, if_exists='replace', index=False)
df_Schedules.to_sql('Schedules', con=engine, if_exists='replace', index=False)
df_Specialities.to_sql('Specialities', con=engine, if_exists='replace', index=False)
df_Pricelist.to_sql('Pricelist', con=engine, if_exists='replace', index=False)
df_Policy.to_sql('Policy', con=engine, if_exists='replace', index=False)

# The code snippet above reads the data from the Excel file and inserts it into the respective tables in the SQLite database using the SQLAlchemy engine. The data is loaded into pandas DataFrames and then inserted into the tables using the to_sql method. The if_exists='replace' parameter ensures that the tables are replaced if they already exist in the database. The index=False parameter prevents the DataFrame index from being inserted as a separate column in the database table.