"""State for the new food calo's from ChatGPT"""

# pylint: disable=too-few-public-methods

from aiogram.fsm.state import StatesGroup, State


class NewFoodGPT(StatesGroup):
    """New food State: estimates the calories & save it"""
    description = State()
    grams = State()
    calories = State()
    proteins = State()
    fats = State()
    carbs = State()
    approved = State()
