import os
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import torch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class preprocessing():
    def __init__(self):
        pass

    def _train(self, data_tr: pd.DataFrame):
        scaler_X = StandardScaler()
        scaler_y = StandardScaler()
        y_tr = data_tr.iloc[:, -1].values.reshape(-1,1)
        X_tr = data_tr.iloc[:, 3:-1].values
        X_tr = scaler_X.fit_transform(X_tr)
        y_tr = scaler_y.fit_transform(y_tr)
        with open(f'{BASE_DIR}/data/scaler/scaler_X.pkl', 'wb') as f:
            pickle.dump(scaler_X, f)
        with open(f'{BASE_DIR}/data/scaler/scaler_y.pkl', 'wb') as f:
            pickle.dump(scaler_y, f)
        return X_tr, y_tr

    def _normalization(self, data: pd.DataFrame):
        with open(f'{BASE_DIR}/data/scaler/scaler_X.pkl', 'rb') as f:
            scaler_X = pickle.load(f)
        le_cols = data.iloc[:, :2].values
        data = data.iloc[:, 2:]
        X_data = scaler_X.transform(data.values)
        X_data = np.hstack([le_cols, X_data])
        return X_data

    def _to_tensor(self, X, y=None, train=False):
        if train:
            X = torch.tensor(X, dtype=torch.float32)
            y = torch.tensor(y, dtype=torch.float32)
            torch.save(X, f'{BASE_DIR}/data/tensor/X_tr.pt')
            torch.save(y, f'{BASE_DIR}/data/tensor/y_tr.pt')
        else:
            X = torch.tensor(X, dtype=torch.float32)
            return X

    def first_try(self, data: pd.DataFrame):
        X_tr, y_tr = self._train(data_tr=data)
        self._to_tensor(X=X_tr, y=y_tr, train=True)

    def another_try(self, data: pd.DataFrame):
        X = self._normalization(data=data)
        return self._to_tensor(X=X)

    def unnorm_y(self, y):
        with open(f'{BASE_DIR}/data/scaler/scaler_y.pkl', 'rb') as f:
            scaler_y = pickle.load(f)
        y = y.cpu().numpy()
        y = scaler_y.inverse_transform(y)
        return float(y[0][0])