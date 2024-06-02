from aiogram import Router, F
from aiogram.types import Message
from lexicon.text_patterns import LexRU, new_commands
from games import Change_number, rock
from Database.Data import databaser
from aiogram.filters import Filter, Command
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message,
                           ReplyKeyboardRemove, ReplyKeyboardMarkup)
from keybords.under_keybords import web_app_keyboard, mini_game_keybords

router = Router()


@router.message(Command(commands='mini_games'))
async def mini_games(message: Message):
    await message.answer(text='Выберите игру', reply_markup=mini_game_keybords.as_markup(resize_keyboard=True))


@router.message(lambda message: message.text in ['rock'] + rock.list_items)
async def rock_games(message: Message):
    ans ,flag= rock.rock_game(message)
    if not flag:
        await message.answer(text=ans, reply_markup=ReplyKeyboardRemove())

    else:
        await message.answer(text=ans, reply_markup=rock.rock_btn.as_markup(resize_keyboard=True))


@router.message(Command(commands='games_stats'))
async def games_stats(message: Message):
    ans=databaser(message, returner=True)[1]['games']
    for game,stats in ans.items():
        await message.answer(f'Ваша статистика в игре  {game}\n'+
                             '\n'.join(f'{key} : {stats[key]}' for key in ['all_games','wins','loses']))

# @router.message(lambda message: message.text == 'change_number' or
#                                 databaser(message, returner=True)[1]['games']['change_number']['in_game'])
# async def change_number(message: Message):
#
#     await message.answer(ans)


@router.message()
async def send_echo(message: Message):
    try:
        await message.answer("База данных на ходится в разработке, зайдите попозже ")
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )
