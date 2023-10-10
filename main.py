import telebot
import json
from telebot import types
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time


token = '6498967524:AAESVqMMvNrC1MIjiZXmYJG59SGw7Cj6cJQ'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def Start(message):
    text = "Введите песню или Исполнителя"
    bot.send_message(message.chat.id,text)
    bot.register_next_step_handler(message,search)

def search(message):
    global urls
    query = message.text
    browser = Chrome()
    browser.get("https://sefon.pro")
    search_input = browser.find_element(By.NAME ,'q')
    search_input.send_keys(query)
    search_input.send_keys(Keys.ENTER)
    urls = []
    time.sleep(1)
    for btn in browser.find_elements(By.CLASS_NAME, 'btns'):
        try:
            span = btn.find_element(By.TAG_NAME, 'span')
            url = span.get_attribute('data-url')
        except StaleElementReferenceException:
            continue
        except NoSuchElementException:
            continue
        if url:
            urls.append(url)
    for url in urls:
        bot.send_audio(message.chat.id,url)
    urls = []

bot.infinity_polling()

# Direct by Nursultan Malikov
# 5163171438 - user id Telegram

