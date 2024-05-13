# Flask API to detect phising

import joblib
import numpy as np
from flasgger import Swagger
from flask import Flask, jsonify, request
import libml

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/predict', methods=['POST'])
def predict():

    model = joblib.load('../model/release.joblib')
    tokenizer = libml.TokenizeQuery(model["char_index"])
    query = request.get_json().get('link')
    processed_query = tokenizer.tokenize(query, 200)
    prediction = model.predict(processed_query)[0]
    prediction = (np.array(prediction) > 0.5).astype(int).tolist()  # 0 if phishing, 1 if legitimate
    print(prediction)

    res = {
        "Link": query,
        "Prediction": prediction
    }
    return jsonify(res)

def tokenise():


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
