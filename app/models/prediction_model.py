from datetime import datetime

import joblib

from app import formater


class PredictionModel:
    def __init__(self, model_path):
        self.__model = joblib.load(model_path)

    def predict(self, date:datetime):
        data = formater.format_date(date)
        result = self.__model.predict(data)
        return result[0]
    def predict_all(self,dates):
        data = []
        for date in dates:
            data+= formater.format_date(date)
        result = self.__model.predict(data)
        return result
    def raw_predict(self,data):
        return self.__model.predict(data)