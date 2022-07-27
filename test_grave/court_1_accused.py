import pandas as pd
import re
import os
from tqdm import tqdm

tqdm.pandas()
os.chdir(os.path.dirname(__file__))

df = pd.read_csv("../csv_merge/지방_1_수동편집_완.csv")


def remove_accused(text):
    result = text.strip()
    result = re.split(r",|\(|주거", maxsplit=1, string=result)[0]
    result = result.strip()
    return result


def extract_accused(x):
    try:
        accused = re.split(r"피\s*고\s*인", maxsplit=2, string=x["판례내용"])[1]
    except IndexError as err:
        print(err)
        accused = re.split(r"피\s*고\s*인", maxsplit=2, string=x["판례내용"])[0]
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
    print(len(accused))

    return accused


def extract_guilty(x):
    try:
        guilty = re.split(r"판 *결 *선 *고 *", maxsplit=1, string=x["판례내용"])[1]
        guilty = re.split(r"이 *유.", maxsplit=1, string=guilty)[0]
        return guilty
    except IndexError as err:
        print(err)


df["피고인"] = df.progress_apply(extract_accused, axis=1)
df["유무죄"] = df.progress_apply(extract_guilty, axis=1)

df = df[[True if len(i) == 1 else False for i in df["피고인"]]]

print(df[["사건명", "피고인"]])
df.to_csv(
    "./test.csv", index=False, columns=["사건명", "사건번호", "피고인", "유무죄", "판례내용"]
)
