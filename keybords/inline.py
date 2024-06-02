from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType)
from secondary_functions.second_functions import groupper
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.text_patterns import inline_text, inline_add_text, mech
from aiogram.types.web_app_info import WebAppInfo
from secondary_functions.second_functions import buttomer
import os

# buttons: list[KeyboardButton] = [KeyboardButton(text=f'{inline_text[i]}') for i in range(len(inline_text))]


buttons1: list[KeyboardButton] = [*groupper(buttomer(inline_text), 4)]

keybord_under = ReplyKeyboardMarkup(keyboard=buttons1, resize_keyboard=True)

kb_builder = ReplyKeyboardBuilder()
kb_builder.row(*buttomer(inline_text), width=3)
kb_builder.add(*buttomer(inline_add_text))
kb_builder.adjust(1, 4)

mech_kb = ReplyKeyboardBuilder()
mech_kb.row(*buttomer(mech), width=2)

special_kb = ReplyKeyboardBuilder()
cnt_bld = KeyboardButton(text='Send phone number', request_contact=True)
geo_bld = KeyboardButton(text='Send location', request_location=True)
poll_bld = KeyboardButton(text='Create poll', request_poll=KeyboardButtonPollType(type='regular', is_anonymous=False))

special_kb.row(cnt_bld, geo_bld, poll_bld, width=1)
special_keyboard = special_kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

web_app_btn = KeyboardButton(text='Start Web App', web_app=WebAppInfo(url="https://stepik.org/"))
web_app_btn2 = KeyboardButton(text='Video', web_app=WebAppInfo(url="https://www.youtube.com/"))
web_app_keyboard = ReplyKeyboardMarkup(keyboard=[[web_app_btn], [web_app_btn2]], resize_keyboard=True)

mini_game_keybords = ReplyKeyboardBuilder()
mini_game_keybords.row(*buttomer(['change_number', 'rock']), width=3)
