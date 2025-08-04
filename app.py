from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Replace this with your actual AI logic
def predict_disease(image_url):
    return {"disease": "Ichthyophthirius", "confidence": 0.93, "image_url": image_url}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "image_url" not in data:
        return jsonify({"error": "Missing image_url"}), 400

    result = predict_disease(data["image_url"])
    return jsonify(result)

# Required to bind to the correct port for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses PORT env variable
    app.run(host="0.0.0.0", port=port)
