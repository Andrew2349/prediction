import unittest

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

from app.models.prediction_model import PredictionModel

def get_input_data(path):
    data_frame = pd.read_csv(path)
    X = data_frame[
        ['date', 'day', 'day_sin', 'day_cos', 'month', 'month_sin', 'month_cos', 'hours', 'hours_sin',
         'hours_cos']].values
    y = data_frame['temperature'].values
    return X, y
class PredictionModelTest(unittest.TestCase):
    def setUp(self):
        self.model = PredictionModel('../assets/model.pkl')

    def test_mean_squared_error(self):
        X, y = get_input_data('../assets/Besel.csv')
        y_result = self.model.raw_predict(X)
        error_result = np.sqrt(mean_squared_error(y, y_result))
        print(error_result)
        self.assertLess(error_result, 1)

    def test_mean_squared_error_new(self):
        X, y = get_input_data('../assets/Besel_March.csv')
        y_result = self.model.raw_predict(X)
        error_result = np.sqrt(mean_squared_error(y, y_result))
        print(error_result)
        self.assertLess(error_result, 3)
