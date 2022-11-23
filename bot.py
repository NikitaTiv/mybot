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
    main()