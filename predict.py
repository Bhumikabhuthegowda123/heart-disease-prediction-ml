# predict.py - Inference Predictor Engine
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
        """
        feature_vector:
        [age, sex, cp, trestbps, chol, fbs, restecg,
         thalach, exang, oldpeak, slope, ca, thal]
        """
        arr = np.array(feature_vector).reshape(1, -1)
        scaled_arr = self.scaler.transform(arr)

        prediction = self.model.predict(scaled_arr)[0]
        probs = self.model.predict_proba(scaled_arr)[0]

        risk_label = "High Risk" if prediction == 1 else "Low Risk"
        confidence = round(probs[prediction] * 100, 2)

        return risk_label, confidence
