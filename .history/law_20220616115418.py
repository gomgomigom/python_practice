import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url = "https://www.law.go.kr/DRF/lawSearch.do?OC=nodam89&target=prec&type=HTML"
response = urlopen(url).read()

print(response)
bs(response)
