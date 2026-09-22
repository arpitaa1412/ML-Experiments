# 📊 Simple Linear Regression

A beginner-friendly **Machine Learning project** that uses **Simple Linear Regression** to predict placement-related outcomes from a given input.

## 📌 Project Overview

Simple Linear Regression is a supervised machine learning algorithm used to model the relationship between **one independent variable** and **one dependent variable**.

In this project, a regression model is trained using placement data and saved as a `.pkl` file. A simple web application is created using **Flask** to make predictions using the trained model.

## 🎯 Objective

The main objectives of this project are:

* Understand the concept of Simple Linear Regression
* Load and work with a dataset using Python
* Train a Linear Regression model
* Save the trained model using Pickle
* Create a simple Flask web application
* Make predictions through a web interface

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
Simple-Linear-Regression/
│
├── templates/
│   └── index.html
│
├── Placement.csv
├── SLRModel.pkl
├── app.py
└── README.md
```

### 📄 File Description

| File            | Description                               |
| --------------- | ----------------------------------------- |
| `Placement.csv` | Dataset used for training/testing         |
| `SLRModel.pkl`  | Saved trained Linear Regression model     |
| `app.py`        | Flask application for prediction          |
| `templates/`    | Contains HTML files for the web interface |
| `README.md`     | Project documentation                     |

## 🔄 How the Project Works

```text
Dataset
   ↓
Data Preprocessing
   ↓
Train Linear Regression Model
   ↓
Save Model
   ↓
Load Model in Flask
   ↓
User Enters Input
   ↓
Model Makes Prediction
   ↓
Prediction Displayed
```

## 📈 Simple Linear Regression

The basic equation of Simple Linear Regression is:

```text
y = mx + c
```

Where:

* `y` = predicted output
* `x` = input feature
* `m` = slope/coefficient
* `c` = intercept

The model learns the relationship between the input and output from the training data.

## 💡 Key Learning Outcomes

Through this project, I learned:

* Basics of supervised learning
* Simple Linear Regression
* Training a machine learning model
* Making predictions using Scikit-learn
* Saving and loading ML models using Pickle
* Connecting a machine learning model with Flask
* Creating a basic ML web application
