from aiogram import Dispatcher,Bot
from aiogram.filters import Command
from aiogram.types import Message
from config1 import config_loader
from Modular_bot.games import Change_number
from Modular_bot.Databse import Data

# from keyboards.main_menu import set_main_menu

config = config_loader('.env')


bot_token = config.tg_bot.token
bot=Bot(token=bot_token)
superadmin = config.tg_bot.admin_ids[0]
dp = Dispatcher()

some_var_1=1
some_var_2="Некоторый текст"

dp.workflow_data.update({'my_int_var': some_var_1, 'my_text_var': some_var_2})

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message,my_int_var,my_text_var):
    Data.databaser(message)
    await message.answer(text=f"Привет {message.from_user.full_name}")
    await message.answer(text=my_text_var)
    await message.answer("Хули надо ?")


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
        Data.databaser(idd = id, id_data=data)
        await message.answer(ans)

    else:
        try:
            Data.databaser(message)
            await message.answer("Ебать ты хуйню спросил ")
        except TypeError:
            await message.reply(
                text='Данный тип апдейтов не поддерживается '
                     'методом send_copy'
            )


if __name__ == '__main__':
    dp.run_polling(bot)
