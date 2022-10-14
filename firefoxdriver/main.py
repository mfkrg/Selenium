from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

url = "http://graecolatini.bsu.by/htm-different/latin-translit.htm"
driver = webdriver.Firefox(options=options, executable_path="C:\\Users\\Zahar\\PycharmProjects\\Selenium\\firefoxdriver\\geckodriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()