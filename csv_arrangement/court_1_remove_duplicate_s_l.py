import pandas as pd
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

df_supreme = pd.read_csv("./대법원_고_죄.csv")
df_local = pd.read_csv("../csv_merge/court_1_.csv")

supreme_case = df_supreme["사건번호"].to_list()

df_l_not_duplicate = [
    True if i not in supreme_case else False for i in df_local["사건번호"]
]
print(df_l_not_duplicate)
print(df_l_not_duplicate.count(True))
print(df_l_not_duplicate.count(False))

df_local_not_duplicate = df_local[df_l_not_duplicate]

df_local_not_duplicate.to_csv("./test.csv", index=False)
