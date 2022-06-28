from sqlalchemy import Column, Integer, Text
from .db import Base


class Disease(Base):
    __tablename__ = "disease_info"

    pk = Column(Integer, primary_key=True)
    disease_name = Column(Text)
    overview = Column(Text)
    symptoms = Column(Text)
    when_to_see_doctor = Column(Text)
    causes = Column(Text)
    risk_factors = Column(Text)
    complication = Column(Text)
    prevention = Column(Text)

class DiseaseID(Base):
    __tablename__ = "disease_info_id"

    pk = Column(Integer, primary_key=True)
    disease_name = Column(Text)
    overview = Column(Text)
    symptoms = Column(Text)
    when_to_see_doctor = Column(Text)
    causes = Column(Text)
    risk_factors = Column(Text)
    complication = Column(Text)
    prevention = Column(Text)