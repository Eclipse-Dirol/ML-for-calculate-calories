import pandas as pd
import numpy as np
from work_with_db import work_with_db
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class preprocessing():
    def __init__(self):
        self.db = work_with_db()
        self.pca = PCA()
        self.data = pd.DataFrame(self.db.action_with_db(action='SELECT', columns=['id', 'Sex', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']), columns=['id', 'Sex', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])
        self.target = pd.DataFrame(self.db.action_with_db(action='SELECT', columns=['id', 'Calories'], close=True), columns=['id', 'Calories'])
        
    def train_test_data(self):
        train_target = self.target[self.target['Calories'].notna() == True]
        test_target = self.target[self.target['Calories'].notna() == False]
        self.train_data = self.data.merge(train_target, on='id').drop(columns='id')
        self.test_data = self.data.merge(test_target, on='id').drop(columns='id')
        
    def col_trans(self):
        cat_cols = self.train_data.select_dtypes(include=['object', 'category']).columns.tolist()
        num_cols = self.train_data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        