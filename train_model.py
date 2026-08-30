# train_model.py - Scikit-Learn Multi-Algorithm Training Pipeline
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from data_preprocessing import load_and_preprocess_dataset

def train_and_export_models():
    """Train multiple algorithms and export the best model using joblib."""
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess_dataset()
    
    models = {
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "SVM": SVC(probability=True)
    }
    
    best_acc = 0.0
    best_model = None
    best_name = ""
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"{name} Accuracy: {acc*100:.2f}%")
        
        if acc > best_acc:
            best_acc = acc
            best_model = model
            best_name = name
            
    # Save best model & scaler
    joblib.dump(best_model, "models/best_heart_model.joblib")
    joblib.dump(scaler, "models/scaler.joblib")
    print(f"Exported {best_name} to models/best_heart_model.joblib")

if __name__ == "__main__":
    train_and_export_models()
