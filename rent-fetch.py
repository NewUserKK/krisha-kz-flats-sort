#!/usr/bin/python

import bs4
import json
import webbrowser
import os
import requests
import re

from dataclasses import dataclass
from typing import List
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

import templates

###### Config ######

# API restricted so views counter request has limit on approx. 4 pages.
# You can request separately in batches, otherwise views counter would not show
# (but flats still will be sorted)
PAGE_START = 1
PAGE_END = 1

REQUEST_URL = "https://krisha.kz/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&das[price][to]=10000&das[rent.period]=1"
####################

@dataclass
class PageScrapResults:
    flats: str
    ids: List[int]


def retry_session(retries, session=None, backoff_factor=0.3):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


VIEWS_URL = "https://krisha.kz/ms/views/krisha/live/{IDS}/"


def getPage(page: int) -> str:
    session = retry_session(3)
    content = session.get(f"{REQUEST_URL}&page={page}", timeout=3000).content
    return str(content, encoding='utf-8')


def scrapFlatsFromPage(soup):
    flats = soup.find(class_="a-list-with-favs")
    flatsAsStrings = map(lambda tag: str(tag), flats.contents)

    return list(filter(lambda s: s != '\n', flatsAsStrings))


def scrapFlatIdsFromPage(soup) -> List[int]:
    jsdataString = soup.find(id="jsdata").string
    jsonString = jsdataString[20:-6]  # trim "var data = {....};"
    parsedJson = json.loads(jsonString)

    return parsedJson["search"]["ids"]


def sortFlatsByViews(flats: PageScrapResults) -> PageScrapResults:
    print(f"Sorting {len(flats.ids)} flats...")
    idList = flats.ids

    viewsData = {}
    batchSize = 35
    for i in range(len(idList) // batchSize + 1):
        batch = idList[batchSize*i : min(batchSize*(i+1), len(idList))]
        idsParam = ",".join(map(str, batch))
        session = retry_session(3)
        content = session.get(VIEWS_URL.format(IDS=idsParam), timeout=3000).content
        viewsData.update(json.loads(content)["data"])

    flatsWithViews = []
    for flat in flats.flats:
        flatId = re.findall('data-id="(\d+)"', flat)
        if not flatId:
            continue
        flatId = flatId[0]
        flatViews = viewsData[flatId]["nb_views"]
        flatsWithViews.append((flat, flatViews))
    
    flatsWithViews.sort(key=lambda x: x[1])

    return PageScrapResults(
        flats=list(map(lambda x: x[0], flatsWithViews)),
        ids=flats.ids
    )


def scrapAllFlats() -> PageScrapResults:
    allFlats = []
    allIds = []

    for i in range(PAGE_START, PAGE_END + 1):
        print(f"Scrapping page {i}")

        page = getPage(i)
        soup = bs4.BeautifulSoup(page, "lxml")

        flats = scrapFlatsFromPage(soup)
        allFlats += flats

        ids = scrapFlatIdsFromPage(soup)
        allIds += ids

    results = PageScrapResults(flats=allFlats, ids=allIds)
    filtered = sortFlatsByViews(results)

    return filtered


def main():
    scrappedFlats = scrapAllFlats()

    with open("index.html", "w") as out:
        flatList = "\n".join(scrappedFlats.flats)

        flatIds = ",".join(map(str, scrappedFlats.ids))
        jsdata = templates.JSDATA.format(FLAT_IDS=flatIds)
        out.write(templates.TEMPLATE.format(FLAT_LIST=flatList, JSDATA=jsdata))

    webbrowser.open(f"file://{os.path.realpath('index.html')}")


main()

