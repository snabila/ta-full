import json
from turtle import update
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from db.database import (
    add_q,
    retrieve_q,
    retrieve_qs,
    retrieve_qus,
    update_q,
    delete_q,
    push_participant,
    pull_participant
)

from db.models import (
    Questionare,
    UpdateQuestionare,
    PushParticipant,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()

# Add new questionare
@router.post("", response_description="New questionare added into the database")
async def add_questionare(questionare: Questionare):
    questionare = jsonable_encoder(questionare)
    new_questionare = await add_q(questionare)
    return ResponseModel(new_questionare, "Questionare added successfully.")

# Get all questionares
@router.get("", response_description="Questionares retrieved")
async def get_questionares():
    questionares = await retrieve_qs()
    if questionares:
        return ResponseModel(questionares, "Questionares data retrieved successfully")
    return ResponseModel(questionares, "Empty list returned")

# Get a questionare with a matching code
@router.get("/{code}", response_description="Questionare data retrieved")
async def get_questionare_data(code):
    questionare = await retrieve_q(code)
    if questionare:
        return ResponseModel(questionare, "Questionare data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Questionare doesn't exist.")

# Get the questions from a questionare with a matching code
@router.get("/{code}/questions", response_description="Questions data retrieved")
async def get_questions(code):
    questionare = await retrieve_qus(code)
    if questionare:
        return ResponseModel(questionare, "Questions data retrieved successfully")
    return ErrorResponseModel("An error occured.", 404, "Questionare doesn't exist.")

# Add a new participant into a questionare
@router.put("/{code}/push")
async def add_new_participant(code: str, newParticipant: PushParticipant):
    updated_q = await push_participant(code, newParticipant.username)
    if updated_q:
        return ResponseModel(
            "Participant {} added successfully".format(newParticipant.username),
            "Questionare updated successfully",
        )
    # print(updated_q)
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the questionare data.",
    )

# Pull a participant into a questionare
@router.put("/{code}/pull")
async def del_participant(code: str, newParticipant: PushParticipant):
    updated_q = await pull_participant(code, newParticipant.username)
    if updated_q:
        return ResponseModel(
            "Participant {} removed successfully".format(newParticipant.username),
            "Questionare updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the questionare data.",
    )

# Update an existing questionare
@router.put("/{code}")
async def update_questionare_data(code: str, req: UpdateQuestionare = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_q = await update_q(code, req)
    if updated_q:
        return ResponseModel(
            "Questionare with code: {} update is successful".format(code),
            "Questionare updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the questionare data.",
    )

# Delete an existing questionare
@router.delete("/{code}", response_description="Questionare deleted from the database")
async def delete_questionare(code: str):
    deleted_q = await delete_q(code)
    if deleted_q:
        return ResponseModel(
            "Questionare with code: {} removed".format(code), "Questionare deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Questionare with code {0} doesn't exist".format(code)
    )