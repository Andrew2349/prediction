from app.models.prediction_model import PredictionModel
from app.ui.window import Window



def main():
    model = PredictionModel('assets/model.pkl')
    window = Window(model)
    window.title("Weather prediction")
    window.mainloop()

if __name__ == '__main__':
    main()



