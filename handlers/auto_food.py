"""Estimates the food calories with GPT & saves it"""

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from bot_back.gpt_funcs import estimate_nutrition
from bot_back.processing import process_food_estimation, dict2msg
from bot_back.cloud import save_food_entry_s3
from states import NewFoodGPT
from keyboards.approve_kb import approve_buttons, get_approve_kb


auto_food_router = Router()


@auto_food_router.message(StateFilter(None), F.text)
async def check_auto_food(message: Message, state: FSMContext):
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

    await state.update_data(
        description=checked_estimation.get('еда'),
        grams=checked_estimation.get('грамм'),
        calories=checked_estimation.get('калории'),
        proteins=checked_estimation.get('белки'),
        fats=checked_estimation.get('жиры'),
        carbs=checked_estimation.get('углеводы')
        )
    data = await state.get_data()
    msg_d = dict2msg(data)

    await message.answer(f'Твоя еда:\n\n{msg_d}\n\nВсё верно?',
                         reply_markup=get_approve_kb())

    await state.set_state(NewFoodGPT.approved)


@auto_food_router.message(NewFoodGPT.approved, F.text.in_(approve_buttons))
async def get_approve_auto_food(message: Message, state: FSMContext):
    """User approves the dict with food"""

    user_message = message.text

    left_b, _ = approve_buttons

    if user_message == left_b:
        await message.answer('Сколько грамм ты съел?',
                             reply_markup=ReplyKeyboardRemove())

        await state.clear()
        return

    food_dict = await state.get_data()
    save_food_entry_s3(food_dict)
    await state.clear()
    await message.answer('Я сохранил инфу в S3 💫',
                         reply_markup=ReplyKeyboardRemove())


@auto_food_router.message(NewFoodGPT.approved)
async def wrong_approve_auto_food(message: Message):
    """User sends wrong message - without keyboard"""

    await message.answer('Воспользуйся кнопками клавиатуры',
                         reply_markup=get_approve_kb())
