import pandas as pd
import os
import re
import pdfminer
import pdfplumber
from tqdm import tqdm

tqdm.pandas()
os.chdir(os.path.dirname(__file__))

df = pd.read_csv(
    "../csv_merge/지방_1_수동편집_완완.csv", converters={"file_name": pd.eval}
)


def convert_2columns_pdf(x):
    file_name = x["file_name"][0]
    li = []
    try:
        with pdfplumber.open(f"../pdf_hwp/{file_name}") as pdf:
            li = []
            pages = pdf.pages
            text = ""
            for page in pages:
                try:
                    if page.width > page.height:
                        left = page.crop((0, 0, 0.5 * page.width, page.height))
                        right = page.crop(
                            (0.5 * page.width, 0, page.width, page.height)
                        )
                        text += re.sub(r"\n", "", left.extract_text())
                        text += re.sub(r"\n", "", right.extract_text())
                    else:
                        text += re.sub(r"\n", "", page.extract_text())
                except AttributeError as err1:
                    text = f"❌ Error1 {file_name} : {str(err1)}"
                    print(text)
            if len(text) < 9:
                text = f"❌ Error2 {file_name} 한글인식불가 ! RequiredOCR"
                print(text)
            li.append(text)
    except pdfminer.pdfparser.PDFSyntaxError as err3:
        text = f"❌ Error3 {file_name} : {str(err3)}"
        print(text)
        li.append(text)
    return li


df.판례내용 = df.progress_apply(convert_2columns_pdf, axis=1)

df.to_csv("./test.csv", index=False)
