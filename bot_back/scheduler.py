"""Scheduler that ask questions every /time/"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from bot_back.questions import ask_breakfast, ask_dinner, ask_supper


scheduler = AsyncIOScheduler()

scheduler.add_job(
    ask_breakfast,
    CronTrigger().from_crontab(
        expr='0 10 * * *',
        timezone=pytz.timezone('Europe/Moscow')),
    id='ask_breakfast'
)


scheduler.add_job(
    ask_dinner,
    CronTrigger().from_crontab(
        expr='0 15 * * *',
        timezone=pytz.timezone('Europe/Moscow')),
    id='ask_dinner'
)

scheduler.add_job(
    ask_supper,
    CronTrigger().from_crontab(
        expr='0 20 * * *',
        timezone=pytz.timezone('Europe/Moscow')),
    id='ask_supper'
)
