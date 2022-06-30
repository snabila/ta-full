from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class QuestionareFields(BaseModel):
    id : int
    label : str
    question : str
    answer_type : str

class Questionare(BaseModel):
    name : str
    desc : Optional[str] = None
    host : str
    code : str
    notif : bool
    questions : List[QuestionareFields]
    participants : Optional[List[str]] = None

class UpdateQuestionare(BaseModel):
    name : Optional[str]
    desc : Optional[str]
    host : Optional[str]
    code : Optional[str]
    notif : Optional[bool]
    questions : Optional[List[QuestionareFields]]
    participants : Optional[List[str]]

class PushParticipant(BaseModel):
    username : str

class AnswerFields(BaseModel):
    q_id : int
    answer : str

class RecordAnswer(BaseModel):
    user : str
    qs_code : str
    submit_time : datetime
    answers : List[AnswerFields]

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}