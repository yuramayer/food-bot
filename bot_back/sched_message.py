"""Methods with messaging user every /time/"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from bot import bot
from config.conf import admins_ids


async def ask_food():
    """Test function asking what admin has eaten"""

    for admin_id in admins_ids:
        await bot.send_message(admin_id, "Что ты съел?")


scheduler = AsyncIOScheduler()

scheduler.add_job(
    ask_food,
    CronTrigger().from_crontab(
        expr='* * * * *',
        timezone=pytz.timezone('Europe/Moscow'))
)
