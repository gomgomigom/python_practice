from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("disable-gpu")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


driver = set_chrome_driver()


url1 = "https://www.naver.com"
driver.get(url1)
driver.implicitly_wait(3)
driver.get_screenshot_as_file("naver_main_headless.png")
time.sleep(30)
driver.quit()
