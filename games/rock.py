from typing import Any

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, ContentType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from secondary_functions.second_functions import buttomer
from random import choice
from Database.Data import databaser

list_items: list = ['rock', '🪨 КАМЕНЬ', '📄БУМАГА', '✂️НОЖНИЦЫ']
vars_lose: list = [['🪨 КАМЕНЬ', '📄БУМАГА'], ['📄БУМАГА', '✂️НОЖНИЦЫ'], ['✂️НОЖНИЦЫ', '🪨 КАМЕНЬ']]
vars_win = [list(reversed(i)) for i in vars_lose]


def rock_game(message: Message) -> tuple[str, Any] | tuple[tuple[str, Any], Any]:
    result = ''
    user_answer = message.text
    id, data = databaser(message=message, returner=True)
    tries = data['games']['rock']['tries']
    bot = data['games']['rock']['bot_points']
    user = data['games']['rock']['points']
    flag=data['games']['rock']['in_game']
    if user_answer == list_items[0]:
        data['games']['rock']['in_game'] = True
        result = 'Игра будет состоять из 10 раундов.\nВыбирайте', data['games']['rock']['in_game']
    bot_answer = choice(list_items[1:])
    if user_answer == bot_answer:
        result = f'{bot_answer}\nНичья\nСчет {user}:{bot}\nОсталось попыток {tries}', data['games']['rock']['in_game']
    elif [user_answer, bot_answer] in vars_lose:
        bot += 1
        result = f'{bot_answer}\nНе угадали\nСчет {user}:{bot}\nОсталось попыток {tries}', data['games']['rock'][
            'in_game']
    elif [user_answer, bot_answer] in vars_win:
        user += 1
        result = f'{bot_answer}\nВаша взяла!\nСчет {user}:{bot}\nОсталось попыток {tries}', data['games']['rock'][
            'in_game']
    data['games']['rock']['tries'] = tries - 1
    data['games']['rock']['bot_tries'] = tries - 1
    if tries == 0 :
        data['games']['rock']['in_game'] = False
        if user<bot:
            result = (f'\n\nВы проиграли со счетом {user}:{bot}.\nЕсли хотите сыграть еще раз то напишите /mini_games',
                      data['games']['rock']['in_game'])
            data['games']['rock']['loses']+=1
        else:
            result = (f'\n\nВы выиграли со счетом {user}:{bot}!!.\nЕсли хотите сыграть еще раз то напишите /mini_games',
                      data['games']['rock']['in_game'])
            data['games']['rock']["wins"] += 1
        data['games']['rock']['tries'] = 10
        data['games']['rock']['bot_tries'] = 10
        data['games']['rock']['all_games'] += 1
        bot = 0
        user = 0

    data['games']['rock']['bot_points'] = bot
    data['games']['rock']['points'] = user
    databaser(message=message, id=id, id_data=data)
    return result


rock_btn = ReplyKeyboardBuilder()
rock_btn.row(*buttomer(list_items[1:]), width=3)
