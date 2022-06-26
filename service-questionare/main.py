import config
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.questionares import router as QRouter
from routes.records import router as RRouter

app = FastAPI()

origins = [
    config.Settings().GATE
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(QRouter, tags=["Questionare"], prefix="/questionare")
app.include_router(RRouter, tags=["Records"], prefix="/records")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Questionare Service API"}