from aiogram import Dispatcher, Bot
from Configurations.config1 import config_loader
from handlers import game_handlers, user_handlers
import asyncio

from Database.Data import databaser


config = config_loader('.env')


async def main() -> None:
    bot = Bot(token=config.tg_bot.token)
    superadmin = config.tg_bot.admin_ids[0]
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(game_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
