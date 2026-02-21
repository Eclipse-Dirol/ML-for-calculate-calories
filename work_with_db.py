import sqlite3 as sql
import pandas as pd
import os

class work_with_db():
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), 'data', 'database.db')
        self.conn = sql.connect(db_path)
        self.cursor = self.conn.cursor()
        
    def db_entry_from_df(self, df: pd.DataFrame):
        df.to_sql('data', con=self.conn, if_exists='append', index=False)
        
    def action_with_db(self, action, columns):
        placeholder = ', '.join(columns)
        data = self.cursor.execute(f'{action} {placeholder} FROM data').fetchall()
        self.conn.commit()
        self.conn.close()
        return data