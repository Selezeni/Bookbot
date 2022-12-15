from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon import LEXICON
from services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    bookmarks_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(
                            text=f'{button} - {book[button][:100]}',
                            callback_data=str(button)))
    bookmarks_kb.add(InlineKeyboardButton(
                            text=LEXICON['edit_bookmarks_button'],
                            callback_data='edit_bookmarks'),
                     InlineKeyboardButton(text=LEXICON['cancel'],
                                          callback_data='cancel'))
    return bookmarks_kb


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    bookmarks_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(
                    text=f"{LEXICON['del']} {button} - {book[button][:100]}",
                    callback_data=f"{button}del"))
    bookmarks_kb.add(InlineKeyboardButton(
                        text=LEXICON['cancel'],
                        callback_data="cancel"))

    return bookmarks_kb
