from flask import Flask, request
import db

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/sensor_data', methods=['POST'])
def sensor_data():
    data = request.get_json()
    temp = data['temperature'] if 'temperature' in data else None
    hum = data['humidity'] if 'humidity' in data else None
    soil = data['soil moisture'] if 'soil moisture' in data else None
    height = data['height'] if 'height' in data else None
    print(temp, hum, soil, height)
    db.insert(temp, hum, soil, height)
    return 'Data received', 200


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
