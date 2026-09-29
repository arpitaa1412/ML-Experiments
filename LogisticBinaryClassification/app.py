from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("BCModel_Social_Network_Ads.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = float(request.form["age"])
        salary = float(request.form["salary"])

        # Prediction
        prediction = model.predict([[age, salary]])[0]

        # Probability
        probability = model.predict_proba([[age, salary]])[0][1] * 100

        if prediction == 1:
            result = "The customer is likely to purchase the product."
        else:
            result = "The customer is unlikely to purchase the product."

        return render_template(
            "index.html",
            prediction=result,
            probability=round(probability, 2)
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)