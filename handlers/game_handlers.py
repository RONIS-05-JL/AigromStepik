from aiogram import Router, F
from aiogram.types import Message
from lexicon.text_patterns import LexRU, new_commands
from games import Change_number, rock
from Database.Data import databaser
from aiogram.filters import Filter, Command
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message,
                           ReplyKeyboardRemove, ReplyKeyboardMarkup)
from keybords.inline import web_app_keyboard, mini_game_keybords

router = Router()


@router.message(Command(commands='mini_games'))
async def mini_games(message: Message):
    await message.answer(text='Выберите игру', reply_markup=mini_game_keybords.as_markup(resize_keyboard=True))


@router.message(lambda message: message.text in ['rock'] + rock.list_items)
async def rock_games(message: Message):
    ans = rock.rock_game(message)

    await message.answer(text=ans, reply_markup = rock.rock_btn.as_markup(resize_keyboard=True))

@router.message(F.text == 'change_number')
async def change_number(message: Message):
    idd, data = databaser(message, returner=True)

    ans = Change_number.numbers(data['games'], answer=message.text)
    databaser(id=id, id_data=data)
    await message.answer(ans)

@router.message()
async def send_echo(message: Message):
    try:
        await message.answer("База данных на ходится в разработке, зайдите попозже ")
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )
