from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.environ.get("KEY")
url = f"http://www.law.go.kr/DRF/lawSearch.do?OC={KEY}&target=prec&type=HTML&query=computer"
print(url)
print(url)

response = urlopen(url).read()
bs(response)
