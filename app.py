from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the saved model
with open('insurance_model_xgboost.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        age = float(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']

        # Convert categorical variables
        sex_binary = 1 if sex == 'male' else 0
        smoker_binary = 1 if smoker == 'yes' else 0
        
        # Create region dummy variables
        region_northeast = 1 if region == 'northeast' else 0
        region_northwest = 1 if region == 'northwest' else 0
        region_southeast = 1 if region == 'southeast' else 0
        region_southwest = 1 if region == 'southwest' else 0

        # Create feature array
        features = np.array([[
            age, sex_binary, bmi, children, smoker_binary,
            region_northeast, region_northwest, region_southeast, region_southwest
        ]])

        # Make prediction
        log_prediction = model.predict(features)[0]
        prediction = np.expm1(log_prediction)
        
        # Format prediction as currency
        formatted_prediction = f"${prediction:,.2f}"
        
        return jsonify({'prediction': formatted_prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)