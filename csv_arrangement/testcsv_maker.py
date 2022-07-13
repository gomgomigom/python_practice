import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("../csv_merge/court.csv")
df["seqnum"] = df["seqnum"] + 50000000
df = df.rename(
    columns={
        "file_name": "사건번호",
        "file_body": "판례내용",
        "법원": "법원명",
        "seqnum": "판례정보일련번호",
    }
)
df = df.drop(["url", "제목", "내용"], axis=1)
df.head(10).to_csv("./test.csv", index=False)
