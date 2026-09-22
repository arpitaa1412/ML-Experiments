# 📊 Placement Prediction using Machine Learning

A beginner-friendly **Machine Learning project** that uses **Logistic Regression for Binary Classification** to predict whether a student will be placed or not based on the given input.

## 📌 Project Overview

Placement prediction is a **classification problem** in Machine Learning where the model predicts the placement outcome of a student based on placement-related information.

In this project, a classification model is trained using placement data and saved as a `.pkl` file. A simple web application is created using **Flask** to make predictions using the trained model.

## 🎯 Objective

The main objectives of this project are:

* Understand the concept of Binary Classification
* Load and work with a placement dataset using Python
* Train a Machine Learning classification model
* Save the trained model using Pickle
* Create a simple Flask web application
* Make placement predictions through a web interface

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Flask**
* **Pickle**
* **HTML/CSS**

## 📂 Project Structure

```text
Exp4/
│
├── templates/
│   ├── .gitkeep
│   └── index.html
│
├── Placement_Y_N.csv
├── BCModel.pkl
├── app.py
└── README.md
```

### 📄 File Description

| File                | Description                               |
| ---------------     | ----------------------------------------- |
| `Placement_Y_N.csv` | Dataset used for training/testing         |
| `BCModel.pkl`       | Saved trained Binary Classification model |
| `app.py`            | Flask application for placement prediction|
| `templates/`        | Contains HTML files for the web interface |
| `README.md`         | Project documentation                     |


### 🔄 How the Project Works
```text

Placement Dataset
       ↓
Data Preprocessing
       ↓
Train Classification Model
       ↓
Save Model
       ↓
Load Model in Flask
       ↓
User Enters Input
       ↓
Model Makes Prediction
       ↓
Placement Result Displayed
```

📈 Binary Classification

Binary Classification is a supervised machine learning technique used when the output has two possible classes.

In this project, the model predicts the placement outcome:

Yes → Student is Placed

No  → Student is Not Placed

The model learns the relationship between the input features and the placement outcome from the training data.


💡 Key Learning Outcomes

Through this project, I learned:

Basics of supervised learning

Binary Classification

Working with placement datasets

Training a Machine Learning classification model

Making predictions using Scikit-learn

Saving and loading ML models using Pickle

Connecting a Machine Learning model with Flask
