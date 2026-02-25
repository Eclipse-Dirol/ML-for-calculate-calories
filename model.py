import os
import torch
import torch.nn as nn
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
    def __init__(self, data):
        self.data = torch.tensor(data, device='cuda')
        input_feat = self.data.shape[1]
        self.model = model_nn(input_feat=input_feat)
        self.model.load_state_dict(torch.load(f'{BASE_DIR}/data/model/model_weight.pt', weights_only=True))
        self.y_stats = torch.load(f'{BASE_DIR}/data/tensor/y_stats.pt')
        
    def predict(self):
        self.model.eval()
        device = next(self.model.parameters()).device
        df = pd.DataFrame(self.data)
        with torch.no_grad():
            pred = self.model(self.data)
            pred_real = pred * self.y_stats['std'] + self.y_stats['mean']
        return pred_real.item()