"""yes / no keyboard"""

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

approve_buttons = ('Нет', 'Да')


def get_approve_kb() -> ReplyKeyboardMarkup:
    """Creates the 'yes' / 'no' keyboard"""
    kb = ReplyKeyboardBuilder()
    for btn in approve_buttons:
        kb.button(text=btn)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
