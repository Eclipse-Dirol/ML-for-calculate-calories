import os
import torch
import torch.nn as nn
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
device = 'cuda' if torch.cuda.is_available() else 'cpu'

class model_nn(nn.Module):
    def __init__(self, input_feat):
        super().__init__()
        self.layer1 = nn.Linear(input_feat, 256)
        self.layer2 = nn.Linear(256, 128)
        self.layer3 = nn.Linear(128, 64)
        self.layer4 = nn.Linear(64, 1)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        
    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        x = self.layer3(x)
        x = self.relu(x)
        x = self.layer4(x)
        return x
    
class work_with_model():
    def __init__(self):
        self.model = model_nn(input_feat=6).to(device)
        self.model.load_state_dict(torch.load(f'{BASE_DIR}/data/model/model_weight.pt'))

    def predict(self, data):
        data = data.to(device)
        self.model.eval()
        with torch.no_grad():
            return self.model(data)

    def train(self):
        self.model.train()
        pass