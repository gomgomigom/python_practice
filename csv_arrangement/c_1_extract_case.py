import pandas as pd
import re
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv(
    "./court_1_requiredOCR_False.csv",
)
pd.set_option("display.max_rows", 8000)
pd.set_option("display.max_columns", 200)
pd.set_option("display.width", 20000)
print(df.shape)

with open("./crime_extract.txt", "r") as f:
    crime_ext = f.read()
with open("./crime_extract_2.txt", "r") as f:
    crime_ext_2 = f.read()

crime_regex = re.compile(
    r"(\b사 *건\b)?(?(1)|(\b\d+[가-힣]{1,3}\d+\b))(?P<target>.*?)(\n *피 *고 *인\b)?(?(4)|(\b피 *고 *인\b))",
    re.DOTALL,
)

print("--")


def extract_crime_1(x):
    try:
        crime = crime_regex.search(x["판례내용"]).group("target")
    except AttributeError as err:
        print(err)
        return "x"
    return crime


def extract_crime_2(x):
    text = x["사건-피고인"]
    text = re.sub(r"\n", "", text)
    crime = re.findall(rf"{crime_ext}", text)
    crime = list(set(crime))
    return crime


def extract_crime_2_2(x):
    text = x["사건-피고인"]
    text = re.sub(r"\n", "", text)
    crime = re.findall(rf"{crime_ext_2}", text)
    crime = list(set(crime))
    return crime


df["사건-피고인"] = df.apply(extract_crime_1, axis=1)

df["사건명"] = df.apply(extract_crime_2, axis=1)
df["사건명_2"] = df.apply(extract_crime_2_2, axis=1)

print(df.shape)

# df = df[list(map(operator.not_,[True if i != 'x' else False for i in df['사건-피고인']]))]
# df = df[[True if i != 'x' else False for i in df['사건-피고인']]]

df = df[[True if len(i) != 0 else False for i in df["사건명"]]]
print(df.shape)
print(df[["사건명", "사건-피고인"]])
print(df.columns)
df.to_csv(
    "../csv_arrangement/test3.csv",
    index=False,
    columns=[
        "판례정보일련번호",
        "사건명",
        "사건명_2",
        "사건번호",
        "선고일자",
        "법원명",
        "판시사항",
        "판결요지",
        "참조조문",
        "참조판례",
        "판례내용",
        "비고",
        "제목",
        "내용",
        "file_name",
        "RequiredOCR",
        "사건-피고인",
    ],
)
