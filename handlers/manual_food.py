"""Save the food calories by the manual"""

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from bot_back.processing import dict2msg
from bot_back.cloud import save_food_entry_s3
from states import NewFoodManual
from keyboards.approve_kb import approve_buttons, get_approve_kb


manual_food_router = Router()


@manual_food_router.message(NewFoodManual.grams)
async def save_grams_ask_calos(message: Message, state: FSMContext):
    """User asks the calories & saves the grams"""

    user_grams = message.text

    await state.update_data(
        grams=user_grams
        )
    await message.answer('Сколько калорий было в твоём блюде?')
    await state.set_state(NewFoodManual.calories)


@manual_food_router.message(NewFoodManual.calories)
async def save_calos_ask_proteins(message: Message, state: FSMContext):
    """User saves the calories & asks the proteins"""

    user_calories = message.text

    await state.update_data(
        calories=user_calories
        )
    await message.answer('Сколько белков?')
    await state.set_state(NewFoodManual.proteins)


@manual_food_router.message(NewFoodManual.proteins)
async def save_proteins_ask_fats(message: Message, state: FSMContext):
    """User saves the proteins & asks the fats of the food"""

    user_proteins = message.text

    await state.update_data(
        proteins=user_proteins
        )
    await message.answer('Сколько жиров?')
    await state.set_state(NewFoodManual.fats)


@manual_food_router.message(NewFoodManual.fats)
async def save_fats_ask_carbs(message: Message, state: FSMContext):
    """User saves the fats & asks the carbs of the food"""

    user_fats = message.text

    await state.update_data(
        fats=user_fats
        )
    await message.answer('Сколько углеводов?')
    await state.set_state(NewFoodManual.carbs)


@manual_food_router.message(NewFoodManual.carbs)
async def save_carbs_ask_approve(message: Message, state: FSMContext):
    """User saves the carrbs & repeat all the info"""

    user_carbs = message.text

    await state.update_data(
        carbs=user_carbs
        )

    data = await state.get_data()
    msg_d = dict2msg(data)

    await message.answer(f'Твоя еда:\n\n{msg_d}\n\nВсё верно?',
                         reply_markup=get_approve_kb())

    await state.set_state(NewFoodManual.approved)


@manual_food_router.message(
        NewFoodManual.approved, F.text.in_(approve_buttons))
async def get_approve_manual_food(message: Message, state: FSMContext):
    """User approves the dict with manual food"""

    user_message = message.text

    left_b, _ = approve_buttons

    if user_message == left_b:
        await message.answer('Жаль 😢',
                             reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    food_dict = await state.get_data()
    save_food_entry_s3(food_dict)
    await state.clear()
    await message.answer('Я сохранил инфу в S3 💫',
                         reply_markup=ReplyKeyboardRemove())


@manual_food_router.message(NewFoodManual.approved)
async def wrong_approve_manual_food(message: Message):
    """User sends wrong message - without keyboard"""

    await message.answer('Воспользуйся кнопками клавиатуры',
                         reply_markup=get_approve_kb())
