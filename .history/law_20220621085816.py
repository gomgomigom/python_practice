from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.environ.get('KEY')


url = "https://www.law.go.kr/DRF/lawSearch.do?OC=&target=prec&type=XML"
response = urlopen(url).read()
print(bs(response, "xml"))
