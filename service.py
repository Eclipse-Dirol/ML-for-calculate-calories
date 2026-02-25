import random
from fastapi import FastAPI
from pydantic import BaseModel

class ClientData(BaseModel):
    Male: int
    Female: int
    Age: int
    Height: float
    Weight: float
    Duration: float
    
app = FastAPI()

@app.post('/score')
def score(data: ClientData):
    score = 500
    return {'Calories': score}