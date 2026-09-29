from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("multiple_linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])
    bmi = float(request.form["bmi"])
    children = int(request.form["children"])

    sex = request.form["sex"]
    smoker = request.form["smoker"]
    region = request.form["region"]

    # Create input data
    data = {
        "age": age,
        "bmi": bmi,
        "children": children,

        "sex_male": 1 if sex == "male" else 0,

        "smoker_yes": 1 if smoker == "yes" else 0,

        "region_northwest": 1 if region == "northwest" else 0,
        "region_southeast": 1 if region == "southeast" else 0,
        "region_southwest": 1 if region == "southwest" else 0
    }

    # Convert to DataFrame
    input_data = pd.DataFrame([data])

    # Arrange columns in the same order as training
    input_data = input_data[
        [
            "age",
            "bmi",
            "children",
            "sex_male",
            "smoker_yes",
            "region_northwest",
            "region_southeast",
            "region_southwest"
        ]
    ]

    # Predict
    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)