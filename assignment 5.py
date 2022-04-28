import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"
response = requests.get(alba_url)
#------------------------------------------------
soup = BeautifulSoup(response.text, 'html.parser')
find_1 = soup.find("div", {"id": "MainSuperBrand"})
find_2 = find_1.find("ul", {"class": "goodsBox"})
link = []
for i in find_2.find_all("li"):
    link.append(i.find("a")["href"])
#----------슈퍼브랜드 링크---------------------------


def scraper(link):

    s_response = requests.get(link)
    s_soup = BeautifulSoup(s_response.text, 'html.parser')
    s_find_1 = s_soup.find("div", {"id": "NormalInfo"})
    infos = s_find_1.find_all("tr", {"class": ""})

    infomation = {}
    for info in infos:

        local = info.find("td", {"class", "local"})
        if local:
            local = local.text
            print(local)

        title = info.find("span", {"class", "company"})
        if title:
            title = title.text
            print(title)

        data = info.find("td", {"class", "data"})
        if data:
            data = data.text
            print(data)

        pay = info.find("td", {"class", "pay"})
        if pay:
            pay = pay.text
            print(pay)

        last = info.find("td", {"class", "last"})
        if last:
            last = last.text
            print(last)
        infomation = {}


scraper(link[0])
