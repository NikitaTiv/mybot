from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings


def get_smile(user_data):
    '''Функция выбирает случайный смайлик'''
    if 'emoji' not in user_data:
      smile = choice(settings.USER_EMOJI)
      return emojize(smile, language='alias')
    return user_data['emoji']


def main_keyboard():
    '''Функция создает клавиатуру'''
    return ReplyKeyboardMarkup([['Прислать котика', KeyboardButton('Мои координаты', request_location=True)]], resize_keyboard= True)


def play_with_bot(user_number):
    '''Функция генерирует число бота и сравнивает его с вводом пользователя'''
    bot_number = randint(user_number -10, user_number +10)
    if user_number > bot_number:
      return f'Ваше число {user_number}, мое число {bot_number}. Вы победили'
    if user_number < bot_number:
      return f'Ваше число {user_number}, мое число {bot_number}. Вы проиграли'
    else:
      return f'Ваше число {user_number}, мое число {bot_number}. Ничья'
 