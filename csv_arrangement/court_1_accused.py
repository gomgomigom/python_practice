import pandas as pd
import re
import os
from tqdm import tqdm

tqdm.pandas()
os.chdir(os.path.dirname(__file__))

df = pd.read_csv("../csv_merge/지방_1_수동편집_완완.csv")

with open("./crime_extract.txt", "r") as file:
    regex = file.read()


def remove_accused(text):
    result = text.strip()
    result = re.split(r",|\(|주거", maxsplit=1, string=result)[0]
    result = result.strip()
    return result


def extract_accused(x):
    try:
        accused = re.split(r"피\s*고\s*인", maxsplit=2, string=x["판례내용"])[1]
    except IndexError as err:
        # print(err)
        return "❌ PDF형식 올바르지 않음"
    accused = re.split(r"검 *사", maxsplit=1, string=accused)[0]
    accused = accused.strip()
    # print(accused)
    accused = re.split(r"(?<![3-9])\d+\.", string=accused)[:]
    if len(accused) > 1:
        for index, i in enumerate(accused):
            accused[index] = remove_accused(i)
        accused = accused[1:]
    else:
        accused[0] = accused[0].strip()
    # print(accused)
    # print(len(accused))

    return accused


def extract_guilty(x):
    try:
        guilty = re.split(r"판 *결 *선 *고 *", maxsplit=1, string=x["판례내용"])[1]
        guilty = re.split(r"이 *유.", maxsplit=1, string=guilty)[0]
        return guilty
    except IndexError as err:
        pass


def string2list(x):
    try:
        li = re.split(r",", string=x["사건명"])
        return li
    except Exception as e:
        pass


df["피고인"] = df.progress_apply(extract_accused, axis=1)
df["유무죄"] = df.progress_apply(extract_guilty, axis=1)
df["사건명"] = df.progress_apply(string2list, axis=1)

# df = df[
#     df["사건명"].str.contains(
#         rf"{regex}",
#         na=False,
#     )
# ]

omitted_crime = []


def check_match(x):
    reg = re.compile(rf"{regex}")
    for i in x.사건명:
        if "인정된죄명" in i:
            i = re.split(r"인정된죄명:? ?", string=i)[1]
        elif bool(reg.search(i.strip())) == False:
            omitted_crime.append(i.strip())
            return False
    return True


df["match"] = df.progress_apply(check_match, axis=1)
df = df[df["match"]]
crime_set = set(omitted_crime)
omitted_crime_list = list(crime_set)
print(omitted_crime_list)
print(len(omitted_crime))
print(len(omitted_crime_list))

# df = df[[True if len(i) == 1 else False for i in df["사건명"]]]

df.to_csv(
    "./test.csv",
    index=False,
    columns=["사건명", "사건번호", "피고인", "유무죄", "case", "판례내용"],
)
