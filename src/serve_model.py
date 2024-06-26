# Flask API to detect phising

from flasgger import Swagger
from flask import Flask, jsonify, request
from fetch_model import download_latest_joblib
from model_class import URL_phishing
from datetime import datetime

download_latest_joblib("REMLA24-TEAM-15", "model-training", "release.joblib", "../model")

app = Flask(__name__)
swagger = Swagger(app)
url_model = URL_phishing()


@app.route('/predict', methods=['POST'])
def predict():
    prediction, query = url_model.predict(request)
    print(prediction)

    pred_time = datetime.now()
    pred_time = pred_time.strftime("%Y-%m-%d %H:%M:%S")
    model_version = url_model.version

    res = {
        "Link": query,
        "Prediction": prediction,
        "PredictionTime": pred_time,
        "ModelVersion": model_version
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
