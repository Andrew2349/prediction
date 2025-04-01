import tkinter as tk
from datetime import datetime

from pandas import DataFrame
from tkcalendar import Calendar

from app.ui.graph import Graph
from app.utility import two_digital

class Window(tk.Tk):
    def __init__(self, model):
        super().__init__()
        self.__model = model
        label = tk.Label(self, text="Choose date to predict")
        label.pack()

        self.__calendar = Calendar(self, selectmode='day',
                       year=2020, month=5,
                       day=22)

        self.__calendar.pack(pady=20)
        button = tk.Button(self, text="Predict", command=self.__predict)
        button.pack(pady=20)

        self.__graph = Graph(self)
        self.__graph.pack()

    def __predict(self):
        date = self.__calendar.get_date()
        params = []
        times = []
        for i in range(24):
            time_item = f'{two_digital(i)}:00'
            times.append(time_item)
            item = f'{date} {time_item}'
            param = datetime.strptime(item, '%m/%d/%y %H:%M')
            params.append(param)
        result = self.__model.predict_all(params)
        data_frame = DataFrame(data={'Temperature': result, 'Time': times})
        self.__graph.update_graph(data_frame)