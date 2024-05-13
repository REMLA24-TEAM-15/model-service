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
    """
    Predict whether a link is a phishing link.
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: link to be evaluated.
          required: True
          schema:
            type: object
            required: link
            properties:
                link:
                    type: string
                    example: https://www.tudelft.nl/en/student/administration/termination-of-enrolment
    responses:
      200:
        description: "The result of the classification: 'phishing' or 'legitimate'."
    """
    char_index = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
    }
    tokenizer = libml.TokenizeQuery(char_index)
    query = request.get_json().get('link')
    processed_query = tokenizer.tokenize(query, 200)
    model = joblib.load('../model/release.joblib')
    prediction = model.predict(processed_query)[0]
    prediction = (np.array(prediction) > 0.5).astype(int).tolist()  # 0 if phishing, 1 if legitimate
    print(prediction)

    res = {
        "Link": query,
        "Prediction": prediction
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
