from flask import Flask, request, jsonify
import joblib
import numpy as np
from encode_prenom import encode_prenom
app = Flask(__name__)

# Load the model when the app starts
reg = joblib.load("model.v1.bin")

@app.route('/predict', methods=['GET'])
def predict():
    name = request.args.get('name')
    if name:
        result = reg.predict([encode_prenom(name)])
        return jsonify({"name": name, "prediction": int(result[0])})
    else:
        return jsonify({"error": "Please provide a name in the query parameters"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
