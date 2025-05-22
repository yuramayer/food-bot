"""Check the message if it's food"""

from aiogram import Router, F
from aiogram.types import Message
from bot_back.gpt_funcs import estimate_nutrition
from bot_back.processing import process_food_estimation, dict2msg


food_router = Router()


@food_router.message(F.text)
async def check_food(message: Message):
    """User sends food, we estimate it"""
    food_message = message.text
    estimation, err_message = estimate_nutrition(food_message)

    if estimation is None:
        await message.answer(err_message)
        return
    checked_estimation, err_message = process_food_estimation(estimation)

    if checked_estimation is None:
        await message.answer(err_message)
        return

    msg_d = dict2msg(checked_estimation)

    await message.answer(f'Готовый словарь:\n{msg_d}')
