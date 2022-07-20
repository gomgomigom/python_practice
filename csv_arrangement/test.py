import pandas as pd
import re
import os
import fitz
from tqdm import tqdm

tqdm.pandas()
os.chdir(os.path.dirname(__file__))


df = pd.read_csv("../csv_merge/court_one.csv", converters={"사건번호": pd.eval})
print(df["사건번호"][0])


def change_text(x):
    file_name = x["사건번호"][0]
    try:
        with fitz.open(f"../pdf_hwp/{file_name}") as doc:
            text = ""
            for page in doc:
                text += re.sub(r"\n", "", page.get_text())
            return text
    except fitz.fitz.FileDataError as err:
        print(err)
        return f"❌{file_name}" + str(err)


df["판례내용"] = df.progress_apply(change_text, axis=1)
print(df)
df.to_csv("./test2.csv", index=False)
