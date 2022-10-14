from selenium import webdriver
import time
import random
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
user_agents_list = [
    "hello world",
    "agent test 2",
    "super"
]

useragent = UserAgent()

options.add_argument(f"user-agent={useragent.opera}")

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
driver = webdriver.Chrome(r"C:\Users\Zahar\PycharmProjects\Selenium\chromedriver\chromedriver.exe", options=options, )

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()