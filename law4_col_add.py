import pandas as pd
from tqdm import tqdm

df_origin = pd.read_csv("./csv_merge/precedent.csv")
df_new = pd.read_csv("./csv_merge/cases.csv")

df_origin["판례상세링크"] = df_new["판례상세링크"]

print(df_origin)
df_origin.to_csv("./warehouse/precedent_merge.csv", index=False)
