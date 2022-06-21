from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url = "https://www.law.go.kr/DRF/lawSearch.do?OC=nodam89&target=prec&type=XML"
response = urlopen(url).read()
bs(markup="html.parser")
bs(response, parse_only="html.parser")