from unittest import case
import pandas as pd
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from tqdm import trange
import time
import re
import os

case_list = pd.read_csv("./cases.csv")
part_standard = 5000
start = 20000 + 55000 + 5000
rows = []

for i in trange(len(case_list) - start):
    url = "https://www.law.go.kr"
    link = (
        case_list.loc[i + start]
        .replace("HTML", "XML")["판례상세링크"]
        .replace("HTML", "XML")
    )
    url += link
    response = urlopen(url).read()
    xtree = ET.fromstring(response)
    판례정보일련번호 = xtree.findtext("판례정보일련번호")
    사건명 = xtree.findtext("사건명")
    사건번호 = xtree.findtext("사건번호")
    선고일자 = xtree.findtext("선고일자")
    선고 = xtree.findtext("선고")
    법원명 = xtree.findtext("법원명")
    법원종류코드 = xtree.findtext("법원종류코드")
    사건종류명 = xtree.findtext("사건종류명")
    사건종류코드 = xtree.findtext("사건종류코드")
    판결유형 = xtree.findtext("판결유형")
    판시사항 = xtree.findtext("판시사항")
    판결요지 = xtree.findtext("판결요지")
    참조조문 = xtree.findtext("참조조문")
    참조판례 = xtree.findtext("참조판례")
    판례내용 = xtree.findtext("판례내용")
    rows.append(
        {
            "판례정보일련번호": 판례정보일련번호,
            "사건명": 사건명,
            "사건번호": 사건번호,
            "선고일자": 선고일자,
            "선고": 선고,
            "법원명": 법원명,
            "법원종류코드": 법원종류코드,
            "사건종류명": 사건종류명,
            "사건종류코드": 사건종류코드,
            "판결유형": 판결유형,
            "판시사항": 판시사항,
            "판결요지": 판결요지,
            "참조조문": 참조조문,
            "참조판례": 참조판례,
            "판례내용": 판례내용,
        }
    )

    if (i + 1) % part_standard == 0:
        partNumber = (i + start) // part_standard
        part = pd.DataFrame(rows)
        part.to_csv(path_or_buf=f"./part{partNumber}.csv", index=False)
        rows = []
cases = pd.DataFrame(rows)
cases.to_csv(path_or_buf="./part_last.csv", index=False)
print(cases)
