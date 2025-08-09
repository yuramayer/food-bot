"""Bot reacts to the commands for the non-admins"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from filters.admin_checker import NotAdmin
from config.conf import admins_ids


start_admin_router = Router()
start_admin_router.message.filter(
    NotAdmin(admins_ids)
)


@start_admin_router.message(Command('start'))
@start_admin_router.message(F.text)
async def plug(message: Message):
    """Message to the non-useres"""
    msg = (
        'Бот доступен только для администраторов! 🙅🏼‍♀️'
        '\n\nРазработчик: <b>@botrqst</b>'
    )
    await message.answer(msg)
