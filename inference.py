import joblib
import pandas as pd

class MLInferenceEngine:

    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)
        self.model_features = self.model.feature_names_in_

    def predict(self, input_data: dict):

        # Convert input to DataFrame
        df_input = pd.DataFrame([input_data])

        # One-hot encoding
        df_encoded = pd.get_dummies(df_input)

        # Align with training features
        df_final = df_encoded.reindex(columns=self.model_features, fill_value=0)

        # Prediction (0 or 1)
        prediction = int(self.model.predict(df_final).item())

        # Convert to human readable label
        # With this:
        class_name = (
           "Alert! The patient shows indicators associated with elevated stroke risk. Please consult a physician immediately."
          if prediction == 1 else
         "Great news! Based on the provided information, the patient shows no significant stroke risk."
        )

        # Risk level
        risk_level = "High Risk" if prediction == 1 else "Low Risk"

        return {
            "type": "classification",
            "prediction": prediction,
            "class_name": class_name,
            "risk_level": risk_level
        }


# ================================
# TESTING BLOCK
# ================================
if __name__ == "__main__":

    MODEL_PATH = "random_forest_model.pkl"
    engine = MLInferenceEngine(model_path=MODEL_PATH)

    sample_data = {
        "gender": "Female",
        "age": 54,
        "hypertension": 0,
        "heart_disease": 0,
        "ever_married": "Yes",
        "work_type": "Private",
        "Residence_type": "Urban",
        "avg_glucose_level": 120.5,
        "bmi": 27.3,
        "smoking_status": "never smoked"
    }

    result = engine.predict(sample_data)

    print("\n--- Standalone Inference Test Successful! ---")
    print(f"Result Payload: {result}\n")


# Global engine for FastAPI
engine = MLInferenceEngine("random_forest_model.pkl")