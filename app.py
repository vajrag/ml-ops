from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("linear_regression_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:

        data = request.json
        features = data['features']  # List of features from the request
        prediction = model.predict([features])

        return jsonify({"prediction": prediction.tolist()})
    
    except Exception as e:
        return jsonify({"Error":str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
