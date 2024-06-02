import random

patt = {"start": ['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу играть', '/game', '/game_continue','/stats'],
        'end': ['/cancel', 'нет', 'не хочу', 'не хочу играть'],
        'body': ["Программа принимает только числа ,пожалуйста введите число",
                 'Начинайте отгадывать )',
                 'Слишком много, попробуйте еще раз',
                 'Слишком мало, попробуйте еще раз',
                 "Хорошо давайте начнем игру!У вас будет 6 попыток чтобы отгадать число )"
                 "\nВведите значение максимаьльной границы "]}

def valid(number):
    try:
        return int(number)
    except:
        return (patt['body'][0])


def numbers(data, answer=100):
    tries = int(data['tries'])
    if answer == '/stats':
        return (
                f"Всего игр: {data['all games']}\n"
                f"Побед: {data['wins']}\n"
                f"Процент побед:, {round(data['wins'] / data['all games'] * 100, 2)}%\n")
    if answer in patt['end']:
        data['tries'] = 8
        data['in_game'] = False
        return ('Хорошо, если захотите сыграть, вы уже знаете нужные команды ')
    if tries == 8:
        if answer == "/game_continue":
            data['in_game'] = True
            data['tries'] = 7
            return ("Рада что вы остались!\n" + patt['body'][4])
        data['in_game'] = True
        data['tries'] = 7
        return (patt['body'][4])
    validation = valid(answer)
    if isinstance(validation, str):
        return validation

    if tries == 7:
        data['tries'] = 6
        data.setdefault('random', None)
        data["random"] = random.randint(1, validation)
        return (patt['body'][1])

    if 6 >= tries > 0:
        if data["random"] < validation:
            data['tries'] = tries - 1
            return (patt['body'][2])
        if data["random"]> validation:
            data['tries'] = tries - 1
            return (patt['body'][3])
        if data["random"] == validation:
            data['tries'] = 8
            data['all games'] = int(data['all games']) + 1
            data['wins'] = int(data['wins']) + 1
            data['in_game'] = False
            return (f"Вы угадали, поздравляем!\n"
                    f"Число ваших попыток:, {tries}\n"
                    f"Хотите сыграть еще раз? Если да то напишите /game_continue ,если нет /cancel\n")
    else:
        data['tries'] = 7
        data['all games'] = int(data['all games']) + 1
        data['loses'] = int(data['loses']) + 1
        data['in_game'] = False
        return ('Увы вы проиграли (\n'
                'Если хотите сыграть еще раз то напишите /game_continue ,если нет /cancel\n')
