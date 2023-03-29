from bs4 import BeautifulSoup
import requests
import urllib
import csv
import pandas as pd
req = requests.get("put the url")
req_css = requests.get("put the css")
html_content = req.content
css_content = req_css.content
soup = BeautifulSoup(html_content,"html.parser")
html = soup.find("html")
with open("style.css", "w", encoding="utf-8") as arquivo:
    arquivo.write(str(req_css.text))
with open("html.html","w", encoding="utf-8") as arquivo:
    arquivo.write(str(html))
