import pandas as pd
import numpy as np
import os
import re
from tqdm import tqdm

tqdm.pandas()
os.chdir(os.path.dirname(__file__))

df = pd.read_csv("../csv_merge/court_1.csv")

df["사건번호"] = df["사건번호"].str.extract(r"(\d{4}[가-힣]{1,3}\d+)")
df["사건번호"] = df["사건번호"].fillna(np.nan)


def test(x):
    if x["사건번호"] is np.nan:
        try:
            result = re.search(r"\b(\d+[가-힣]{1,3}\d+)\b", x["판례내용"]).group(1)
        except AttributeError:
            try:
                result = re.search(r"\b(\d+[가-힣]{1,3})", x["판례내용"]).group(1)
                print(x.name)
                print(x["판례내용"][:70])
            except AttributeError:
                result = np.nan
                print(f"🔥np.nan: {x.name}")
                print(f"🔥np.nan: {x['판례내용'][:70]}")

        return result
        # return print(x["판례내용"].extract(r"(\d+[가-힣]{1,3}\d+)"))
    else:
        return x["사건번호"]


df["사건번호"] = df.progress_apply(test, axis=1)
# df["사건번호"] = df["사건번호"].apply(test)
print(df["사건번호"].isna().sum())


df.to_csv("./test.csv", index=False)


# df = pd.read_csv("./test.csv", converters={"판례내용": pd.eval})
# print(df)

# df2 = df["사건번호"].str.findall(
#     r"\d+[가-힣]{1,3}\d+|\d+[가-힣]{1,3}\d+|\d+[가-힣]{1,3}\d+|[가-힣]{1,3}\d+",
# )

# df["사건번호"] = df2

# 리스트를 문자열로 바꾸는 함수
# def try_join(l):
#     try:
#         return ",".join(map(str, l))
#     except TypeError:
#         return np.nan

# print(df)
# df3 = [try_join(l) for l in df["사건번호"]]
# print(df3)
# print(df)

# x = []
# for l in df["사건번호"]:
#     x.append(try_join(l))

# print(x)

# df["사건번호"] = df3
# print(df)

# 문자열을 리스트로 바꾸는 함수
# def try_split(l):
#     try:
#         return str(l).split(",")
#     except TypeError:
#         return np.nan

# df4 = [try_split(l) for l in df["사건번호"]]
# print(df4)
# df["사건번호"] = df4
# print(df)

# print(df[[True if len(i) == 1 else False for i in df["사건번호"].to_list()]])
# print([len(i) for i in df["판례내용"].to_list()])
