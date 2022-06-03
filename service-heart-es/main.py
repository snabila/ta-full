from fastapi import FastAPI, HTTPException
from joblib import load
from models.models import CovidModel
# from es.covid import model as covid

covid_clf = load('models/covid_v1.joblib')

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Heart Disease Expert System Service API"}


# # Covid Expert System
# @app.on_event('startup')
# async def load_model():
#     covid_clf = load('models/covid_v1.joblib')

@app.post('/covid', tags=["Predictions"])
async def get_covid_prediction(input: CovidModel):
    data = dict(input)['data']
    prediction = covid_clf.predict(data).tolist()
    log_proba = covid_clf.predict_proba(data).tolist()
    return {"prediction": prediction,
            "log_proba": log_proba}