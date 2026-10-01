from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

# Load trained KNN model and scaler
model_data = load("KNNModel.joblib")

model = model_data["model"]
scaler = model_data["scaler"]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    # Get input values from HTML form
    pregnancies = float(request.form['Pregnancies'])
    glucose = float(request.form['Glucose'])
    blood_pressure = float(request.form['BloodPressure'])
    skin_thickness = float(request.form['SkinThickness'])
    insulin = float(request.form['Insulin'])
    bmi = float(request.form['BMI'])
    diabetes_pedigree = float(request.form['DiabetesPedigreeFunction'])
    age = float(request.form['Age'])

    # Create input array
    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]])

    # Scale input using the same scaler used during training
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    # Convert prediction to readable result
    if prediction[0] == 1:
        result = "Diabetic"
    else:
        result = "Not Diabetic"

    return render_template(
        "index.html",
        prediction_text=f"Prediction: {result}"
    )


if __name__ == "__main__":
    app.run(debug=True)