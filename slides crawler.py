# crawl 572 slides to pdf
# just put Prof saty's web slide url in url variable

import requests 

from bs4 import BeautifulSoup

USER_AGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

url = ""

soup = BeautifulSoup(requests.get(url, headers=USER_AGENT).text, "html.parser")

slides = soup.find_all("div", attrs = {"class" : "slide"})

import re
title = slides[0].table.tr.td.h1.text
title = title.replace("\n","")
title = title.replace("\r","")

base_url = url[:url.rfind('/')+1]

img_data = []
for slide in slides[1:]:
    img_url = slide.p.img['src']
    abs_url = base_url + img_url
    img_data.append(requests.get(abs_url).content)

import img2pdf
with open(title+".pdf", "wb") as f:
    f.write(img2pdf.convert(img_data))