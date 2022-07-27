import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("../csv_merge/court_one.csv")
print(df.columns)
df = df.drop(["판례정보일련번호", "사건명", "선고일자", "법원명", "판시사항", "판결요지", "참조조문"], axis=1)
df.head(100).to_csv("./test.csv", index=False)
