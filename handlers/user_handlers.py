from aiogram import Router, F
from aiogram.filters import Command, CommandStart, KICKED, ChatMemberUpdatedFilter
from lexicon.text_patterns import LexRU, inline_text,inline_add_text
from keybords.inline import keybord_under, kb_builder, mech_kb, special_keyboard
from aiogram.types import (ReplyKeyboardRemove, Message, ChatMemberUpdated, FSInputFile)
from Database.Data import databaser
from keybords.inline import web_app_keyboard

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')


@router.message(CommandStart())
async def process_start_command(message: Message):
    databaser(message)
    await message.answer(text=LexRU['start'].format(message.from_user.first_name), reply_markup=special_keyboard)
    # await message.answer(LexRU['start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    databaser(message)
    await message.answer(LexRU['help'])


@router.message(Command(commands='available_instructions'))
async def process_game_command(message: Message):
    databaser(message)
    await message.answer(text='Вот список доступных инструкций и услуг',
                         reply_markup=kb_builder.as_markup(resize_keyboard=True))


@router.message(Command(commands='web_app'))
async def process_web_app__command(message: Message):
    await message.answer(text='Testing web app features', reply_markup=web_app_keyboard)


@router.message(lambda message: message.text in inline_text+inline_add_text)
async def for_selecotor_answer(message: Message):
    databaser(message)
    if message.text == 'Автомеханики на час':
        await message.answer_photo(photo=FSInputFile('Database/20191201_004844(0).jpg')
                                   ,reply_markup=ReplyKeyboardRemove())
        await message.answer(text='Вот доступные слесари ,кого из них хотите?', reply_markup=mech_kb.as_markup(
            resize_keyboard=True))
    else:
        await message.answer(text='Хорошо сейчас предоставлю вам информацию ', reply_markup=ReplyKeyboardRemove())
