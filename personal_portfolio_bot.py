# библиотеки, которые загружаем из вне
from telebot import types
import telebot
from os import environ
from dotenv import load_dotenv
load_dotenv()
TOKEN = environ['personal_portfolio_bot']


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🗃️ Мой репозиторий GitHub")
    item2 = types.KeyboardButton("🗃️ Мой репозиторий GitLab")
    item3 = types.KeyboardButton("✍🏻 Написать мне в личку")
    item4 = types.KeyboardButton("📖 Мой сайт")
    markup.row(item1, item2)
    markup.row(item3, item4)

    bot.send_message(message.chat.id, "Привет тебе от краба, {0.first_name}!".format(message.from_user),
                     parse_mode='html', reply_markup=markup)

# назначаем действие для клавиатуры


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🗃️ Мой репозиторий GitHub':
            bot.send_message(message.chat.id, 'https://github.com/Napster256')
        elif message.text == '✍🏻 Написать мне в личку':
            bot.send_message(message.chat.id, 'https://t.me/Shadow_zeus')
        elif message.text == '📖 Мой сайт':
            bot.send_message(
                message.chat.id, 'https://napster256.github.io/KubsuStudioPersonalPortfolio/')
        elif message.text == '🗃️ Мой репозиторий GitLab':
            bot.send_message(message.chat.id, 'https://gitlab.com/Napster256')
        else:
            bot.send_message(
                message.chat.id, 'Не знаю что ответить😢. С уважением, ваш бот {0.first_name}'.format(bot.get_me()))


bot.polling(none_stop=True)
