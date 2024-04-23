import json
import numpy as np
import os
import pandas as pd
from sklearn.cluster import KMeans

def irrigationmodel(json):
    with open(json) as f:
        data=json.load(f)

    min_soil_moisture=20
    max_soil_moisture=80
    min_air_temp=15
    max_air_temp=25

    min_air_humidity=40
    max_air_humidity=80

    data=pd.DataFrame(data)

    data['Soil_Moisture'].fillna(data['Soil_Moisture'].mean(), inplace=True)
    data['Air_Temperature'].fillna(data['Air_Temperature'].mean(), inplace=True)
    data['Air_Humidity'].fillna(data['Air_Humidity'].mean(), inplace=True)

    X=data[['Soil_Moisture','Air_Temperature','Air_Humidity']].values

    Xnormal=(X-X.mean())/X.std()

    Kmeans.fit(Xnormal)

    flag=False
    
    for point in Xnormal:
        if(min_soil_moisture <=point[0]<=max_soil_moisture) and (min_air_humidity<=point[2]<=max_air_humidity):
            flag=False
        else:
            flag=True

    return flag
