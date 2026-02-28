from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from data_preprocessing import preprocessing
from model import work_with_model

prep = preprocessing()
model = work_with_model()

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
    data = pd.DataFrame([data.model_dump()])
    X = prep.another_try(data=data)
    y = model.predict(data=X)
    answer = prep.unnorm_y(y=y)
    return answer