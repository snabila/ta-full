from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from db import models, schemas
from db.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/diseases/", response_model=List[schemas.Disease])
def read_diseases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    diseases = crud.get_diseases(db, skip=skip, limit=limit)
    return diseases

# get disease by id
@app.get("/diseases/id/{disease_id}", response_model=schemas.Disease)
def read_disease(disease_id: int, db: Session = Depends(get_db)):
    db_disease = crud.get_disease(db, disease_id=disease_id)
    if db_disease is None:
        raise HTTPException(status_code=404, detail="Disease information not found")
    return db_disease

# query disease by name > then return the data
@app.get("/diseases/name/{name}", response_model=schemas.Disease)
def read_disease_name(name: str, db: Session = Depends(get_db)):
    
    db_disease = crud.get_disease_name(db, name=name)
    if db_disease is None:
        raise HTTPException(status_code= 404, detail="404")

    return db_disease
