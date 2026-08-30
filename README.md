# 🫀 CardioGuard – Heart Disease Prediction Using Machine Learning

CardioGuard is a machine-learning-based heart disease prediction project developed using Python.

The project is designed to demonstrate how patient clinical parameters can be processed and used with machine-learning algorithms to estimate heart disease risk.

> ⚠️ **Educational Project:** This system is intended for educational and research purposes only. It must not be used as a substitute for professional medical diagnosis or treatment.

---

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. Early identification of potential risk can help support further medical evaluation.

CardioGuard demonstrates a machine-learning workflow in which patient clinical parameters are processed, machine-learning models are trained and evaluated, and the best-performing model can be used for prediction.

The project also includes a graphical user interface, user authentication, SQLite database support, and PDF report generation.

---

## 🎯 Objectives

The main objectives of CardioGuard are:

- To demonstrate heart disease prediction using machine learning.
- To preprocess clinical patient data.
- To compare multiple machine-learning algorithms.
- To select the best-performing model based on test accuracy.
- To provide a simple graphical interface.
- To support user authentication.
- To store application data using SQLite.
- To generate a PDF diagnostic report.

---

## 🤖 Machine Learning Algorithms

The training pipeline includes three machine-learning algorithms:

### 1. Random Forest Classifier

Random Forest combines multiple decision trees to produce a classification result.

### 2. Logistic Regression

Logistic Regression is a classification algorithm commonly used for binary prediction problems.

### 3. Support Vector Machine (SVM)

SVM finds a suitable decision boundary between different classes.

The training pipeline evaluates the models and selects the model with the highest test accuracy.

---

## 🧬 Input Features

The prediction module is designed to use **13 clinical features**:

| No. | Feature |
|---:|---|
| 1 | Age |
| 2 | Sex |
| 3 | Chest Pain Type |
| 4 | Resting Blood Pressure |
| 5 | Cholesterol |
| 6 | Fasting Blood Sugar |
| 7 | Resting ECG |
| 8 | Maximum Heart Rate |
| 9 | Exercise-Induced Angina |
| 10 | Oldpeak |
| 11 | Slope |
| 12 | Number of Major Vessels |
| 13 | Thalassemia |

---

## 🔄 Machine Learning Workflow

```text
Patient Clinical Data
        ↓
Data Preprocessing
        ↓
Train/Test Split
        ↓
Feature Scaling
        ↓
Train Multiple ML Models
        ↓
Evaluate Models
        ↓
Select Best Model
        ↓
Save Model and Scaler
        ↓
Risk Prediction
        ↓
Generate Report
