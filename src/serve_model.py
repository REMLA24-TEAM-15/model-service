# Flask API to detect phising

import joblib
from flask import Flask, jsonify, request
from flasgger import Swagger
import numpy as np

from lib_ml import preprocess_input #to do

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

    link = request.get_json().get('link')
    processed_link = preprocess_input(link)
    model = joblib.load('output/model.joblib')  #change path
    prediction = model.predict(processed_link)
    prediction = (np.array(prediction) > 0.5).astype(int)

    res = {
        "Prediction": "todo",
        "Link": link
    }
    return jsonify(res)


if __name__ == '__main__':
    clf = joblib.load('output/model.joblib')
    app.run(host="0.0.0.0", port=8081, debug=True)
