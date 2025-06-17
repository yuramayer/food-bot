"""State for the new food calo's typed by the user"""

# pylint: disable=too-few-public-methods

from aiogram.fsm.state import StatesGroup, State


class NewFoodManual(StatesGroup):
    """Food State by the user: got the calories & save it"""
    description = State()
    grams = State()
    calories = State()
    proteins = State()
    fats = State()
    carbs = State()
    approved = State()
