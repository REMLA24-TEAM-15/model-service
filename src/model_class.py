# Flask API to detect phising

import joblib
import numpy as np
import libml


class URL_phishing:
    """
    URL_phishing class is responsible for loading the trained model and making predictions
    on whether a given URL is phishing or legitimate.
    """
    def __init__(self):
        self.model = None
        self.tokenizer = None

        self.load_model()

    def load_model(self):
        dic = joblib.load('../model/release.joblib')
        self.tokenizer = libml.TokenizeQuery(dic["char_index"])
        self.model = dic['model']

    def predict(self, req):
        query = req.get_json().get('link')
        processed_query = self.tokenizer.tokenize(query, 200)
        prediction = self.model.predict(processed_query)[0]
        prediction = (np.array(prediction) > 0.5)\
            .astype(int).tolist()  # 0 if phishing, 1 if legitimate
        return prediction, query
