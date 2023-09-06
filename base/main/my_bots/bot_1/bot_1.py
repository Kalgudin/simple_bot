import telebot
from main.tokens import TOKEN_b1

# from main.tokens import TOKEN_b1

# Simple echo-bot ############################################################


bot = telebot.TeleBot(TOKEN_b1)


@bot.message_handler(commands=['start'])  # обработчик команд( начинается с слэша )
def main(message):
    bot.send_message(message.chat.id, f'Hellow {message.from_user.first_name}!')


@bot.message_handler()  # обработчик любого текста, должен идти ниже обработчиков команд(иначе команды обрабатываться не будут)
def info(message):
    if message.text.lower() == 'hellow' or message.text.lower() == 'hi' or message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hellow, {message.from_user.first_name}!')
    else:
        bot.send_message(message.chat.id, f'Все говорят {message.text}, а ты купи слона!')  # ЭХО ответ


my_bot_1 = bot



# @bot.message_handler(commands=['site', 'website'])
# def main(message):
#     webbrowser.open('https://yandex.ru')
#
#
# @bot.message_handler(commands=['hellow', 'hi!'])  # обработчик команд( начинается с слэша )
# def main(message):
#     bot.send_message(message.chat.id, f'Hellow {message.from_user.first_name}!')
#
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<u>Some <b>help</b> <em>info</em></u>', parse_mode='html')
#
#
# @bot.message_handler()  # обработчик любого текста, должен идти ниже обработчиков команд(иначе команды обрабатываться небудут)
# def info(message):
#     if message.text.lower() == 'hellow' or message.text.lower() == 'hi' or message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Hellow, {message.from_user.first_name}!')
#     elif message.text.lower() == 'fack you':
#         bot.send_message(message.chat.id, f'Go FACK yourself, {message.from_user.first_name}!')
#     else:
#         bot.reply_to(message, f'Can`t understand you, {message.from_user.first_name}!')  # Альтернативный вариант ответа
#

# BUTTONS + Передача файлов
# @bot.message_handler(content_types=CONTENT_TYPES)
# def get_any_content(message):
#     if message.content_type == 'document':  # Проверяем тип контента
#         bot.reply_to(message, 'It`s DOCUMENT!!!!!!!!!')
#     elif message.content_type == 'photo':
#         bot.reply_to(message, 'It`s Photo!')
#
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Btn 1 - URL', url='https://ya.ru')
#     btn2 = types.InlineKeyboardButton('Btn 2 - Del', callback_data='delete')            # callback_data - может быть любым, его ловим с ледующей функции
#     btn3 = types.InlineKeyboardButton('Btn 3 - Edit', callback_data='какая-то хрень')   #  Пример :)
#     markup.row(btn1)                                                            #  First ROW
#     markup.row(btn2, btn3)                                                      #  Second Row with 2 battons
#     bot.reply_to(message, 'We get your data...', reply_markup=markup)

#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_massage(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id-1)  #  Удаляем отправленный файл
#     elif callback.data == 'какая-то хрень':
#         bot.edit_message_text('Edited text!!!!!!', callback.message.chat.id, callback.message.message_id)
#     else:
#         print('Сюда я не должен был попасть  :)')





