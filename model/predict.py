import torch
from model import DiabetesPredictorModel

def generate_prediction(data):
    """Generate a prediction of diabetes risk based on the 16 factors"""
    data = torch.tensor(data)
    model = DiabetesPredictorModel()
    model.load_state_dict(torch.load("./model2.pt"))
    model.eval()
    with torch.no_grad():
        return model(data)
