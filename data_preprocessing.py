import os
import pandas as pd
from work_with_db import work_with_db
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import torch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
device = 'cuda' if torch.cuda.is_available() else 'cpu'

class preprocessing():
    def __init__(self):
        self.db = work_with_db()
        self.data = pd.DataFrame(
        self.db.action_with_db(action='SELECT', columns=['id', 'Sex', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Calories']),
        columns=['id', 'Sex', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Calories']
    )
        
    def train_test_data(self):
        train_mask = self.data['Calories'].notna()
        self.train_data = self.data.loc[train_mask].drop(columns=['id', 'Calories'])
        self.train_target = self.data.loc[train_mask, 'Calories']
        self.test_data = self.data.loc[~train_mask].drop(columns=['id', 'Calories'])
        return self.train_data.shape, self.train_target.shape, self.test_data.shape
        
    def col_trans(self):
        cat_cols = self.train_data.select_dtypes(include=['object', 'category']).columns.tolist()
        num_cols = self.train_data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        self.prep = ColumnTransformer(transformers=[
            ('cat_cols', OneHotEncoder(handle_unknown='ignore'), cat_cols),
            ('num_cols', StandardScaler(), num_cols)
        ])
        self.train_data = self.prep.fit_transform(self.train_data)
        self.test_data = self.prep.transform(self.test_data)
        self.train_target = (self.train_target - self.train_target.mean()) / self.train_target.std()
    
    def to_tensor(self):
        os.makedirs(f'{BASE_DIR}/data/tensor', exist_ok=True)
        X_tr = torch.tensor(self.train_data, dtype=torch.float32, device=device)
        y_tr = torch.tensor(self.train_target, dtype=torch.float32, device=device)
        X_test = torch.tensor(self.test_data, dtype=torch.float32, device=device)
        y_mean = self.train_target.mean()
        y_std = self.train_target.std()
        torch.save(X_tr, f'{BASE_DIR}/data/tensor/X_tr.pt')
        torch.save(y_tr, f'{BASE_DIR}/data/tensor/y_tr.pt')
        torch.save(X_test, f'{BASE_DIR}/data/tensor/X_test.pt')
        torch.save({'mean': float(y_mean), 'std': float(y_std)}, f'{BASE_DIR}/data/tensor/y_stats.pt')
        
    def for_pred(self, data: pd.DataFrame):
        return self.prep.transform(data)
    
    def process(self):
        self.train_test_data()
        self.col_trans()
        self.to_tensor()
        