import requests
import telebot
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

weather_token = os.environ['TOKEN']
bot_token = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Enter the name of the city and I will give out information about the weather')


@bot.message_handler(content_types=['text'])
def main(message):
    data = get_weather(message.text.lower(), weather_token)
    bot.send_message(message.chat.id, f'''{data[0]}
Temperature: {data[1]}°C
Pressure: {data[2]} mm Hg
Humidity: {data[3]}%
Wind speed: {data[4]} m/s
{data[5]}''')


def get_weather(city, token):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric')
        info = r.json()
        #  pprint(info)
    except Exception as e:
        return e
    else:
        data = []
        data.append(info['name'])
        data.append(info['main']['temp'])
        data.append(str(round(0.75 * float(info['main']['pressure']), 2)))
        data.append(info['main']['humidity'])
        data.append(str(round(0.447 * float(info['wind']['speed']), 2)))
        data.append(info['weather'][0]['main'])
        return data


bot.polling(none_stop=True)
