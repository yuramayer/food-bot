"""Starting Telegram bot app"""

import asyncio
from bot import bot, dp
from utils.starting import on_startup
from handlers import start_router, food_router


async def main():
    """Bot startup function"""
    dp.include_routers(start_router, food_router)
    dp.startup.register(on_startup)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
