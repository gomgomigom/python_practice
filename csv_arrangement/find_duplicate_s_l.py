import pandas as pd
import re
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

df_supreme = pd.read_csv("./대법원_고_죄.csv")
df_local = pd.read_csv("./지방법원_1_죄명추출.csv")

supreme_case = df_supreme["사건번호"].to_list()

df_l_not_duplicate = [
    True if i not in supreme_case else False for i in df_local["사건번호"]
]
print(df_l_not_duplicate)
print(df_l_not_duplicate.count(True))

df_local_not_duplicate = df_local[df_l_not_duplicate]

df_local_not_duplicate.to_csv("./test.csv", index=False)
