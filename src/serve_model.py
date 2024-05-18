# Flask API to detect phising

import numpy as np
from flasgger import Swagger
from flask import Flask, jsonify, request
import libml
from model_class import URL_phishing

app = Flask(__name__)
swagger = Swagger(app)
url_model = URL_phishing()


@app.route('/predict', methods=['POST'])
def predict():
    prediction, query = url_model.predict(request)
    print(prediction)

    res = {
        "Link": query,
        "Prediction": prediction
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
