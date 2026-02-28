from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

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
    data = np.array(list(data.model_dump().values()), dtype=float)
    