from pydantic import BaseModel
import pydantic
from typing import Optional


class AllOptional(pydantic.main.ModelMetaclass):
    def __new__(self, name, bases, namespaces, **kwargs):
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Optional[annotations[field]]
        namespaces["__annotations__"] = annotations
        return super().__new__(self, name, bases, namespaces, **kwargs)


class DiseaseBase(BaseModel):
    disease_name: str
    overview: str
    symptoms: str
    when_to_see_doctor: str
    causes: str
    risk_factors: str
    complication: str
    prevention: str


class Disease(DiseaseBase, metaclass=AllOptional):
    pk: int

    class Config:
        orm_mode = True
