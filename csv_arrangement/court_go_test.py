import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("../csv_merge/court.csv")
df = df.drop(["url"], axis=1)
df["seqnum"] = df["seqnum"] + 50000000
df = df.rename(columns={"file_name": "사건번호", "file_body": "판례내용", "법원": "법원명"})
print(df)
df["사건번호"] = df["사건번호"].str.extract(
    r"(\d+[가-힣]{1,3}\d+|\d+[가-힣]{1,3}\d+|\d+[가-힣]{1,3}\d+)"
)

df.head(10).to_csv("./court_go_test.csv", index=False)
