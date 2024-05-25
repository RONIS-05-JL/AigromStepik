from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType, MessageId
from CFG import BOT_TOKEN
import Change_number
import Data

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    Data.databaser(message)
    await message.answer("Привет! Я бот, который умеет отвечать на вопросы"
                         "Не хотите сыграть в игру ? Если да то напиши мне /game")


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    Data.databaser(message)
    await message.answer("Напиши мне что нибудь и в ответ я пришлю тебе твое сообщение ")


@dp.message()
async def send_echo(message: Message):
    idd, data = Data.databaser(message, returner=True)
    print(data['games']['in_game'])
    if data['games']['in_game'] or message.text in Change_number.patt['start']:
        ans = Change_number.numbers(data['games'], answer=message.text)
        Data.databaser(idd=id, id_data=data)
        await message.answer(ans)

    else:
        try:
            Data.databaser(message)
            await message.send_copy(chat_id=message.chat.id)
        except TypeError:
            await message.reply(
                text='Данный тип апдейтов не поддерживается '
                     'методом send_copy'
            )


if __name__ == '__main__':
    dp.run_polling(bot)
