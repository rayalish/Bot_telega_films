import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.ivi.ru/collections/top-100-best-movies'

API_KEY = '6759549026:AAGHtL2uXI3dpw3mlB7_B-69gnVsJEdIR24'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    films = soup.find_all('span', class_= 'nbl-slimPosterBlock__titleText')
    return [f.text for f in films]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет!, здесь лучшие фильмы. Введите "хочу новый фильм посмотреть"')

@bot.message_handler(content_types=['text'])

def jokes(message):
    if message.text.lower() in 'хочу новый фильм посмотреть':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    elif message.text.lower() in 'спасибо':
        bot.send_message(message.chat.id, 'Обращайся!')
    else:
        bot.send_message(message.chat.id, 'Введите "хочу новый фильм посмотреть" данный текст')


bot.polling()