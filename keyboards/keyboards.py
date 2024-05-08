from aiogram import types
from lexicon.lexicon_ru import LEXICON_RU

earth_key = types.KeyboardButton(text=LEXICON_RU['earth_button'])
astron_key = types.KeyboardButton(text=LEXICON_RU['astron_button'])

gravity_key = types.ReplyKeyboardMarkup(keyboard=[[astron_key, earth_key]], resize_keyboard=True)
