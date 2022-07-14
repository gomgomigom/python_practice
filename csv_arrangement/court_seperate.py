import pandas as pd
import os

os.chdir(os.path.dirname(__file__))


df = pd.read_csv(
    "../csv_merge/court.csv",
    converters={"file_name": pd.eval, "file_body": pd.eval},
)
count = 0
print(df.columns)
print([len(i) for i in df["file_name"].to_list()].count(1))
print(len([len(i) for i in df["file_name"].to_list()]))
print(max([len(i) for i in df["file_body"].to_list()]))


df = df.rename(
    columns={
        "file_name": "사건번호",
        "file_body": "판례내용",
        "법원": "법원명",
        "seqnum": "판례정보일련번호",
    }
)

df["판례정보일련번호"] = df["판례정보일련번호"] + 50000000
df = df.drop(["url"], axis=1)
one_true_list = [True if len(i) == 1 else False for i in df["사건번호"].to_list()]
sev_true_list = [True if len(i) > 1 else False for i in df["사건번호"].to_list()]
df_one = df[one_true_list]
print(df_one)
df_several = df[sev_true_list]
print(df_several)

df_one.to_csv("../csv_merge/court_one.csv", index=False)
df_several.to_csv("../csv_merge/court_several.csv", index=False)
