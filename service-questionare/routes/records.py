from urllib import response
from fastapi import APIRouter, Body, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
import pandas as pd
import csv

from db.database import (
    add_rec,
    del_rec_code_uname,
    get_recs,
    rec_by_code,
    rec_code_uname,
    retrieve_qus
)

from db.models import (
    RecordAnswer,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()

# Add new record
@router.post("", response_description="New record added into the database")
async def add_record(record: RecordAnswer):
    record = jsonable_encoder(record)
    new_record = await add_rec(record)
    return ResponseModel(new_record, "Record added successfully.")

# Get all records
@router.get("", response_description="Records retrieved")
async def get_records():
    records = await get_recs()
    if records:
        return ResponseModel(records, "Records retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "There are no records found")

# Get all records from a monitoring code
@router.get("/code/{code}", response_description="Records retrieved")
async def get_record_code(code):
    records = await rec_by_code(code)
    if records:
        return ResponseModel(records, "Records retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "There are no records for monitoring code {}".format(code))

# Dowload all code records in csv
@router.get("/code/{code}/csv")
async def dl_record_code(code):
    records = await rec_by_code(code)
    questions = await retrieve_qus(code)

    if records:
        flattened_records = []
        for record in records:
            # record_id = record['_id']
            record_user = record['user']
            record_qs = record['qs_code']
            record_time = record['submit_time']

            flattened_record = {
                # '_id': record_id,
                'submit_time': record_time,
                'username': record_user,
                'monitoring_code': record_qs        
            }

            for answer in record['answers']:
                for question in questions:
                    if question['id'] == answer['q_id']:

                        flattened_record[question['label']] = answer['answer']
            
            flattened_records.append(flattened_record)
        
        df = pd.DataFrame(data = flattened_records)

        return Response(content=df.to_csv(), media_type="text/csv")

# Filter by code and username
@router.get("/code/{code}/{uname}", response_description="Records retrieved")
async def get_record_code_uname(code, uname):
    records = await rec_code_uname(code, uname)
    if records:
        return ResponseModel(records, "Records retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "There are no records found")

# Export as csv by code and username
# Dowload all code records in csv
@router.get("/code/{code}/{uname}/csv")
async def dl_record_code_uname(code, uname):
    records = await rec_code_uname(code, uname)
    questions = await retrieve_qus(code)

    if records:
        flattened_records = []
        for record in records:
            # record_id = record['_id']
            record_user = record['user']
            record_qs = record['qs_code']
            record_time = record['submit_time']

            flattened_record = {
                # '_id': record_id,
                'submit_time': record_time,
                'username': record_user,
                'monitoring_code': record_qs        
            }

            for answer in record['answers']:
                for question in questions:
                    if question['id'] == answer['q_id']:
                        flattened_record[question['label']] = answer['answer']
            
            flattened_records.append(flattened_record)
        
        df = pd.DataFrame(data = flattened_records)

        return Response(content=df.to_csv(), media_type="text/csv")

# Delete by code and username
@router.delete("/code/{code}/{uname}", response_description="Records deleted from the database")
async def del_record_code_uname(code, uname):
    deleted_rs = await del_rec_code_uname(code, uname)
    if deleted_rs:
        return ResponseModel(
            "All records removed",
            "Records deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "No records found"
    )

# Get all records from a specific host
# @router.get("/host/{uname}", response_description="Records retrieved")
# async def get_record_host(uname):
