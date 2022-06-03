from typing import List
from pydantic import BaseModel, conlist

class CovidModel(BaseModel):
    data: List[conlist(float, min_items=8, max_items=8)]