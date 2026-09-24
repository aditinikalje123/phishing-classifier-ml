## 🛡️ Phishing Website Detection using Machine Learning

The Phishing Classifier is a machine learning-based system that detects whether a website is potentially phishing or safe. It analyzes different characteristics of a website URL and converts them into features for the ML model. The model is trained on labelled data to learn patterns associated with phishing websites. A Flask web application connects the trained model with the user interface for making predictions. The system helps identify suspicious websites and provides an automated classification result.

## 📌 Project Overview

* Developed an **ML-based phishing website detection system**.
* Analyzes **URL features** to identify suspicious websites.
* Uses **supervised machine learning** for Phishing/Safe classification.
* Includes separate **training and prediction pipelines**.
* Integrated the ML model with a **Flask web application**.



## 🎯 Objectives

- Detect potentially phishing websites using Machine Learning.
- Extract useful features from website URLs.
- Train and evaluate a classification model.
- Save the trained model for future predictions.
- Create separate training and prediction pipelines.
- Provide a web interface using Flask.
- Generate predictions through a simple user interface.


## 🏗️ Simple Architecture

                    ┌─────────────────────┐
                    │      Dataset        │
                    │  Labeled URL Data   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Preprocessing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Extraction  │
                    │  URL Characteristics│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Model Training     │
                    │  & Evaluation       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Saved Model      │
                    │     model.pkl       │
                    └──────────┬──────────┘
                               │
                               ▼
        ┌─────────────────────────────────────────┐
        │             Flask Application           │
        └──────────────────────┬──────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   New Input Data    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Prediction Pipeline │
                    │ Feature Processing   │
                    │ + Saved ML Model     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Prediction     │
                    │  Phishing / Safe    │
                    └─────────────────────┘


## 🛠️ Technologies Used

Python
Machine Learning
XGBoost
Flask
Jupyter Notebook
Git & GitHub            


## 📁 Project Structure

Phishing-Classifier-ML/
│
├── data/
│   └── raw_data/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   └── index.html
│
├── static/
│
├── app.py
├── model.pkl
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore

## 🎯 Real World Example

A real-world example of my Phishing Classifier would be a bank using a similar system to analyze URLs received through emails or messages. For example, if an employee receives a message saying, “Your bank account will be blocked, click here to verify,” the system can analyze the URL in the message, extract its features, and use the trained machine-learning model to classify it as Phishing or Safe. If it is identified as phishing, the system can flag the link and warn the employee before they access the website.


## 🎯 Project Highlights

ML-based phishing website detection
Extracts and analyzes URL features
Uses XGBoost for Phishing/Safe classification
Separate training and prediction pipelines
Flask web application for user interaction
Trained model saved for future predictions
Includes data preprocessing and model evaluation


## 📄 License

This project is intended for educational and portfolio purposes.
