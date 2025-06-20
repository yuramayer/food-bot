"""Methods running when the bot is starting"""

from bot import bot
from config.conf import admins_ids
from bot_back.scheduler import scheduler


async def on_startup():
    """When bot is started, check db & send message to the admins"""

    for admin_id in admins_ids:
        await bot.send_message(admin_id, 'Бот включён 😎')

    scheduler.start()
