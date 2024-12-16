# Post Quality Predictor

This project provides a machine learning-based solution to predict the quality of user posts based on their reputation and interaction metrics. It is built using Python and integrates with Django for a web-based interface.

## Features
- **Model Loading**: Efficiently loads a pre-trained machine learning model and its associated scaler.
- **Prediction**: Uses the user's reputation and interaction metrics to predict post quality.
- **Error Handling**: Gracefully handles invalid inputs and logs errors for debugging.

---

## Library Used
- **Python**: Core programming language.
- **Django**: Web framework for the front-end and API integration.
- **Pandas**: Data manipulation and feature handling.
- **scikit-learn**: Preprocessing and scaling of input data.
- **XGBoost**: Machine learning model used for predictions.
- **joblib**: Model serialization and deserialization.
- **HTML**: Front-end interface for user interaction.

---

## Project Structure
```
.
├── app/
│   ├── views.py          # Django views for web interface
│   ├── ml_model.py       # Predictor class for model interaction
│   └── templates/
│       └── predict.html  # Front-end template for predictions
├── post_quality_model.joblib # Pre-trained model and scaler artifacts
└── README.md             # Project documentation
```

---

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/post-quality-predictor.git
   cd post-quality-predictor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the pre-trained model saved as `post_quality_model.joblib` in the root directory.  
   If you don't have it, train your model and save the artifacts in the required format (see the **Model Training** section).

4. Start the Django server:
   ```bash
   python manage.py runserver
   ```

5. Access the web application in your browser:
   ```
   http://127.0.0.1:8000
   ```

---

## Model Training
To train the model, follow these steps:

1. Prepare your dataset with the following features:
   - `user_reputation`
   - `taker_mpxr_delta`

2. Use XGBoost or another suitable machine learning library to train your model. Example:
   ```python
   from xgboost import XGBClassifier
   import xgboost as xgb
   import logging
   ```

3. Save the trained model and scaler in `post_quality_model.joblib`.

---

## Usage
1. Open the web application.
2. Enter the `reputation` and `interaction` values in the provided form.
3. Submit the form to get the predicted post quality.

---

## Example Prediction
**Input**:
- `user_reputation`: 500
- `taker_mpxr_delta`: 1.5

**Output**:
- `Post Quality`: Good (or numerical prediction, depending on the model).

---

## Error Handling
- Invalid inputs or errors during prediction are captured and displayed as a user-friendly message, such as:  
  `"Invalid input"`.

- Errors are logged for developers to debug effectively.

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add your message here"
   git push origin feature/your-feature
   ```
4. Create a pull request.

---


