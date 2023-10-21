import torch
import torch.nn as nn
import torch.nn.functional as F

# Model hyperparameters
settings = {
    "batch_size": 64,                                          # How many cases are ran in parallel
    "device": 'cuda' if torch.cuda.is_available() else 'cpu',  # Device used
    "epochs": 10000,                                           # Number of training epochs
    "learning_rate": 0.0005,                                   # Learning rate
}

def preprocess(batches):
    """Scale ordinal input features and invert binary features to make 0 'good' and 1 'bad' """
    for batch in batches:
        batch[3] = batch[3] / 60.0 if batch[3] < 60 else 1.0 # Scale BMI to be between 0 and 1, maximum of 60
        batch[7] = 1.0 if batch[6] == 0.0 else 0.0           # Invert physical activity binary (0 becomes yes, 1 becomes no)
        batch[8] = 1.0 if batch[7] == 0.0 else 0.0           # Invert fruit consumption binary (0 becomes yes, 1 becomes no)
        batch[9] = 1.0 if batch[8] == 0.0 else 0.0           # Invert vegetable consumption binary (0 becomes yes, 1 becomes no)
        batch[12] /= 5.0                                     # Scale general health to be between 0 and 1, maximum of 5
        batch[13] /= 30.0                                    # Scale mental health to be between 0 and 1, maximum of 30
        batch[15] /= 13.0                                    # Scale age to be between 0 and 1, maximum of 13 categories
    return batches


class DiabetesPredictorModel(nn.Module):
    def __init__(self):
        """Model definition"""
        super(DiabetesPredictorModel, self).__init__()
        self.fc1 = nn.Linear(16, 64)            # Input layer
        self.batchnorm1 = nn.BatchNorm1d(64)    # Batch normalization layer
        self.dropout1 = nn.Dropout(0.2)         # Dropout layer to prevent overfitting
        self.fc2 = nn.Linear(64, 128)            # Hidden layer
        self.batchnorm2 = nn.BatchNorm1d(128)   # Batch normalization layer
        self.dropout2 = nn.Dropout(0.2)         # Dropout layer to prevent overfitting
        self.fc3 = nn.Linear(128, 1)            # Output layer
        self.sigmoid = nn.Sigmoid()             # Sigmoid activation function

    def forward(self, x):
        """Forward pass"""
        x = preprocess(x) # Preprocess input features
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        x = self.batchnorm1(x)
        x = F.relu(self.fc2(x))
        x = self.dropout2(x)
        x = self.batchnorm2(x)
        x = self.fc3(x)
        x = self.sigmoid(x)
        return x.view(settings["batch_size"]) # Return a vector of length batch size
