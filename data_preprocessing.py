import pandas as pd
import numpy as np
from work_with_db import work_with_db
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import torch

class preprocessing():
    def __init__(self):
        self.db = work_with_db()
        self.pca = PCA()
        self.data = pd.DataFrame(
        self.db.action_with_db(action='SELECT', columns=['id', 'Sex', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Calories']),
        columns=['id', 'Sex', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Calories']
    )

        
    def train_test_data(self):
        train_mask = self.data['Calories'].notna()
        self.train_data = self.data.loc[train_mask].drop(columns=['id', 'Calories'])
        self.train_target = self.data.loc[train_mask, 'Calories']
        self.test_data = self.data.loc[~train_mask].drop(columns=['id', 'Calories'])
        
    def col_trans(self):
        pass
    
    def to_tensor(self):
        pass
    
    def process(self):
        self.train_test_data()
        self.col_trans()
        return self.to_tensor()
        