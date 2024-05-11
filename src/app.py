from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    uri = request.args.get("URI")
    # move contents of predict.py here to quarry the model
    is_phishing = True
    return jsonify({"is_phishing": is_phishing})


app.run(host="0.0.0.0", port=8081, debug=True)
