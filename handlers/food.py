"""Check the message if it's food"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from bot_back.gpt_funcs import estimate_nutrition
from bot_back.processing import process_food_estimation, dict2msg
from states import NewFoodGPT
from keyboards.approve_kb import approve_buttons, get_approve_kb


food_router = Router()


@food_router.message(StateFilter(None), F.text)
async def check_food(message: Message, state: FSMContext):
    """User sends food, we estimate it"""
    food_message = message.text
    estimation, err_message = estimate_nutrition(food_message)

    if estimation is None:
        await message.answer(err_message)
        return
    checked_estimation, err_message = process_food_estimation(
        estimation, food_message)

    if checked_estimation is None:
        await message.answer(err_message)
        return

    await state.update_data(estimation=checked_estimation)
    msg_d = dict2msg(checked_estimation)

    await message.answer(f'Твоя еда:\n\n{msg_d}\n\nВсё верно?',
                         reply_markup=get_approve_kb())

    await state.set_state(NewFoodGPT.approved)


@food_router.message(NewFoodGPT.approved, F.text.in_(approve_buttons))
async def get_approve(message: Message, state: FSMContext):
    """User approves the dict with food"""

    user_message = message.text

    left_b, _ = approve_buttons

    if user_message == left_b:
        await message.answer('Жаль. Попробуем ещё раз')
        await state.clear()
        return

    await message.answer('Отлично. Запишем информацию')
    await state.clear()


@food_router.message(NewFoodGPT.approved)
async def wrong_approve(message: Message):
    """User sends wrong message - without keyboard"""

    await message.answer('Воспользуйся кнопками клавиатуры',
                         reply_markup=get_approve_kb())
