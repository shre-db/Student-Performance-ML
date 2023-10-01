import torch
import torch.nn as nn
import torch.nn.functional as F


# Neural Net Architecture
class StudentNet(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Input Layer wih batch normalization
        self.inp = nn.Linear(58, 64)
        self.bn_inp = nn.BatchNorm1d(64)

        # Hidden Layers with batch normalization
        self.h1 = nn.Linear(64, 64)
        self.bn1 = nn.BatchNorm1d(64)

        self.h2 = nn.Linear(64, 64)
        self.bn2 = nn.BatchNorm1d(64)

        self.h3 = nn.Linear(64, 64)
        self.bn3 = nn.BatchNorm1d(64)

        self.h4 = nn.Linear(64, 64)
        self.bn4 = nn.BatchNorm1d(64)

        # Output Layer
        self.out = nn.Linear(64, 1)

    def forward(self, X):
        X = self.bn_inp(F.gelu(self.inp(X)))
        X = self.bn1(F.gelu(self.h1(X)))
        X = self.bn2(F.gelu(self.h2(X)))
        X = self.bn3(F.gelu(self.h3(X)))
        X = self.bn4(F.gelu(self.h4(X)))
        X = self.out(X)
        return X
    

# Instantiate an untrained model
net = StudentNet()

# Load the trained weights
net.load_state_dict(torch.load('models/model.pt'))

# set the model to eval mode
net.eval()

def predict(data: torch.Tensor):
    yhat = net(data)
    return yhat