import pandas as pd
import re
import os

os.chdir(os.path.dirname(__file__))

with open("./crime_extract.txt", "r") as file:
    regex = file.read()


df = pd.read_csv("../csv_merge/지방_1_수동.csv")

df = df[
    df["사건명"].str.contains(
        rf"{regex}",
        na=False,
    )
]

df.to_csv("./test.csv", index=False)
