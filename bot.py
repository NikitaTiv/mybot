# Импорт библиотек
from datetime import datetime
import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import (greet_user, planet_constellation, quess_number, 
                      send_cat_picture, user_coordinates, talk_to_me)

# Импортирование файла с токеном и данными для входа
import settings

# Насторойка вывода логов
logging.basicConfig(filename='bot.log', 
                    format='[%(asctime)s] [%(levelname)s] => %(message)s', 
                    level=logging.INFO)

#Определение точного времени формата ('YYYY/MM/DD') 
today = datetime.now()
format_date = today.strftime("%Y/%m/%d")
  

def main():
    '''Создание тела бота, настройка диспетчера'''
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_constellation))
    dp.add_handler(CommandHandler('quess', quess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

#Прописываем if чтобы при импорте в другую программу, не запустился бот и все не сломалось
if __name__ == '__main__':
    main()