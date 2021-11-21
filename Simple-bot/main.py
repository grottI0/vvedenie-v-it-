import telebot
from telebot import types
from random import randint
from token import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/random", "/game", "/sum", "Не хочу")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '''Я умею:
генерировать случайные числа (/random)
загадывать число (подробнее /game)
складывать числа (подробнее /sum)''')


@bot.message_handler(commands=['random'])
def random_number(message):
    bot.send_message(message.chat.id, str(randint(1, 100))+"/100")


@bot.message_handler(commands=['game'])
def start_message(message):
    bot.send_message(message.chat.id, 'загадано число от 1 до 3. Для того чтобы угадать отправь чило от 1 до 3 \
(с каждым сообщением число меняется)')


@bot.message_handler(commands=['sum'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пришли выражение вида a + b,  и я выведу сумму  \
числа меньше нуля вводятся без скобок')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() in ["[jxe", "{jxe"]:
        bot.send_message(message.chat.id, 'Смени раскладку :|')
    elif message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'ну ладно(')
    elif message.text in ['1', '2', '3', '4', '5']:
        if str(randint(1, 5)) == message.text:
            bot.send_message(message.chat.id, 'ты угадал!')
        else:
            bot.send_message(message.chat.id, 'ты не угадал!')
    elif '+' in message.text:
        for i in range(len(message.text.lower())):
            if message.text.lower()[i] == '+':
                try:
                    number1 = int(message.text[:i])
                    number2 = int(message.text[(i+1)::])
                except ValueError:
                    bot.send_message(message.chat.id, 'неверный ввод')
                else:
                    bot.send_message(message.chat.id, str(number2+number1))


bot.polling(none_stop=True)
