# -*- coding: utf-8 -*-
import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

with open("./crime_extract.txt", "r") as file:
    regex = file.read()


df = pd.read_csv("./test_court.csv")

df = df[df["file_name"].str.contains(r"고정|고단|고합", na=False)]
df = df[
    df["죄명"].str.contains(
        rf"{regex}",
        na=False,
    )
]
print(df)
df.to_csv("./ttttest_court.csv", index=False)
