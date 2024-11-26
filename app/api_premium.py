from flask import Flask, jsonify, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def generate_data(num_records):
    """
    Genera un dataset di pazienti con dettagli sanitari casuali.
    """
    data = []
    diagnoses = ["Healthy", "Diabetes", "Hypertension", "Pre-Diabetes", "Obesity"]
    genders = ["Male", "Female"]
    
    for i in range(1, num_records + 1):
        # Genera pressione sanguigna
        systolic = random.randint(110, 180)
        diastolic = random.randint(70, 120)

        # Categoria di rischio del glucosio
        glucose_level = random.randint(70, 250)
        if glucose_level < 100:
            glucose_category = "Normal"
        elif 100 <= glucose_level < 140:
            glucose_category = "Pre-Diabetic"
        else:
            glucose_category = "Diabetic"

        # Crea un record
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
    """
    Endpoint per ottenere dati sanitari.
    Permette di specificare il numero di record tramite query string.
    """
    try:
        # Numero di record specificato dalla query string (default: 3.000)
        num_records = int(request.args.get('num_records', 3000))
        if num_records > 100000:
            return jsonify({"error": "Request limit exceeded. Max 100,000 records allowed."}), 400
        data = generate_data(num_records)
        return jsonify(data)
    except ValueError:
        return jsonify({"error": "Invalid number of records specified."}), 400

if __name__ == '__main__':
    app.run(debug=True)
