import pandas as pd
import re
import operator
import os

os.chdir(os.path.dirname(__file__))


df = pd.read_csv("../csv_merge/court_1_go.csv")
pd.set_option("display.max_rows", 8000)
pd.set_option("display.max_columns", 200)
pd.set_option("display.width", 20000)
print(df.shape)


def find_x(x):
    try:
        # crime = re.split(r'\n사 *건\b|\b사 *건 *번 *호\b|\n피 *고 *인\b', maxsplit=2, string=x['판례내용'])[1]
        crime = re.match(r"❌", x["판례내용"])
    except Exception:
        return "x"
    return bool(crime)


df["RequiredOCR"] = df.apply(find_x, axis=1)
print(df.shape)
df = df[list(map(operator.not_, df["RequiredOCR"].to_list()))]
# df = df[df["RequiredOCR"]]
print(df.shape)
print(df[["RequiredOCR", "판례내용"]])
df.to_csv("../csv_arrangement/test.csv", index=False)
