import pandas as pd
import re
import fitz
import os
from tqdm import tqdm
import pdfplumber

tqdm.pandas()
os.chdir(os.path.dirname(__file__))


df = pd.read_csv("./지방_1_사건번호_중복제거_고.csv", converters={"file_name": pd.eval})

with open("./crime_extract.txt", "r") as f:
    crime = f.read()
with open("./crime_extract_배임뺌.txt", "r") as f:
    crime_BE = f.read()
with open("./crime_extract.txt", "r") as file:
    regex = file.read()

print(crime)


def remove_trash(text):
    result = text["사건명"]
    result = re.sub(r"\d*[가-힣]{1,3}\d*\(병합\)", "", result)
    result = re.sub(r"\d+\(병합\)", "", result)
    result = re.sub(r"\(각병합\)", "", result)
    result = re.sub(r"\d+[가-힣]{1,3}\d+", "", result)
    result = re.sub(r"[가나다라마바사아자차카타파하]\.", ", ", result)
    result = re.sub(r"[가나다라마바]\s", ", ", result)
    result = re.sub(r"선고일|선고기일|\.\s?", "", result)
    result = re.sub(r"(?<!\()\d+(?!세)", "", result)
    result = re.sub(r"결\s*과", "", result)
    result = re.sub(
        r"○\s?죄명\s:|○|공소제기|\(우범자\)|배상명령신청|부착명령|\(분리\)|고정|고단|고합|\-|\(병합, 분리\)",
        "",
        result,
    )
    result = re.sub(r"\{", "(", result)
    result = re.sub(r"\}", "(", result)
    result = re.sub(r"\s{1,}", "", result)
    result = re.sub(r",(?!\s?[가-힣])", "", result)
    result = result.strip()
    result = re.sub(r"^·+|^\)|^\:|:$|\($|\(,\s|\[$", "", result)
    result = re.sub(r"^,", "", result)
    result = re.sub(r",", ", ", result)
    result = result.strip()
    if len(result) > 500:
        result = "❌확인필요❌" + result
    print("🥝" + str(text.name) + " " + str(len(result)) + " " + result)
    return result


def extract_crime(x):
    text = re.split(r"피\s*고\s*인", maxsplit=1, string=x["판례내용"])[0]
    try:
        text = text.rsplit(x["사건번호"], maxsplit=1)[1].strip()
    except IndexError:
        try:
            text = "❌사건번호❌" + x["판례내용"].split(x["사건번호"], maxsplit=1)[1][:500]
            text = re.split(r"피\s*고\s*인", maxsplit=1, string=text)[0]
        except IndexError:
            text = "❌사건번호❌" + text[:400]

    confirm = re.compile(
        r"\(\)|1심|2심|■|□|▣|◆|◇|◈|▶|►|▷|▹|▪|▫|[며따있너될으었극값내글는를데런없능게징a-zA-Z받월였옆빨압뒤했뻔함슴뜨렸찾]"
    )
    if bool(confirm.search(text)):
        return "❌확인필요❌" + text
    if "한글인식불가" in text:
        print("🔥pdfOCR필요")
        text = "❌pdfOCR필요❌" + text[:400]
        return text
    if len(text) > 300:
        if "배포를 금합니다" in text:
            print("❌배포금지❌")
            text = "❌배포금지❌" + text[:400]
            return text

        else:
            return text
    else:
        return text


df["사건명"] = df.progress_apply(extract_crime, axis=1)

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
df["사건명"] = df.progress_apply(remove_trash, axis=1)
# df["판례내용"] = df["판례내용"].str[2:-2]


def check_case(x):
    text = x.판례내용[2:150]
    case1 = re.compile(r"지 *방 *법 *원 *판 *결 *사 *건")
    case2 = re.compile(r"지 *방 *법 *원 *.{0,10}?형 *사 *부 *판 *결")
    case3 = re.compile(r"^사 *건 *\d+[가-힣]{1,3}\d+")
    case4 = re.compile(r"지 *방 *법 *원 *.*?지 *원 *판 *결")
    case5 = re.compile(r"^.{0,10}?지 *방 *법 *원")
    case6 = re.compile(r"판결요지서")
    case7 = re.compile(r"보도자료")
    if bool(case1.search(text)):
        return "1"
    elif bool(case2.search(text)):
        return "2"
    elif bool(case3.search(text)):
        return "3"
    elif bool(case4.search(text)):
        return "4"
    elif bool(case5.search(text)):
        return "5"
    elif bool(case6.search(text)):
        return "6"
    elif bool(case7.search(text)):
        return "7"
    else:
        return "e"


df["case"] = df.apply(check_case, axis=1)
# df = df[[True if i == "?" else False for i in df["비고"]]]


def case_x_change_text(x):
    file_name = x["file_name"][0]
    if x["case"] == "x":
        li = []
        try:
            with pdfplumber.open(f"../pdf_hwp/{file_name}") as pdf:
                doc = pdf.pages
                text = ""
                for page in doc:
                    left = page.crop(
                        (
                            0,
                            0,
                            0.5 * float(page.width),
                            1 * float(page.height),
                        )
                    )
                    right = page.crop(
                        (
                            0.5 * float(page.width),
                            0,
                            1 * float(page.width),
                            1 * float(page.height),
                        )
                    )
                    text += re.sub(r"\n", "", left.extract_text())
                    text += re.sub(r"\n", "", right.extract_text())
                if len(text) < 100:
                    text = f"❌{file_name} 한글인식불가 ! RequiredOCR"
            li.append(text)
            return str(li)
        except AttributeError as err:
            print(err)
            text = f"❌{file_name} Error : {str(err)}"
            li.append(text)
            return str(li)
    else:
        return x["판례내용"]


df["판례내용"] = df.progress_apply(case_x_change_text, axis=1)
df["사건명"] = df.progress_apply(extract_crime, axis=1)
df["사건명"] = df.progress_apply(remove_trash, axis=1)

df = df[
    df["사건명"].str.contains(
        rf"{regex}",
        na=False,
    )
]


df.to_csv(
    "./test.csv",
    index=False,
    columns=[
        "판례정보일련번호",
        "사건명",
        "사건번호",
        "선고일자",
        "법원명",
        "판시사항",
        "판결요지",
        "참조조문",
        "참조판례",
        "판례내용",
        "비고",
        "제목",
        "내용",
        "case",
        "file_name",
    ],
)
