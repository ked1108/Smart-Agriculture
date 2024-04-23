# import pandas as pd
# import joblib

# # Load the model and the label encoder from the pickle files
# rf = joblib.load('random_forest_model.pkl')
# le = joblib.load('label_encoder.pkl')

# # Load the preprocessed data from the pickle file
# average_rainfall = joblib.load('average_rainfall.pkl')

# # Get user input
# state = input("Enter the state: ")
# month = input("Enter the month: ")

# n = 90
# p = 42
# k = 43
# temperature = 20.8797
# humidity = 82.0027
# ph = 6.503

# # Get the average rainfall from the precalculated values
# rainfall = average_rainfall[state][month]

# # Prepare the input data
# X_new = pd.DataFrame([[n, p, k, temperature, humidity, ph, rainfall]], columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

# # Use the Random Forest model to make a prediction
# prediction = rf.predict(X_new)

# # Return the predicted crop
# crop = le.inverse_transform(prediction)[0]
# print("The recommended crop is:", crop)

import json
import joblib
import pandas as pd


def recommendation(json, state, month):
    with open(json) as f:
        data=json.load(f)

    rf=joblib.load('random_forest_model.pkl')
    le=joblib.load('label_encoder.pkl')

    average_rainfall = joblib.load('average_rainfall.pkl')

    n = 90
    p = 42
    k = 43

    temperature=data['temperature']
    humidity=data['humidity']
    ph = 6.503
    
    rainfall = average_rainfall[state][month]

    X_new = pd.DataFrame([[n, p, k, temperature, humidity, ph, rainfall]], columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    prediction = rf.predict(X_new)

    crop = le.inverse_transform(prediction)[0]

    return crop