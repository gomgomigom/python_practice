# -*- coding: utf-8 -*-
import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

with open("./crime_extract.txt", "r") as file:
    regex = file.read()


df = pd.read_csv("../csv_merge/precedent.csv")
df = df.drop(["선고", "법원종류코드", "사건종류명", "사건종류코드", "판결유형"], axis=1)
print(df)

df = df[df["사건번호"].str.contains(r"고정|고단|고합", na=False)]
df = df[
    df["사건명"].str.contains(
        rf"{regex}",
        na=False,
    )
]
print(df)
df.to_csv("./supreme_test_.csv", index=False)
