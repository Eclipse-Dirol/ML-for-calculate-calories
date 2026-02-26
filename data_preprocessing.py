import os
import pandas as pd
import numpy as np
from work_with_db import work_with_db
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import torch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
device = 'cuda' if torch.cuda.is_available() else 'cpu'

class preprocessing():
    def __init__(self, data):
        self.db = work_with_db()
        self.data = data

    def train(self):
        pass

    def normalization(self):
        pass

    def to_tenser(self):
        pass