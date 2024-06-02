from aiogram import Dispatcher, Bot
from Configurations.config1 import config_loader
from handlers import other_handlers, user_handlers
import asyncio


config = config_loader('.env')


async def main() -> None:
    bot = Bot(token=config.tg_bot.token)
    superadmin = config.tg_bot.admin_ids[0]
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
