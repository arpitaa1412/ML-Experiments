# 🎾 Play Tennis Prediction using Decision Tree

A beginner-friendly **Machine Learning project** that uses a **Decision Tree Classifier** to predict whether a person should play tennis based on different weather conditions.

## 📌 Project Overview

Weather conditions can affect the decision of whether to play tennis or not.

In this project, a **Decision Tree Classification** algorithm is used to predict whether tennis should be played based on factors such as:

- Outlook
- Temperature
- Humidity
- Windy

The trained model is integrated with a **Flask web application**, allowing users to enter weather conditions and receive a prediction.

## 🎯 Objective

The main objectives of this project are:

- Understand Decision Tree Classification.
- Learn how a Decision Tree makes classification decisions.
- Train a model using the Play Tennis dataset.
- Predict whether to play tennis or not.
- Save the trained model using Pickle.
- Create a Flask web application for prediction.

## 📂 Project Structure

```text
DecisionTree/
│
├── templates/
│   ├── .gitkeep
│   └── index.html
│
├── DTModel_tennis.pkl
├── README.md
├── app.py
└── tennis.csv
