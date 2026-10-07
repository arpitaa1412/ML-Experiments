from flask import Flask, render_template, request
import pickle
import joblib

app = Flask(__name__)

# Load the trained CountVectorizer and Multinomial Naive Bayes model
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("naive_bayes_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    message = ""
    probabilities = None

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            # Use the SAME vectorizer used during training
            message_vector = vectorizer.transform([message])

            # Predict one of the three classes
            prediction = model.predict(message_vector)[0]

            # Get probability for each class
            probs = model.predict_proba(message_vector)[0]
            probabilities = sorted(
                zip(model.classes_, probs),
                key=lambda x: x[1],
                reverse=True
            )

    return render_template(
        "index.html",
        prediction=prediction,
        message=message,
        probabilities=probabilities
    )


if __name__ == "__main__":
    app.run(debug=True)
