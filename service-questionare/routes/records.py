from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from db.database import (
    add_rec
)

from db.models import (
    RecordAnswer,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()

# Add new record
@router.post("/", response_description="New record added into the database")
async def add_record(record: RecordAnswer):
    record = jsonable_encoder(record)
    new_record = await add_rec(record)
    return ResponseModel(new_record, "Record added successfully.")