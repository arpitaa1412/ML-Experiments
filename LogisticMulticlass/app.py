from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("GlassMCModel.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from HTML form
    RI = float(request.form["RI"])
    Na = float(request.form["Na"])
    Mg = float(request.form["Mg"])
    Al = float(request.form["Al"])
    Si = float(request.form["Si"])
    K = float(request.form["K"])
    Ca = float(request.form["Ca"])
    Ba = float(request.form["Ba"])
    Fe = float(request.form["Fe"])

    # Create input array
    features = np.array([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])

    # Prediction
    prediction = model.predict(features)[0]

    # Glass type names
    glass_types = {
        1: "Building Windows - Float Processed",
        2: "Building Windows - Non-Float Processed",
        3: "Vehicle Windows",
        5: "Containers",
        6: "Tableware",
        7: "Headlamps"
    }

    result = glass_types.get(prediction, "Unknown Glass Type")

    return render_template(
        "index.html",
        prediction=f"Predicted Glass Type: {result}",
        class_number=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)