### 🌸 Iris Flower Classification using Logistic Regression

A beginner-friendly Machine Learning project that uses Logistic Regression for Multiclass Classification to predict the species of an Iris flower based on its given features.

### 📌 Project Overview

Iris flower classification is a multiclass classification problem in Machine Learning where the model predicts the species of an Iris flower based on its flower measurements.

In this project, a Logistic Regression model is trained using the Iris dataset. The trained model is saved as a .pkl file, and a simple Flask web application is created to make predictions using the trained model.

### 🎯 Objective

The main objectives of this project are:

Understand the concept of Multiclass Classification

Load and work with the Iris dataset using Python

Train a Logistic Regression classification model

Predict different Iris flower species

Save the trained model using Pickle

Create a simple Flask web application

Make Iris flower predictions through a web interface


### 🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Logistic Regression

Flask

Pickle

HTML/CSS


### 📂 Project Structure
```text
Exp5/
│
├── templates/
│   ├── .gitkeep
│   └── index.html
│
├── MCModel.pkl
├── app.py
└── README.md
```

### 📄 File Description

```text
| File            | Description                               |
| --------------- | ----------------------------------------- |
| `MCModel.pkl`   | Saved trained Logistic Regression model   |
| `app.py`        | Flask application for Iris classification |
| `templates/`    | Contains HTML files for the web interface |
| `README.md`     | Project documentation                     |

```

### 🔄 How the Project Works
```text
Iris Dataset
      ↓
Data Preprocessing
      ↓
Train Logistic Regression Model
      ↓
Save Model
      ↓
Load Model in Flask
      ↓
User Enters Flower Measurements
      ↓
Model Makes Prediction
      ↓
Iris Species Displayed
```

📈 Multiclass Classification

Multiclass Classification is a supervised Machine Learning technique used when the output can belong to more than two classes.

In this project, the model predicts the species of an Iris flower:

Setosa
Versicolor
Virginica

The model learns the relationship between the flower measurements and its species from the training data.

🌱 Input Features

The model uses four features:

Sepal Length

Sepal Width

Petal Length

Petal Width


These features are used by the Logistic Regression model to classify the Iris flower into one of the three species.

🤖 Logistic Regression

Logistic Regression is a supervised Machine Learning algorithm mainly used for classification problems.

Although its name contains "Regression", it is commonly used to predict class labels. For multiclass classification, Logistic Regression can determine which class has the highest predicted probability.
```text
In this project:

Input Features
      ↓
Logistic Regression
      ↓
Class Probabilities
      ↓
Predicted Iris Species
```

### 💡 Key Learning Outcomes

Through this project, I learned:

Basics of supervised learning

Multiclass Classification

Working with the Iris dataset

Logistic Regression

Training a Machine Learning classification model

Making predictions using Scikit-learn

Saving and loading ML models using Pickle

Connecting a Machine Learning model with Flask

Creating a basic ML web application
