import os
from flask import Flask, jsonify, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Funzione per generare dati (rimane invariata)
def generate_data(num_records):
    data = []
    diagnoses = ["Healthy", "Diabetes", "Hypertension", "Pre-Diabetes", "Obesity"]
    genders = ["Male", "Female"]
    for i in range(1, num_records + 1):
        systolic = random.randint(110, 180)
        diastolic = random.randint(70, 120)
        glucose_level = random.randint(70, 250)
        glucose_category = "Normal" if glucose_level < 100 else "Pre-Diabetic" if glucose_level < 140 else "Diabetic"
        record = {
            "ID": i,
            "Name": f"Patient_{i}",
            "Age": random.randint(18, 80),
            "Gender": random.choice(genders),
            "Diagnosis": random.choice(diagnoses),
            "BloodPressure": f"{systolic}/{diastolic}",
            "Systolic": systolic,
            "Diastolic": diastolic,
            "GlucoseLevel": glucose_level,
            "GlucoseCategory": glucose_category,
            "VisitDate": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        }
        data.append(record)
    return data

@app.route('/medical-data', methods=['GET'])
def medical_data():
    try:
        num_records = int(request.args.get('num_records', 3000))
        if num_records > 100000:
            return jsonify({"error": "Request limit exceeded. Max 100,000 records allowed."}), 400
        data = generate_data(num_records)
        return jsonify(data)
    except ValueError:
        return jsonify({"error": "Invalid number of records specified."}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Porta assegnata dinamicamente da Streamlit Cloud
    app.run(host='0.0.0.0', port=port, debug=True)
