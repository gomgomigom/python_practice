from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )


path = "/Users/gom/Documents/Coding/chromedriver"

driver = webdriver.Chrome(path)

url1 = "https://www.naver.com"
driver.get(url1)
time.sleep(3)
driver.quit()