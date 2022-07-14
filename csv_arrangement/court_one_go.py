import pandas as pd
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("../csv_merge/court_one.csv")
df["사건번호"] = df["사건번호"].str.extract(r"(\d+[가-힣]{1,3}\d+)")
df["사건번호"] = df["사건번호"].fillna(np.nan)


def test(x):
    if x is np.nan:
        print(x.name)
        return print(df["판례내용"].str.extract(r"(\d+[가-힣]{1,3}\d+)"))
    else:
        return x


df["사건번호"] = df["사건번호"].apply(test, axis=1)

df.to_csv("./test2.csv", index=False)
