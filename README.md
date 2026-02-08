# Student Performance Prediction

This project is a machine learning web application that predicts a student's
**performance percentage** and **PASS / FAIL status** based on academic data.

---

## Project Overview

The application uses a trained machine learning model to estimate student
performance. The model is loaded from a serialized `.pkl` file and predictions
are served through a Flask web interface.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS
- Joblib

---

## Machine Learning Model

- Algorithm: Linear Regression
- The trained model is stored as `model.pkl`
- The model predicts:
  - Student percentage
  - PASS / FAIL status (based on a threshold)

---

## Project Structure

AI TOOL/
│
├── app.py # Flask application
├── data.py # Data preprocessing logic
├── model.py # Model training script
├── model.pkl # Trained ML model
├── Student.csv # Dataset
├── README.md # Project documentation
│
├── templates/
│ └── index.html # Frontend HTML
│
└── static/
└── style.css # CSS styling

---

## How to Run the Project

### 1. Install required libraries
```bash
pip install flask pandas scikit-learn joblib
python model.py
python app.py
http://127.0.0.1:5000

