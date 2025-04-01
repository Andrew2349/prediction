import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        line = FigureCanvasTkAgg(figure, self)
        line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    def update_graph(self, data_frame):
        for child in self.winfo_children():
            child.destroy()
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        figure_plot = figure.add_subplot(1, 1, 1)
        line = FigureCanvasTkAgg(figure, self)
        line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        data_frame = data_frame[['Time', 'Temperature']].groupby('Time').sum()
        data_frame.plot(kind='line', legend=True, ax=figure_plot, color='r', marker='o', fontsize=10)
        figure_plot.set_title('Daily Temperature')
