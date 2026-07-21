import joblib
import pandas as pd
from pathlib import Path


class UAVIntrusionDetector:
    """
    AI-Based UAV Intrusion Detection System
    """

    def __init__(self):

        base_dir = Path(__file__).resolve().parent.parent

        self.model = joblib.load(base_dir / "models" / "xgboost_final.pkl")
        

        self.label_map = {
            0: "Benign",
            1: "DoS Attack",
            2: "Replay",
            3: "Evil Twin",
            4: "False Data Injection"
        }

        # Features expected by the trained model
        self.features = list(self.model.feature_names_in_)

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:

        # Check for missing features
        missing = [col for col in self.features if col not in df.columns]

        if missing:
            raise ValueError(
                f"Uploaded CSV is missing required columns:\n{missing}"
            )

        # Arrange columns exactly as during training
        df = df[self.features]

        return df

    def predict(self, df: pd.DataFrame):

        processed = self.preprocess(df)

        predictions = self.model.predict(processed)
        probabilities = self.model.predict_proba(processed)

        labels = [
            self.label_map.get(int(pred), f"Class {pred}")
            for pred in predictions
        ]

        confidence = probabilities.max(axis=1)

        result = df.copy()

        result["Prediction"] = labels
        result["Confidence"] = confidence.round(4)

        summary = result["Prediction"].value_counts().to_dict()

        return result, summary