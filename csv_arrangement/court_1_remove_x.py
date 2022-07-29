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


def check_case(x):
    if x["RequiredOCR"] is False:
        try:
            crime = re.search(
                r"(\b사 *건\b)?(?(1)|(\b\d+[가-힣]{1,3}\d+\b))(.*?)(\n *피 *고 *인\b)?(?(4)|(\n *검 *사\b))",
                x["판례내용"],
                re.DOTALL,
            ).group(3)
            crime = not crime
        except AttributeError:
            return True
        return crime
    else:
        return True


df["RequiredOCR"] = df.apply(find_x, axis=1)
df["RequiredOCR"] = df.apply(check_case, axis=1)
print(df.shape)
df_true = df[df["RequiredOCR"]]
df_false = df[list(map(operator.not_, df["RequiredOCR"].to_list()))]

print(df.shape)
print(df[["RequiredOCR", "판례내용"]])
df_true.to_csv("../csv_arrangement/test_true.csv", index=False)
df_false.to_csv("../csv_arrangement/test_false.csv", index=False)
