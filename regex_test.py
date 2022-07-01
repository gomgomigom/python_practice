import pandas as pd
from tqdm import tqdm


df = pd.read_csv("./regex_tex.csv")

df["년도"] = df["file_name"].str.extract(r"(\d{4})(?=[ㄱ-ㅎ|ㅏ-ㅣ|가-힣])")
print(df)
df["구분"] = df["file_name"].str.extract(r"(?<=\d{4})([ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2})(?=\d)")
print(df)

test_df = df[df["file_name"].str.contains(r"고정|고단|고합")]
print(test_df)


def a_func(count):
    def b_func(c_func):
        print(f"{count} 번째 카운트입니다")
        print("b_func")

        def d_func():
            print("d_func")
            c_func()

        return c_func

    return b_func


@a_func(2)
def e_func():
    print("e_func")


print("############")
e_func()
