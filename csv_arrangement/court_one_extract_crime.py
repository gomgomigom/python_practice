import pandas as pd
import re
import os

os.chdir(os.path.dirname(__file__))


df = pd.read_csv("./지방법원_1_죄명추출_중복제거_고.csv")
# df = pd.read_csv("./지방법원_1_죄명추출_중복제거_고.csv", nrows=1000, usecols=["사건번호", "사건명", "판례내용"])

with open("./crime_extract.txt", "r") as f:
    crime = f.read()

with open("./crime_extract_배임뺌.txt", "r") as f:
    crime_BE = f.read()

print(crime)


def remove_trash(text):
    result = text["사건명"]
    result = re.sub(r"\d*[가-힣]{1,3}\d*\(병합\)", "", result)
    result = re.sub(r"\d+\(병합\)|\(각병합\)", "", result)
    result = re.sub(r"\d+[가-힣]{1,3}\d+", "", result)
    result = re.sub(r"[가나다라마바사아자차카타파하]\.", ", ", result)
    result = re.sub(r"[가나다라마바]\s", ", ", result)
    result = re.sub(r"선고일|선고기일|\.\s?", "", result)
    result = re.sub(r"(?<!\()\d+(?!세)", "", result)
    result = re.sub(r"결\s*과", "", result)
    result = re.sub(
        r"○\s?죄명\s:|○|공소제기|\(우범자\)|배상명령신청|부착명령|\(분리\)|고정|고단|고합|\-", "", result
    )
    result = re.sub(r"\{", "(", result)
    result = re.sub(r"\}", "(", result)
    result = re.sub(r"\s{1,}", "", result)
    result = re.sub(r",(?!\s?[가-힣])", "", result)
    result = result.strip()
    result = re.sub(r"^·+|^\:|:$|\($|\(,\s|\[$", "", result)
    result = re.sub(r"^,", "", result)
    result = re.sub(r",", ", ", result)
    result = result.strip()
    if len(result) > 200:
        result = "🔴긺확인필요 " + result
    print("🥝" + str(text.name) + " " + str(len(result)) + " " + result)
    return result


def extract_crime(x):
    text = re.split(r"피\s*고\s*인", maxsplit=1, string=x["판례내용"])[0]
    try:
        text = text.rsplit(x["사건번호"], maxsplit=1)[1].strip()
    except IndexError:
        try:
            text = "❌사건번호없음" + x["판례내용"].split(x["사건번호"], maxsplit=1)[1][:400]
            text = re.split(r"피\s*고\s*인", maxsplit=1, string=text)[0]
        except IndexError:
            text = "❌❌사건번호없음 파일도이상한듯" + text[:120]

    if "한글인식불가" in text:
        print("🔥pdfOCR필요")
        text = "🔥pdfOCR필요" + text[:120]
        return text
    if len(text) > 120:
        if "배포를 금합니다" in text:
            print("❌배포금지")
            text = "❌배포금지" + text[:120]
            return text

        else:
            return text
    else:
        return text


df["사건명"] = df.apply(extract_crime, axis=1)

df_crime_BE = [
    True
    if bool(re.search(crime_BE, i))
    else False
    if bool(re.search(r"배임증재|배임수재", i))
    else True
    for i in df["사건명"]
]
print(df_crime_BE)
print(df_crime_BE.count(False))
df = df[df_crime_BE]
df_crime_check = [
    True if bool(re.search(crime, i)) else False for i in df["사건명"]
]
df = df[df_crime_check]
df["사건명"] = df.apply(remove_trash, axis=1)
df["판례내용"] = df["판례내용"].str[2:-2]
df.to_csv("./test.csv", index=False)
