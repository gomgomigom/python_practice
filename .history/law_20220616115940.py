import pandas as pd
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from tqdm import trange

url = "https://www.law.go.kr/DRF/lawSearch.do?OC=nodam89&target=prec&type=XML"
response = urlopen(url).read()
xtree = ET.fromstring(response)


print(response)
bs(response)
