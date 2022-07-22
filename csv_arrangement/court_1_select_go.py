# -*- coding: utf-8 -*-
import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("./지방_1_사건번호_중복제거.csv")

df = df[df["사건번호"].str.contains(r"고정|고단|고합", na=False)]
print(df)
df.to_csv("./test.csv", index=False)
