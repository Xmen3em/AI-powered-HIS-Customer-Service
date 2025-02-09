# vectorization/vectorize.py
from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import sys
import os
from dotenv import load_dotenv

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db import engine

import pandas as pd

# Load environment variables
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

# initialize the embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load data from the database
df_Physicians = pd.read_sql_table('Physicians', engine)
df_Schedules = pd.read_sql_table('Schedules', engine)
df_Specialities = pd.read_sql_table('Specialities', engine)
df_Pricelist = pd.read_sql_table('Pricelist', engine)
df_Policy = pd.read_sql_table('Policy', engine)

# Combine relevant fields into a single text field
df_Physicians['text'] = df_Physicians.apply(lambda row: f"Doctor: {row['Name']}, Speciality: {row['Speciality']}, Degree: {row['Degree']}", axis=1)

df_Schedules['text'] = df_Schedules.apply(lambda row: f"Doctor: {row['Doctor Name']}, Monday: {row['Monday']}, Tuesday: {row['Tuesday']}, Wednesday: {row['Wednesday']}, Thursday: {row['Thursday']}, Friday: {row['Friday']}, Saturday: {row['Saturday']}, Sunday: {row['Sunday']}", axis=1)

df_Specialities['text'] = df_Specialities.apply(lambda row: f"Speciality: {row['Speciality Name']}, Definition: {row['Definition']}", axis=1)

df_Pricelist['text'] = df_Pricelist.apply(lambda row: f"Service: {row['Service Name']}, Price: {row['Price (USD)']}", axis=1)

df_Policy['text'] = df_Policy.apply(lambda row: f"Name: {row['Name']}, Description: {row['Policy Description']}, Address: {row['Address']}, Landline: {row['Landline']}, Open Date: {row['Open Date']}", axis=1)


# Create a FAISS vector store
vector_store = FAISS.from_texts(df_Physicians['text'].tolist(), embeddings)
vector_store.add_texts(df_Schedules['text'].tolist())

vector_store.add_texts(df_Specialities['text'].tolist())

vector_store.add_texts(df_Pricelist['text'].tolist())

vector_store.add_texts(df_Policy['text'].tolist())

vector_store.save_local("hospital_vector_store")