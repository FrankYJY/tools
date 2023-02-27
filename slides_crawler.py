#!/usr/bin/python3

# crawl 572 slides to pdf
# just put Prof saty's web slide url in url variable

from sys import argv

import img2pdf
import requests
from bs4 import BeautifulSoup

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

url = argv[1]

soup = BeautifulSoup(requests.get(url, headers=HEADER).text, "html.parser")

slides = soup.find_all("div", attrs = {"class" : "slide"})

title = slides[0].table.tr.td.h1.text.strip()

base_url = url[:url.rfind('/')+1]

img_data = [requests.get(base_url + slide.p.img['src']).content for slide in slides[1:]]

with open(title+".pdf", "wb") as f:
    f.write(img2pdf.convert(img_data))
