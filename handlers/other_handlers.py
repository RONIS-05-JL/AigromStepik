from aiogram import Router, F
from aiogram.types import Message
from lexicon.text_patterns import LexRU, new_commands
from games import Change_number
from Database.Data import databaser
from aiogram.filters import Filter, Command
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message,
                           ReplyKeyboardRemove, ReplyKeyboardMarkup)

router = Router()





@router.message(lambda message:message.text not in new_commands)
async def send_echo(message: Message):
    databaser(message)
    idd, data = databaser(message, returner=True)
    if data['games']['in_game'] or message.text in Change_number.patt['start']:
        ans = Change_number.numbers(data['games'], answer=message.text)
        databaser(id=id, id_data=data)
        await message.answer(ans)

    try:
        await message.answer("База данных на ходится в разработке, зайдите попозже ")
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )
