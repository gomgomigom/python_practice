from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from requests import get
import time


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    )
    chrome_options.add_argument("lang=ko_KR,ko,en-US,zh-CN")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


driver = set_chrome_driver()


url1 = "https://www.naver.com"
driver.get(url1)
user_agent = driver.find_element_by_css_selector("#user-agent").text
print("user-agent", user_agent)
driver.implicitly_wait(3)
driver.get_screenshot_as_file("naver_main_headless1.png")
time.sleep(5)
driver.quit()

javascript: download(
    "1352768201699_095641.pdf", "2011%EB%93%9C%EB%8B%A80000.pdf"
)
javascript: download("1352769436651_101716.pdf", "2012%EB%82%9820162.pdf")

ㅌseqnum = 10000
if __name__ == "__main__":
    url = f"https://busan.scourt.go.kr/dcboard/new/DcNewsViewAction.work?seqnum={seqnum}&gubun=44&cbub_code=000410&searchWord=&pageIndex=1"
    download(
        url,
    )
