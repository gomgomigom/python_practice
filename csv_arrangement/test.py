import pandas as pd
import os
import numpy as np

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("./지방법원_1_pymupdf.csv")

print(df)
df["판례내용"] = df["판례내용"].fillna(np.nan)
df["판례내용"] = df["판례내용"].fillna("❌한글인식불가")
df["판례내용"] = df.apply(lambda x: x["판례내용"], axis=1)
print(df)

df.to_csv("./test2.csv", index=False)
