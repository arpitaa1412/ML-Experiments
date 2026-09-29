from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the Decision Tree model
model = joblib.load("DTModel_tennis.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from HTML form
    outlook = request.form["outlook"]
    temp = request.form["temp"]
    humidity = request.form["humidity"]
    windy = request.form["windy"]

    # Create DataFrame with the same column names used during training
    input_data = pd.DataFrame({
        "outlook": [outlook],
        "temp": [temp],
        "humidity": [humidity],
        "windy": [windy]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == "yes":
        result = "Yes, you can play tennis! 🎾"
    else:
        result = "No, you should not play tennis today."

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)

