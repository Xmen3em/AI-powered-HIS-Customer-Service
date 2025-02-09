from flask import Flask, request, jsonify
import os
import sys
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db import engine
from vectorization.vectorize import embeddings, FAISS
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

@app.route("/add_physician", methods=["POST"])
def add_physician():
    data = request.json
    try:
        with engine.connect() as conn:
            conn.execute(
                f"INSERT INTO physicians (name, speciality, degree) VALUES ('{data['Name']}', '{data['Speciality']}', '{data['Degree']}')"
            )

        text = f"Doctor: {data['Name']}, Speciality: {data['Speciality']}, Degree: {data['Degree']}"
        vector_store = FAISS.load_local("hospital_vector_store", embeddings)
        vector_store.add_texts([text])
        vector_store.save_local("hospital_vector_store")

        return jsonify({"message": "Physician added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_schedule", methods=["POST"])
def add_schedule():
    data = request.json
    try:
        with engine.connect() as conn:
            conn.execute(
                f"INSERT INTO schedules (doctor_name, monday, tuesday, wednesday, thursday, friday, saturday, sunday) "
                f"VALUES ('{data['Doctor_Name']}', '{data['Monday']}', '{data['Tuesday']}', '{data['Wednesday']}', "
                f"'{data['Thursday']}', '{data['Friday']}', '{data['Saturday']}', '{data['Sunday']}')"
            )

        text = f"Doctor: {data['Doctor_Name']}, Monday: {data['Monday']}, Tuesday: {data['Tuesday']}, Wednesday: {data['Wednesday']}, Thursday: {data['Thursday']}, Friday: {data['Friday']}, Saturday: {data['Saturday']}, Sunday: {data['Sunday']}"
        vector_store = FAISS.load_local("hospital_vector_store", embeddings)
        vector_store.add_texts([text])
        vector_store.save_local("hospital_vector_store")

        return jsonify({"message": "Schedule added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_speciality", methods=["POST"])
def add_speciality():
    data = request.json
    try:
        with engine.connect() as conn:
            conn.execute(
                f"INSERT INTO specialities (speciality_name, definition) VALUES ('{data['Speciality_Name']}', '{data['Definition']}')"
            )

        text = f"Speciality: {data['Speciality_Name']}, Definition: {data['Definition']}"
        vector_store = FAISS.load_local("hospital_vector_store", embeddings)
        vector_store.add_texts([text])
        vector_store.save_local("hospital_vector_store")

        return jsonify({"message": "Speciality added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_pricelist", methods=["POST"])
def add_pricelist():
    data = request.json
    try:
        with engine.connect() as conn:
            conn.execute(
                f"INSERT INTO pricelist (service_name, price) VALUES ('{data['Service_Name']}', '{data['Price']}')"
            )

        text = f"Service: {data['Service_Name']}, Price: {data['Price']}"
        vector_store = FAISS.load_local("hospital_vector_store", embeddings)
        vector_store.add_texts([text])
        vector_store.save_local("hospital_vector_store")

        return jsonify({"message": "Pricelist added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_policy", methods=["POST"])
def add_policy():
    data = request.json
    try:
        with engine.connect() as conn:
            conn.execute(
                f"INSERT INTO policy (name, policy_description, address, landline, open_date) VALUES ('{data['Name']}', '{data['Policy_Description']}', '{data['Address']}', '{data['Landline']}', '{data['Open_Date']}')"
            )

        text = f"Name: {data['Name']}, Description: {data['Policy_Description']}, Address: {data['Address']}, Landline: {data['Landline']}, Open Date: {data['Open_Date']}"
        vector_store = FAISS.load_local("hospital_vector_store", embeddings)
        vector_store.add_texts([text])
        vector_store.save_local("hospital_vector_store")

        return jsonify({"message": "Policy added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")

    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        vector_store = FAISS.load_local("hospital_vector_store", embeddings, allow_dangerous_deserialization=True)
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It"),
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
        )
        response = qa_chain.run(query)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
