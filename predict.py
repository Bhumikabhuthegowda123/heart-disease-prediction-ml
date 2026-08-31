# predict.py - Heart Disease Prediction Module

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import joblib


class HeartDiseasePredictor:
    def __init__(
        self,
        model_path="models/best_heart_model.joblib",
        scaler_path="models/scaler.joblib"
    ):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def predict_risk(self, feature_vector):
        """Predict heart disease risk using 13 input features."""

        arr = np.array(feature_vector, dtype=float).reshape(1, -1)

        if arr.shape[1] != 13:
            raise ValueError("Exactly 13 features are required.")

        scaled_arr = self.scaler.transform(arr)

        prediction = self.model.predict(scaled_arr)[0]

        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(scaled_arr)[0]
            confidence = float(max(probabilities) * 100)
        else:
            confidence = 100.0

        risk_label = "High Risk" if int(prediction) == 1 else "Low Risk"

        return risk_label, round(confidence, 2)


class PredictorModule(ttk.Frame):
    """GUI module used by dashboard.py."""

    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(
            self,
            text="Heart Disease Predictor",
            font=("Helvetica", 16, "bold")
        )
        title.pack(pady=20)

        ttk.Label(
            self,
            text="Enter the 13 patient features to perform prediction."
        ).pack(pady=5)

        self.feature_entries = []

        feature_names = [
            "Age",
            "Sex",
            "Chest Pain Type",
            "Resting Blood Pressure",
            "Cholesterol",
            "Fasting Blood Sugar",
            "Resting ECG",
            "Maximum Heart Rate",
            "Exercise Induced Angina",
            "Oldpeak",
            "Slope",
            "Number of Major Vessels",
            "Thalassemia"
        ]

        form = ttk.Frame(self)
        form.pack(pady=10)

        for i, name in enumerate(feature_names):
            ttk.Label(
                form,
                text=name + ":"
            ).grid(
                row=i,
                column=0,
                padx=10,
                pady=4,
                sticky="w"
            )

            entry = ttk.Entry(form, width=20)
            entry.grid(
                row=i,
                column=1,
                padx=10,
                pady=4
            )

            self.feature_entries.append(entry)

        ttk.Button(
            self,
            text="Predict Risk",
            command=self.run_prediction
        ).pack(pady=15)

        self.result_label = ttk.Label(
            self,
            text="",
            font=("Helvetica", 14, "bold")
        )
        self.result_label.pack(pady=10)

    def run_prediction(self):
        try:
            values = [
                float(entry.get())
                for entry in self.feature_entries
            ]

            if len(values) != 13:
                raise ValueError("Exactly 13 features are required.")

            predictor = HeartDiseasePredictor()

            risk, confidence = predictor.predict_risk(values)

            self.result_label.config(
                text=f"Result: {risk} | Confidence: {confidence}%"
            )

        except Exception as e:
            messagebox.showerror(
                "Prediction Error",
                f"Unable to make prediction.\n\n{e}"
            )
