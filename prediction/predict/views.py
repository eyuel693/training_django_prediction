from django.shortcuts import render
from .ml_model import PostQualityPredictor

# Create your views here.

def predict_post_quality(request):
    prediction = None
    if request.method == 'POST':
        try:
            # Retrieve reputation and interaction values from the POST request
            reputation = float(request.POST.get('reputation'))
            interaction = float(request.POST.get('interaction'))
            
            # Initialize the predictor and make the prediction
            predictor = PostQualityPredictor()
            prediction = predictor.predict(reputation, interaction)
        except (ValueError, TypeError) as e:
            # Handle errors if the input is invalid
            prediction = "Invalid input"
            # Optionally print the error for debugging
            print(e)

    # Render the result in the 'predict.html' template
    return render(request, 'predict.html', {'prediction': prediction})
