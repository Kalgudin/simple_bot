import telebot

from main.tokens import TOKEN_b2

# Чуть посложнее, может огрызаться :) ###########################################################

bot = telebot.TeleBot(TOKEN_b2)


@bot.message_handler(commands=['start'])  # обработчик команд( начинается с слэша )
def main(message):
    bot.send_message(message.chat.id, f'Hellow {message.from_user.first_name}!')


@bot.message_handler(content_types=['text'])  # обработчик любого текста, должен идти ниже обработчиков команд(иначе команды обрабатываться не будут)
def info(message):
    if message.text.lower() == 'hellow' or message.text.lower() == 'hi' or message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hellow, {message.from_user.first_name}!')
    elif message.text.lower() == 'fack you':
        bot.send_message(message.chat.id, f'Go FACK yourself, {message.from_user.first_name}!')
    else:
        bot.send_message(message.chat.id, f'You sad, {message.text}?')  # ЭХО ответ


my_bot_2 = bot

