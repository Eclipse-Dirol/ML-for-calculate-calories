import sqlite3 as sql
import pandas as pd
import os

class work_with_db():
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'data', 'database.db')
        
    def db_entry_from_df(self, df: pd.DataFrame):
        with sql.connect(self.db_path) as conn:
            df.to_sql('data', con=conn, if_exists='append', index=False)
        
    def action_with_db(self, action, columns):
        with sql.connect(self.db_path) as conn:
            placeholder = ', '.join(columns)
            cursor = conn.cursor()
            data = cursor.execute(f'SELECT {placeholder} FROM data').fetchall()
        return data