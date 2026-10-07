from flask import Flask, render_template, request
import pickle

import joblib

app = Flask(__name__)

vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("naive_bayes_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    message = ""

    if request.method == "POST":

        message = request.form["message"]

        # Convert message into Bag-of-Words
        message_vector = vectorizer.transform([message])

        # Predict class
        prediction = model.predict(message_vector)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)