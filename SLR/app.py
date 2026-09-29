from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    tv = float(request.form["tv"])

    prediction = model.predict([[tv]])

    predicted_sales = round(prediction[0], 2)

    return render_template(
        "index.html",
        prediction=predicted_sales,
        tv=tv
    )


if __name__ == "__main__":
    app.run(debug=True)