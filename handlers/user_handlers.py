from copy import deepcopy

from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from database.database import user_dict_template, users_db
from keyboards.bookmarks_kb import (create_bookmarks_keyboard, create_edit_keyboard)
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon import LEXICON
from services.file_handling import book


async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


async def process_beginning_command(message: Message):
    users_db[message.from_user.id]['page'] = 1
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(text=text,
                         reply_markup=create_pagination_keyboard('backward',
                                                                 f"{users_db[message.from_user.id]['page']}/{len(book)}",
                                                                 'forward'))







def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_beginning_command, commands=['beginning'])
