<<<<<<< HEAD
# Импорт библиотек
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Импортирование файла с токеном и данными для входа
import settings

# Насторойка вывода логов
logging.basicConfig(filename='bot.log', 
                    format='[%(asctime)s] [%(levelname)s] => %(message)s', 
                    level=logging.INFO)

#Настройка прокси сервера
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    '''Функция вызываемая про вводе пользователем /start'''
    print('Вызван /start')
    update.message.reply_text('Здравствуй пользователь!')


def talk_to_me(update,context):
    '''Функция вызываемая при вводе пользователем текстового сообщения'''
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    '''Создание тела бота, настройка диспетчера'''
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

#Прописываем if чтобы при импорте в другую программу, не запустился бот и все не сломалось
if __name__ == '__main__':
=======
"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
# Импорт библиотек
from datetime import datetime
from emoji import emojize
import ephem
from glob import glob
import logging
from random import choice, randint 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Импортирование файла с токеном и данными для входа
import settings

# Насторойка вывода логов
logging.basicConfig(filename='bot.log', 
                    format='[%(asctime)s] [%(levelname)s] => %(message)s', 
                    level=logging.INFO)

#Определение точного времени формата ('YYYY/MM/DD') 
today = datetime.now()
format_date = today.strftime("%Y/%m/%d")


def get_smile(user_data):
    '''Функция выбирает случайный смайлик'''
    if 'emoji' not in user_data:
      smile = choice(settings.USER_EMOJI)
      return emojize(smile, language='alias')
    return user_data['emoji']


def greet_user(update, context):
    '''Функция вызываемая про вводе пользователем /start'''
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Здравствуй, пользователь {context.user_data['emoji']}!")


def planet_constellation(update, context):
    '''Функция отвечающая пользователю в каком созвездии находится планета'''
    text = update.message.text.split()
    #Перебирает список кортежей библиотеки, оставляет только название планеты
    list_planet = [name for _0, _1, name in ephem._libastro.builtin_planets()] 
    #Сравнивает ввод пользователя и список list_planet
    if text[1] in list_planet:
      #Получаем название планеты с помощью функции getattr()
      planet = getattr(ephem, text[1])
      #Вычисляем координаты
      coord_planet = planet(format_date)
      #По коорд. определяем созвездие
      const = ephem.constellation(coord_planet)
      #Передаем ответ пользователю
      update.message.reply_text(const)
    else:
      update.message.reply_text('Эта планета еще не открыта')


def play_with_bot(user_number):
    '''Функция генерирует число бота и сравнивает его с вводом пользователя'''
    bot_number = randint(user_number -10, user_number +10)
    if user_number > bot_number:
      return f'Ваше число {user_number}, мое число {bot_number}. Вы победили'
    if user_number < bot_number:
      return f'Ваше число {user_number}, мое число {bot_number}. Вы проиграли'
    else:
      return f'Ваше число {user_number}, мое число {bot_number}. Ничья'


def quess_number(update, context):
    '''Функция проверяет данные которые ввел пользователь для игры'''
    if context.args:
      try:
        user_number = int(context.args[0])
        message = play_with_bot(user_number)
      except (ValueError, TypeError):
        message = 'Введите целое число'
    else:
      message = 'Введите число'
    update.message.reply_text(message)


def send_cat_picture(update, context):
    '''Функция отправляет котов'''
    cat_photo_list = glob('images/cat*.jp*g')
    cat_pict_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id = chat_id, photo = open(cat_pict_filename, 'rb'))
      

def talk_to_me(update, context):
    '''Функция вызываемая при вводе пользователем текстового сообщения'''
    text = update.message.text
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"{text} {context.user_data['emoji']}")


def main():
    '''Создание тела бота, настройка диспетчера'''
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_constellation))
    dp.add_handler(CommandHandler('quess', quess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

#Прописываем if чтобы при импорте в другую программу, не запустился бот и все не сломалось
if __name__ == '__main__':
>>>>>>> 34ac1c3 (Смайлики и картинки)
    main()