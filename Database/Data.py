import json
from aiogram.types import Message, ContentType


data_path = 'Database/.database.json'
def databaser(message: Message|str = "", id='', id_data="", returner: bool = False) -> object:
    '''Функция для записи данных в базу данных.'''

    with open(data_path, 'r') as dates:
        user_field = json.load(dates)
        if id:
            user_field[id] = id_data
        else:
            id = str(message.from_user.id)
            if id not in user_field:
                user_field[id] = user_field.setdefault(id, {"message": [],'administration': False,
        "games": {'change_number':{'tries': 8, 'all_games': 0, "in_game": False,"wins": 0,"loses": 0},
        'rock' : {'points' : 0 ,'bot_points': 0, 'tries': 10, 'all_games': 0,'wins': 0,"loses": 0,"in_game":False}}})
        user_field[str(message.from_user.id)]["message"].append(message.text)
    if returner:
        return id, user_field[id]
    with open(data_path, 'w') as dates:
        json.dump(user_field, dates, indent=4)

def database_fields_updater()-> None:
    '''Функция для обновления и добавления новых полей в базу данных'''
    with open(data_path, 'r') as dates:
        user_field = json.load(dates)
        for i in user_field:
            if 'administration' not in user_field[i]:
                user_field[i]['administration'] = False
            if 'change_number' not in user_field[i]['games']:
                user_field[i]['games']['change_number']={'tries': 7, 'all games': 0,
                                                         "in_game": False,"wins": 0,"loses": 0}

            if 'rock' not in user_field[i]['games']:
                user_field[i]['games']['rock'] = {'tries': 7, 'all games': 0, "in_game":False}

            if'message' not in user_field[i]:
                user_field[i]['message'] = []
    with open(data_path, 'w') as dates:
        json.dump(user_field, dates, indent=4)

