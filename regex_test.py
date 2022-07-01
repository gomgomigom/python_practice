import pandas as pd
from tqdm import tqdm


df = pd.read_csv("./regex_tex.csv")

df["년도"] = df["file_name"].str.extract(r"(\d{4})(?=[ㄱ-ㅎ|ㅏ-ㅣ|가-힣])")
df["사건번호"] = df["file_name"].str.extract(r"(\d{4}[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2}\d{1,4})")
df["구분"] = df["file_name"].str.extract(r"(?<=\d{4})([ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2})(?=\d)")
print(df)
df.to_csv("./warehouse/test.csv", index=False)
print(df)
df = pd.read_csv("./warehouse/test.csv")


test_df = df[df["사건번호"].str.contains(r"고정|고단|고합", na=False)]
print(test_df)


def column_add(file_name):
    df = pd.read_csv(file_name)
    df["사건번호"] = df["file_name"].str.extract(
        r"(\d{4}[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2}\d{1,4})"
    )
    test_df = df[df["사건번호"].str.contains(r"고정|고단|고합", na=False)]
    print(test_df)
    test_df.to_csv("./warehouse/test.csv", index=False)


if __name__ == "__main__":
    file_name = "./csv_merge/court.csv"
    column_add(file_name)
