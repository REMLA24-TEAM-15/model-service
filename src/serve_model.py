# Flask API to detect phising

import joblib
from flask import Flask, jsonify, request
from flasgger import Swagger
import numpy as np

# from preprocessing import tokenize_single # Should eventually be from lib-ml
from lib_ml import preprocess_input

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
    # print("Processed link: ", processed_link)
    model = joblib.load('output/model.joblib')  # may have to change path in final version
    # prediction = model.predict(processed_link)[0]
    prediction = model.predict(processed_link)
    # print("Length of prediction: ", len(prediction))
    prediction = (np.array(prediction) > 0.5).astype(int)
    # print("Length of link: ", len(link))

    # Test code, remove
    # with open('output/test.txt', 'r') as file:
    #  file_content = file.read()
    # print(file_content)

    res = {
        "Prediction": "TODO",
        "Link": link
    }
    return jsonify(res)


if __name__ == '__main__':
    clf = joblib.load('output/model.joblib')
    app.run(host="0.0.0.0", port=8081, debug=True)
