from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
# Ensure the model file exists before trying to load it
MODEL_PATH = 'car_price_model.pkl'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if model exists
        if not os.path.exists(MODEL_PATH):
            return jsonify({'error': 'Prediction model not found. Please train the model first.'}), 500

        model = joblib.load(MODEL_PATH)
        
        # Get data from the form
        data = {
            'Make': [request.form['Make']],
            'Model': [request.form['Model']],
            'Year': [int(request.form['Year'])],
            'Engine Size': [float(request.form['Engine_Size'])],
            'Mileage': [int(request.form['Mileage'])],
            'Fuel Type': [request.form['Fuel_Type']],
            'Transmission': [request.form['Transmission']],
            'Owner': [request.form['Owner']],
            'Location': [request.form['Location']]
        }
        
        # Create a DataFrame
        df_input = pd.DataFrame(data)
        
        # Make prediction (Model outputs log-price)
        prediction_log = model.predict(df_input)
        price_val = np.expm1(prediction_log[0])
        
        # Create a Range (Honest Valuation) - 7% margin for condition variations
        low_price = price_val * 0.93
        high_price = price_val * 1.07
        
        # Format the result as a range
        prediction_text = f"Valuation Range: ₹{low_price:,.0f} - ₹{high_price:,.0f}"
        
        # Image logic
        car_make = request.form['Make']
        car_model = request.form['Model']
        safe_make = car_make.replace(' ', '_')
        safe_model = car_model.replace(' ', '_')
        car_image = f"{safe_make}_{safe_model}.png"
        
        if not os.path.exists(os.path.join(app.static_folder, car_image)):
            car_image = f"{safe_make}.png"

        return render_template('index.html', prediction_text=prediction_text, car_image=car_image)
        
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
