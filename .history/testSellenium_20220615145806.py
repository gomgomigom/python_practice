from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from key import key

url = f"https://www.law.go.kr/DRF/lawSearch.do?{key}=test&target=prec&type=XML&query=%EB%8B%B4%EB%B3%B4%EA%B6%8C"
print(url)