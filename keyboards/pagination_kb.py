from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon import LEXICON


# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons: str):
    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    pagination_kb.row(*[InlineKeyboardButton(LEXICON[button] if button in LEXICON else button,
                        callback_data=button) for button in buttons])

    return pagination_kb
