import ephem
from glob import glob
from random import choice

from utils import play_with_bot, get_smile, main_keyboard


def greet_user(update, context):
    '''Функция вызываемая про вводе пользователем /start'''
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
      f"Здравствуй, пользователь {context.user_data['emoji']}!",
      reply_markup = main_keyboard())


def talk_to_me(update, context):
    '''Функция вызываемая при вводе пользователем текстового сообщения'''
    text = update.message.text
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup = main_keyboard())


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
    update.message.reply_text(message, reply_markup = main_keyboard())


def send_cat_picture(update, context):
    '''Функция отправляет котов'''
    cat_photo_list = glob('images/cat*.jp*g')
    cat_pict_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id = chat_id, photo = open(cat_pict_filename, 'rb'), reply_markup = main_keyboard())
   

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    print(coords)
    update.message.reply_text(f"Ваши координаты {coords} {context.user_data['emoji']}",
    reply_markup = main_keyboard())


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
