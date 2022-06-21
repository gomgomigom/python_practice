from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


driver = set_chrome_driver()


url1 = "https://www.law.go.kr/DRF/lawSearch.do?OC=nodam89&target=prec&type=XML&query=%EB%8B%B4%EB%B3%B4%EA%B6%8C"
driver.get(url1)
driver.implicitly_wait(3)
time.sleep(30)
driver.quit()
