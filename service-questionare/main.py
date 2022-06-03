from fastapi import FastAPI, HTTPException
from routes.questionares import router as QRouter
from routes.records import router as RRouter

app = FastAPI()

app.include_router(QRouter, tags=["Questionare"], prefix="/questionare")
app.include_router(RRouter, tags=["Records"], prefix="/records")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Questionare Service API"}