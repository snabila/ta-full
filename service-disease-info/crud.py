from sqlalchemy.orm import Session
from sqlalchemy import func
from db import models, schemas
import re

table = models.DiseaseID

# query by id
def get_disease(db: Session, disease_id: int):
    return db.query(table).filter(table.pk == disease_id).first()

# query by name
def get_disease_name(db: Session, name: str):
    # return db.query(table).filter({'disease_name': re.compile('^' + name + '$', re.IGNORECASE)}).first()
    return db.query(table).filter(func.lower(table.disease_name) == name).first()
    # return db.query(table).filter(table.disease_name == name).first()

# return first 100
def get_diseases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(table).offset(skip).limit(limit).all()
