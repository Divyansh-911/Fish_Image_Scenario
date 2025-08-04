from flask import Flask, request, jsonify
from model import diagnose_fish_disease

app = Flask(__name__)

@app.route('/')
def home():
    return "Fish Disease Detection API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    image_url = data.get('image_url')

    if not image_url:
        return jsonify({'error': 'No image_url provided'}), 400

    result = diagnose_fish_disease(image_url)

    return jsonify({'diagnosis': result}), 200