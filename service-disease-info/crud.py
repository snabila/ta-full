from sqlalchemy.orm import Session
from db import models, schemas


def get_disease(db: Session, disease_id: int):
    return db.query(models.Disease).filter(models.Disease.pk == disease_id).first()


def get_diseases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disease).offset(skip).limit(limit).all()
