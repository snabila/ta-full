from sqlalchemy.orm import Session
from db import models, schemas

# query by id
def get_disease(db: Session, disease_id: int):
    return db.query(models.Disease).filter(models.Disease.pk == disease_id).first()

# query by name
def get_disease_name(db: Session, name: str):
    return db.query(models.Disease).filter(models.Disease.disease_name == name).first()

# return first 100
def get_diseases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disease).offset(skip).limit(limit).all()
