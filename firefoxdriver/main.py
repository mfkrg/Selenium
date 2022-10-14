from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
import time

useragent = UserAgent()

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
options.set_preference("general.useragent.override", f"{useragent.opera}")
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
driver = webdriver.Firefox(options=options, executable_path= r"C:\Users\Zahar\PycharmProjects\Selenium\firefoxdriver\geckodriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()