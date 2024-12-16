import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

class PostQualityPredictor:
    def __init__(self, model_path='post_quality_model.joblib'):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = ['user_reputation', 'taker_mpxr_delta']
        self.model_path = model_path
        self.load_model(model_path)

    def load_model(self, path):
        """Load saved model and scaler once"""
        try:
            model_artifacts = joblib.load(path)
            self.model = model_artifacts['model']
            self.scaler = model_artifacts['scaler']
            self.feature_names = model_artifacts['feature_names']
            logging.info("Model loaded successfully")
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")
            self.model = None  

    def predict(self, user_reputation, taker_mpxr_delta):
        """Make predictions for new data"""
        if self.model is None:
            logging.error("Model not trained or loaded.")
            return None

        input_features = pd.DataFrame({
            'user_reputation': [user_reputation],
            'taker_mpxr_delta': [taker_mpxr_delta]
        })

        
        try:
            scaled_features = self.scaler.transform(input_features)
            prediction = self.model.predict(scaled_features)[0]
            logging.info(f"Prediction made: {prediction}")
            return prediction
        except Exception as e:
            logging.error(f"Error during prediction: {str(e)}")
            return None
