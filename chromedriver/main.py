from selenium import webdriver
import time

url = "http://graecolatini.bsu.by/htm-different/latin-translit.htm"
driver = webdriver.Chrome(executable_path="C:\\Users\\Zahar\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()