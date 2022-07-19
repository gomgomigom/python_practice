import pandas as pd
import os
import re

os.chdir(os.path.dirname(__file__))

df = pd.read_csv(
    "./지방법원_1_죄명추출_중복제거_고.csv", nrows=1000, usecols=["사건번호", "사건명", "판례내용"]
)


def extract_crime(x):
    return x


# print(
#     df["판례내용"]
#     .str.split(r"피\s*고\s*인", 1, expand=True)[0]
#     .str.split(pat=df["사건번호"], n=1)
# )
def remove_trash(text):
    result = re.sub(r"\d*[가-힣]{1,3}\d*\(병합\)", "", text)
    result = re.sub(r"\d+\(병합\)", "", result)
    result = re.sub(r"\s{2,}", " ", result)
    result = re.sub(r",(?!\s?[가-힣])", "", result)
    result = re.sub(r".*죄\s?명\s?:", "", result)
    result = re.sub(r"^·", "", result)
    result = result.strip()

    return result


def extract_crime(x):
    l = re.split(r"피\s*고\s*인", maxsplit=1, string=x["판례내용"])[0]
    try:
        l = l.rsplit(x["사건번호"], maxsplit=1)[1].strip()
    except IndexError:
        try:
            l = "❌" + x["판례내용"].split(x["사건번호"], maxsplit=1)[1][:100]
        except IndexError:
            l = "❌❌" + l

    pattern = re.compile(r"배포를\s?금합니다")
    if "한글인식불가" in l:
        return "🔥pdf"
    if len(l) > 100:
        if "배포를 금합니다" in l:
            print("❌배포금지")
            return "❌ 배포금지 ❌"

        else:
            print(remove_trash(l))
            return remove_trash(l)
    else:
        print(remove_trash(l))
        return remove_trash(l)


df["사건명"] = df.apply(extract_crime, axis=1)


df.to_csv("./test.csv", index=False)
