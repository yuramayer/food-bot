"""Messages to ask with scheduler"""

from bot import bot
from config.conf import admins_ids


async def ask_breakfast():
    """Ask user what did he eat for the breakfast"""

    for admin_id in admins_ids:
        await bot.send_message(admin_id, "Что ты позавтракал?")


async def ask_dinner():
    """Ask user what did he eat for the dinner"""

    for admin_id in admins_ids:
        await bot.send_message(admin_id, "Что ты поел на обед?")


async def ask_supper():
    """Ask user what did he eat for the supper"""

    for admin_id in admins_ids:
        await bot.send_message(admin_id, "Что ты поел на ужин?")
