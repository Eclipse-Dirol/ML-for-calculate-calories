import random
from fastapi import FastAPI
from pydantic import BaseModel

class ClientData(BaseModel):
    Sex: list
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float
    
app = FastAPI()

@app.post('/score')
def score(data: ClientData):
    if data.Height > 150 and data.Age > 20:
        score = random.randint(1, 400)
    else:
        score = 500
    return {'Calories': score}