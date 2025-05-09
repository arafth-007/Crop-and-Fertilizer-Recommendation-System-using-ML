#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load fertilizer recommendation model and preprocessing
fertilizer_model = pickle.load(open('fertilizer_model.pkl', 'rb'))
fertilizer_scaler = pickle.load(open('fertilizer_scaler.pkl', 'rb'))
soil_encoder = pickle.load(open('soil_encoder.pkl', 'rb'))
crop_encoder = pickle.load(open('crop_encoder.pkl', 'rb'))

# Load crop recommendation model and preprocessing
crop_model = pickle.load(open('crop_model.pkl', 'rb'))
crop_scaler = pickle.load(open('crop_scaler.pkl', 'rb'))

# Manual crop dictionary mapping
crop_dict = {
    0: 'rice', 1: 'maize', 2: 'chickpea', 3: 'kidneybeans',
    4: 'pigeonpeas', 5: 'mothbeans', 6: 'mungbean', 7: 'blackgram',
    8: 'lentil', 9: 'pomegranate', 10: 'banana', 11: 'mango',
    12: 'grapes', 13: 'watermelon', 14: 'muskmelon', 15: 'apple',
    16: 'orange', 17: 'papaya', 18: 'coconut', 19: 'cotton',
    20: 'jute', 21: 'coffee'
}

@app.route('/')
def home():
    soil_types = ['Sandy', 'Loamy', 'Black', 'Red', 'Clayey']
    crop_types = ['Barley', 'Cotton', 'Ground Nuts', 'Maize', 'Millets', 
                 'Oil seeds', 'Paddy', 'Pulses', 'Sugarcane', 'Tobacco', 'Wheat']
    return render_template('index.html', 
                         soil_types=soil_types,
                         crop_types=crop_types)

@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    try:
        features = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]
        
        scaled_features = crop_scaler.transform([features])
        prediction = crop_model.predict(scaled_features)
        crop_name = crop_dict.get(int(prediction[0]), 'Unknown Crop')
        
        return jsonify({
            'success': True,
            'prediction': crop_name
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

fertilizer_dict = {
    1: 'Urea',
    2: 'DAP',
    3: '14-35-14',
    4: '28-28',
    5: '17-17-17',
    6: '20-20',
    7: '10-26-26',
}

@app.route('/predict_fertilizer', methods=['POST'])
def predict_fertilizer():
    try:
        features = [
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['moisture']),
            soil_encoder.transform([request.form['soil_type']])[0],
            crop_encoder.transform([request.form['crop_type']])[0],
            float(request.form['nitrogen']),
            float(request.form['potassium']),
            float(request.form['phosphorous'])
        ]

        scaled_features = fertilizer_scaler.transform([features])
        prediction = fertilizer_model.predict(scaled_features)

        # Convert index to fertilizer name
        fertilizer_index = int(prediction[0])  # Convert NumPy int64 to Python int
        fertilizer_name = fertilizer_dict.get(fertilizer_index, "Unknown Fertilizer")

        return jsonify({
            'success': True,
            'prediction': fertilizer_name
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True, use_reloader=False)


# In[ ]:




