from selenium import webdriver
import time
from fake_useragent import UserAgent

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.opera}")
driver = webdriver.Chrome(r"C:\Users\Zahar\PycharmProjects\Selenium\chromedriver\chromedriver.exe", options=options, )
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"

try:
    driver.get("https://2ip.ru")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()