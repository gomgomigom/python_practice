from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from dotenv import load_dotenv
from tqdm import tqdm, trange
import pandas as pd
import os
import time

# conn = pymysql.connect(host='localhost', user='root', password='1234', charset='utf8')
# cur = conn.cursor(pymysql.cursors.DictCursor)
# cur.execute("show databases")


load_dotenv()
page = 1
KEY = os.environ.get("KEY")
url = f"https://www.law.go.kr/DRF/lawSearch.do?OC={KEY}&target=prec&type=XML&page={page}&display=100"
response = urlopen(url).read()
xtree = ET.fromstring(response)
totalCnt = int(xtree.find("totalCnt").text)
print(url)
print(xtree[5:])
print(totalCnt)
print("---")
# print(bs(response, "xml"))
text = ""
rows = []
for char in tqdm(range(100), desc="hello world", mininterval=0.01):
    time.sleep(0.01)

for i in trange(int(totalCnt / 100)):
    try:
        items = xtree[5:]
    except:
        print("error xtree null")
        break
    for node in items:
        판례일련번호 = node.find("판례일련번호").text
        사건명 = node.find("사건명").text
        사건번호 = node.find("사건번호").text
        선고일자 = node.find("선고일자").text
        법원명 = node.find("법원명").text
        사건종류명 = node.find("사건종류명").text
        사건종류코드 = node.find("사건종류코드").text
        판결유형 = node.find("판결유형").text
        선고 = node.find("선고").text
        판례상세링크 = node.find("판례상세링크").text
        rows.append(
            {
                "판례일련번호": 판례일련번호,
                "사건명": 사건명,
                "사건번호": 사건번호,
                "선고일자": 선고일자,
                "법원명": 법원명,
                "사건종류명": 사건종류명,
                "사건종류코드": 사건종류코드,
                "판결유형": 판결유형,
                "선고": 선고,
                "판례상세링크": 판례상세링크,
            }
        )
    page += 1
    url = f"https://www.law.go.kr/DRF/lawSearch.do?OC={KEY}&target=prec&type=XML&page={page}&display=100"
    response = urlopen(url).read()
    xtree = ET.fromstring(response)

cases = pd.DataFrame(rows)
cases.to_csv(path_or_buf="./cases.csv", index=False)
print(cases)


test1 = pd.DataFrame(
    [{"바나나": 1000, "콜라": 600}, {"맥주": 200, "사탕": 300}, {"바나나": 500, "콜라": 300}]
)
print(test1)
test1.to_csv(path_or_buf="./test1.csv", index=False)
