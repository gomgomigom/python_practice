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


set_chrome_driver()

path = "/Users/gom/Documents/Coding/chromedriver"


url1 = "https://www.naver.com"
driver.get(url1)
time.sleep(3)
driver.quit()
