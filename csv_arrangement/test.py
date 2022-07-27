import pandas as pd
import re
import os
from tqdm import tqdm

tqdm.pandas()
os.chdir(os.path.dirname(__file__))

df1 = pd.read_csv("../csv_merge/지방_1_수동편집_완완.csv")
df2 = pd.read_csv("../csv_merge/지방_1_수동편집_완.csv")
print(df1.dtypes, df2.dtypes)
print(df1.info(), df2.info())


def test(x):
    li = re.split(r",", string=x.사건명)
    return li


def check_case(x):
    try:
        text = x["판례내용"][2:150]
    except TypeError as err:
        return "ERROR"
    case1 = re.compile(r"지 *방 *법 *원 *판 *결 *사 *건")
    case2 = re.compile(r"지 *방 *법 *원 *.{0,10}?형 *사 *부 *판 *결")
    case3 = re.compile(r"^사 *건 *\d+[가-힣]{1,3}\d+")
    case4 = re.compile(r"지 *방 *법 *원 *.*?지 *원 *판 *결")
    case5 = re.compile(r"^.{0,10}?지 *방 *법 *원")
    case6 = re.compile(r"판결요지서")
    case7 = re.compile(r"보도자료")
    if bool(case1.search(text)):
        return "1"
    elif bool(case2.search(text)):
        return "2"
    elif bool(case3.search(text)):
        return "3"
    elif bool(case4.search(text)):
        return "4"
    elif bool(case5.search(text)):
        return "5"
    elif bool(case6.search(text)):
        return "6"
    elif bool(case7.search(text)):
        return "7"
    else:
        return "e"


df1["case"] = df1.progress_apply(check_case, axis=1)


df1.to_csv(
    "./test.csv",
    index=False,
)
