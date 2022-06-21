from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from key import KEY

url = f"http://www.law.go.kr/DRF/lawSearch.do?OC={KEY}&target=prec"
print(url)

response = urlopen(url).read()
bs(response)
