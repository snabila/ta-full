from googlesearch import search
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import requests

async def get_result(query):
    urls = search('site:halodoc.com/kesehatan ' + query, stop=1)
    source = []

    for url in urls:
        source.append(url)

    # r = requests.get(source[0])

    asession = AsyncHTMLSession()
    r = await asession.get(source[0])
    await r.html.arender()

    soup = BeautifulSoup(r.content, "html.parser")

    contentWrapper = soup.find_all("div", class_="article__content")[0]

    contentFound = {}

    contentFound["source"] = {
        "url" : source[0]
    }

    for header in contentWrapper:
        if header.text.lower() in query:
            # contentFound["content"] = {
            #     header.name : {
            #         "text" : header.text,
            #     },
            # }
            contentFound[header.name] = {
                "content" : header.text
            }

            for sibling in header.next_siblings:
                if sibling.name and sibling.name.startswith('h'):
                    break
                elif sibling.name == "ul":
                    contentFound[sibling.name] = {
                        "content" : sibling.text,
                    }
                    # contentFound["content"] = {
                    #     sibling.name : {
                    #         "text" : sibling.text,
                    #     },
                    # }
                    # contentFound += sibling.text
                    break
                else:
                    contentFound[sibling.name] = {
                        "content" : sibling.text,
                    }
                    # contentFound["content"] = {
                    #     sibling.name : {
                    #         "text" : sibling.text,
                    #     },
                    # }
                    # contentFound += sibling.text


    return contentFound

# print(get_result('gejala diabetes'))