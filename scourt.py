import requests
import lxml
from bs4 import BeautifulSoup
import re
import pandas as pd
from tqdm import tqdm
import pdfplumber
import time


def read_pdf(file_name):
    check_pdf = re.compile(r".*\.pdf")
    if re.match(check_pdf, file_name) is None:
        return None
    try:
        with pdfplumber.open(f"./pdf_hwp/{file_name}") as pdf:
            pages = pdf.pages
            text = ""
            for page in pages:
                if page.width > page.height:
                    left = page.crop((0, 0, 0.5 * page.width, page.height))
                    right = page.crop(
                        (0.5 * page.width, 0, page.width, page.height)
                    )
                    text += re.sub(r"\n", "", left.extract_text())
                    text += re.sub(r"\n", "", right.extract_text())
                else:
                    text += re.sub(r"\n", "", page.extract_text())
            if len(text) < 100:
                text = f"❌{file_name} 한글인식불가 ! RequiredOCR"
    except AttributeError as err:
        print(err)
        text = f"❌{file_name} Error : {str(err)}"
    return text


# file_id = '1138672129786_104849.pdf'
# file_name = 'down.pdf'
def download_file(file_id, file_name=None):
    if not file_name:
        return
    download_url = f"https://file.scourt.go.kr//AttachDownload?&name=downForm&file={file_id}&path=003&downFile={file_name}"

    with open(f"./pdf_hwp/{file_name}", "wb") as file:
        response = requests.get(download_url)
        file.write(response.content)


def make_csv_file(body_content, file_name=None):
    if not file_name:
        return
    file_name = re.sub(r"\..{2,4}", r".csv", file_name)
    pd_body_content = pd.DataFrame(body_content)
    pd_body_content.to_csv(path_or_buf=f"./pdf_hwp/{file_name}", index=False)


empty_list = [{"seqnum": None}]
error_list = [{"error": None, "seqnum": None}]
for i in tqdm(range(13001, 25001)):
    try:
        base_url = "https://busan.scourt.go.kr/dcboard/new/DcNewsViewAction.work?&gubun=44&cbub_code=000410&searchWord=&pageIndex=1"
        params = {"seqnum": i}
        resp = requests.get(base_url, params=params)
        soup = BeautifulSoup(resp.content, "lxml")
        tbody_list = []
        tbody = soup.find("tbody")
        title = tbody.find("td", class_="title").text
        court = tbody.select_one("tr:nth-child(2) > td:nth-child(2)").text
        downloads = tbody.select("tr:nth-child(3) > td > a")
        url_regex = re.compile(r"\'(.*\..{2,4})\'\,\'(.*\..{2,4})\'")
        body = tbody.find("div", class_="view_content").getText()
        file_list = []
        file_name = None
        for download in downloads:
            file_id = url_regex.search(str(download)).group(1)
            file_name = url_regex.search(str(download)).group(2)
            file_list.append(file_name)
            download_file(file_id, file_name)

        body_content = [
            {
                "seqnum": i,
                "url": f"{base_url}&seqnum={i}",
                "제목": title,
                "법원": court,
                "내용": body,
                "file_name": file_list,
                "file_body": None,
            }
        ]
        text_list = []
        for file_name in file_list:
            text_list.append(read_pdf(file_name))

        body_content[0]["file_body"] = text_list

        if file_name is None:
            empty_list.append({"seqnum": i})
            print(f"empty: {i}")
        else:
            make_csv_file(body_content, file_name)
    except Exception as error:
        print(i)
        print(error)
        error_list.append({"error": error, "seqnum": i})


make_csv_file(empty_list, f"empty_list{int(time.time())}.csv")
make_csv_file(error_list, f"error_list{int(time.time())}.csv")
# In[18]:


# print(read_pdf('2005허5860.pdf'))
# with open('./pdf_hwp/eee.txt', 'w') as f:
#     text_desc = read_pdf('2005허5860.pdf')
#     f.write(text_desc)
