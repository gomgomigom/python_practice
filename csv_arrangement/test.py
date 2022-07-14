import pandas as pd
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("./test.csv", converters={"판례내용": pd.eval})
print(df)

df2 = df["사건번호"].str.findall(
    r"\d+[가-힣]{1,3}\d+|\d+[가-힣]{1,3}\d+|\d+[가-힣]{1,3}\d+|[가-힣]{1,3}\d+",
)

df["사건번호"] = df2


def try_join(l):
    try:
        return ",".join(map(str, l))
    except TypeError:
        return np.nan


print(df)
df3 = [try_join(l) for l in df["사건번호"]]
print(df3)
print(df)

x = []
for l in df["사건번호"]:
    x.append(try_join(l))


print(x)

df["사건번호"] = df3
print(df)


def try_split(l):
    try:
        return str(l).split(",")
    except TypeError:
        return np.nan


df4 = [try_split(l) for l in df["사건번호"]]
print(df4)
df["사건번호"] = df4
print(df)

print(df[[True if len(i) == 1 else False for i in df["사건번호"].to_list()]])
print([len(i) for i in df["판례내용"].to_list()])
