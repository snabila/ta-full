from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from db.models import (
    Questionare,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()

