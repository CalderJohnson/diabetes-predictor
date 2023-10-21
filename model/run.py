import torch
from train import test_data, get_batch
 
def generate_prediction(data):
    model = torch.load("./model.pt")
    return model(data)
