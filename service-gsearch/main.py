from fastapi import FastAPI
from googlesearch import search
from bs4 import BeautifulSoup
import requests

app = FastAPI()

whitelist = [
    "alodokter",
    "halodoc",
    "wikipedia",
]

result = ''

def search_header(header_type, data, query):
    for header in data.find_all(header_type):
        if header.text.lower() in query:
            print(header.text)
            for sibling in header.next_siblings:
                if sibling.name and sibling.name.startswith('h'):
                    break
                elif sibling.name == "ul":
                    result = result + sibling.text
                    break
                else:
                    result = result + sibling.text

def source_alodokter(source, query):
    page = requests.get(source)
    page_parsed = BeautifulSoup(page.content, "html.parser")

    article_content = page_parsed.find_all("div", class_="post-content")
    article_content = article_content[0]

    search_header("h3", article_content, query)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Google Search Service API"}

@app.post("/{query}", tags=["Search"])
def search_query(query: str):
    filterQuery = 'site:alodokter.com ' + query
    url = search(filterQuery, stop=1)
    source_alodokter(url, filterQuery)
    return result
