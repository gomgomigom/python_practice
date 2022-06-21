from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

path = "/Users/gom/Documents/Coding/chromedriver"

driver = webdriver.Chrome(path)

url1 = "https://www.naver.com"
driver.get(url1)
time.sleep(3)
driver.quit()
