from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import win32clipboard
import telebot

bot = telebot.TeleBot('5506740712:AAGC6stP91eN63hZbHyYZIfr4CxQ9y_SZ1Q')
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.opera}")
driver = webdriver.Chrome(r"C:\Users\Zahar\PycharmProjects\Selenium\chromedriver\chromedriver.exe", options=options)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Введи слово и получи транскрипцию!'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def transcr(message):
    driver.get("http://graecolatini.bsu.by/htm-different/latin-translit.htm")
    text_input = driver.find_element(By.ID, "text")
    button_click_med = driver.find_element(By.ID, "chMed").click()
    text_input.clear()
    text_input.send_keys(message.text)
    result_click = driver.find_element(By.ID, "convertButton").click()
    time.sleep(2)
    driver.find_element(By.ID, "text2").send_keys(Keys.CONTROL, 'a')
    driver.find_element(By.ID, "text2").send_keys(Keys.CONTROL, 'c')
    win32clipboard.OpenClipboard()
    clipped = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(clipped)
    bot.send_message(message.chat.id, clipped, parse_mode='html')

bot.polling(none_stop=True)