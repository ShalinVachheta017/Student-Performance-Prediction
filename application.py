from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import traceback  # Import traceback for debugging

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for home page


@app.route('/')
def index():
    return render_template('index.html')

# Route for prediction


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        else:
            # Print user input for debugging
            print("Received user input:", request.form)

            # Handling missing values with default values
            gender = request.form.get('gender', 'unknown')
            # Default to avoid unknown category issue
            race_ethnicity = request.form.get('race_ethnicity', 'group A')
            parental_level_of_education = request.form.get(
                'parental_level_of_education', "bachelor's degree")
            lunch = request.form.get('lunch', 'standard')
            test_preparation_course = request.form.get(
                'test_preparation_course', 'none')
            reading_score = request.form.get(
                'reading_score', '0')  # Default 0 if missing
            writing_score = request.form.get('writing_score', '0')

            # Convert to float (ensuring valid numerical input)
            reading_score = float(reading_score)
            writing_score = float(writing_score)

            # Creating DataFrame
            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:\n", pred_df)

            # Load Prediction Pipeline
            predict_pipeline = PredictPipeline()
            print("Loaded prediction pipeline")

            # Make Prediction
            results = predict_pipeline.predict(pred_df)
            print("Prediction Result:", results)

            return render_template('home.html', results=results[0])

    except Exception as e:
        print("Error Occurred:", str(e))
        print(traceback.format_exc())  # Print full error traceback
        # Show error details in response
        return f"Internal Server Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Debug mode enabled


'''
For home page : http://127.0.0.1:5000/

and for prediction : http://127.0.0.1:5000/predictdata  

You need to enter the following data in the input fields:

gender: male or female

race_ethnicity: group A, group B, group C, group D

parental_level_of_education: some college, high school, bachelor's degree, master's degree

lunch: standard or free/reduced

test_preparation_course: none or completed

reading_score: 0 to 100

writing_score: 0 to 100

Click on the Predict button to get the prediction result.

'''