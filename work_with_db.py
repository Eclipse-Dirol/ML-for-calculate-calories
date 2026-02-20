import sqlite3 as sql
import pandas as pd

class work_with_db():
    def __init__(self):
        self.conn = sql.connect('data/database.db')
        self.cursor = self.conn.cursor()
    
    def import_from_db(self):
        pass
    
    def db_entry(self):
        pass
    
    def db_entry_from_df(self, df: pd.DataFrame):
        df.to_sql('data', con=self.conn, if_exists='append', index=False)
    
    def update_db(self):
        pass