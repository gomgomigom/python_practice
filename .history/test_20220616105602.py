from selenium import webdriver
import time

path = "/Users/gom/Documents/Coding/chromedriver"

driver = webdriver.Chrome(path)

url1 = "https://www.naver.com"
driver.get(url1)
