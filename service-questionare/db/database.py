import config
import motor.motor_asyncio
import pymongo
from bson.objectid import ObjectId

settings = config.Settings()

client = motor.motor_asyncio.AsyncIOMotorClient(settings.DB_URL)

database = client.qs

# monitoring data
qs_collection = database.get_collection("qs_collection")

# record data
rs_collection = database.get_collection("rs_collection")

# Helpers
# # Monitoring helper
def q_helper(q) -> dict:
    return {
        "id": str(q["_id"]),
        "name": q["name"],
        "desc": q["desc"],
        "host" : q["host"],
        "code" : q["code"],
        "notif" : q["notif"],
        "questions" : q["questions"],
        "participants" : q["participants"]
    }

def questions_helper(q) -> dict:
    return {
        "questions" : q["questions"]
    }

# # Record helper
def r_helper(q) -> dict:
    return {
        "id": str(q["_id"]),
        "user": q["user"],
        "qs_code": q["qs_code"],
        "submit_time": q["submit_time"],
        "answers": q["answers"]
    }

####################
### Questionares ###
####################

# Retrieve all questionares present in the database
async def retrieve_qs():
    qs = []
    async for q in qs_collection.find():
        qs.append(q_helper(q))
    return qs

# Add a new questionare into to the database
async def add_q(q_data: dict) -> dict:
    q = await qs_collection.insert_one(q_data)
    new_q = await qs_collection.find_one({"code": q_data["code"]})
    return q_helper(new_q)


# Retrieve a questionare with a matching code
async def retrieve_q(code: str) -> dict:
    q = await qs_collection.find_one({"code": code})
    if q:
        return q_helper(q)

# Get questions from a questionare with a matching code
async def retrieve_qus(code: str) -> dict:
    qus = await qs_collection.find_one({"code": code})
    if qus:
        qus = questions_helper(qus)
        return qus["questions"]


# Update a questionare with a matching code
async def update_q(code: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    q = await qs_collection.find_one({"code": code})
    if q:
        updated_q = await qs_collection.update_one(
            {"code": code}, {"$set": data}
        )
        if updated_q:
            return True
        return False

# Delete a questionare from the database
async def delete_q(code: str):
    q = await qs_collection.find_one({"code": code})
    if q:
        await qs_collection.delete_one({"code": code})
        return True


###############
### Records ###
###############

# Add new record
async def add_rec(answer_data: dict) -> dict:
    rec = await rs_collection.insert_one(answer_data)
    new_req = await rs_collection.find_one(sort=[( '_id', pymongo.DESCENDING )])
    return r_helper(new_req)

# Get all records
async def get_recs():
    rs = []
    async for r in rs_collection.find():
        rs.append(r_helper(r))
    return rs

# Filter records by monitoring code
async def rec_by_code(code: str) -> dict:
    rs = []
    async for r in rs_collection.find({"qs_code": code}):
        rs.append(r_helper(r))
    return rs

# Filter by code and username
async def rec_code_uname(code, uname: str) -> dict:
    rs = []
    async for r in rs_collection.find({"qs_code": code, "user": uname}):
        rs.append(r_helper(r))
    return rs