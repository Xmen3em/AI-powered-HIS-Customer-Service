# Hospital Rag System

### A Retrieval-Augmented Generation (RAG) System for hospital management, leveraging FAISS-based vector search and Flask API for efficient data retrieval and querying.

## 🎥 Demo Video

https://github.com/Xmen3em/AI-powered-HIS-Customer-Service/assets/demo.mp4


## 📌 Features

- Database Integration: Stores hospital-related data (physicians, schedules, specialities, pricelist, policies) using SQLite.

- Vectorization & Search: Uses FAISS for efficient similarity search.

- REST API: Flask-based API for querying information.

- User Interface: Streamlit frontend for easy interaction.

## 📂 Project Structure

```
hospital-rag-system/
├── database/
│   ├── db.py  # Handles database setup & data insertion
│   ├── models.py  # Defines database schema
├── api/
│   ├── app.py  # Flask API for querying data
├── vectorization/
│   ├── vectorize.py    Vectorizes data & stores in FAISS
├── ui/
│   ├── app.py   # Streamlit UI for querying the system
├── README.md     # Project Documentation
├── requirements.txt   # Dependencies
```

## 🛠️ Installation
### 1️⃣ Clone the Repository
```
git clone https://github.com/Xmen3em/AI-powered-HIS-Customer-Service.git
cd AI-powered-HIS-Customer-Service
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Set Up the Database
Ensure you have the Xyris HIS_data.xlsx file in the project directory. 
Then run:
```
python database/db.py
```

### 4️⃣ Vectorize the Data
```
python vectorization/vectorize.py
```

### 5️⃣ Run the API Server
```
python api/app.py
```
The API will be accessible at: http://127.0.0.1:5000

### 6️⃣ Run the Streamlit UI
```
streamlit run ui/app.py
```

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| /ask | POST | Queries the RAG system with a user question |
| /add_physician | POST | Adds a new physician to the database |
| /add_schedule | POST | Adds a new schedule entry |
| /add_speciality | POST | Adds a new medical speciality |
| /add_pricelist | POST | Adds a new service price entry |
| /add_policy | POST | Adds a new hospital policy |

## Example Request (Using cURL)
```
curl -X POST "http://127.0.0.1:5000/ask" -H "Content-Type: application/json" -d '{"query": "What is the hospital policy?"}'
```

## 📝 Notes

- Ensure your .env file contains the HF_TOKEN for Hugging Face embeddings and Groq api key for LLM Model

- The database is automatically created from Xyris HIS_data.xlsx.

- FAISS stores the vectorized hospital data for efficient retrieval.


###  Developed by Abdelmoneim Mohamed 🚀