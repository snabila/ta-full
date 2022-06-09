from fastapi import FastAPI, HTTPException
from scrape import get_result

app = FastAPI()

# whitelist = [
#     "alodokter",
#     "halodoc",
#     "wikipedia",
# ]

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Google Search Service API"}

@app.get("/{query}", tags=["Search"])
async def search_query(query):
    summary_data = await get_result(query)
    return { "result": summary_data }