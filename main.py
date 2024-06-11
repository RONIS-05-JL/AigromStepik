from aiogram import Dispatcher, Bot
from Configurations.config1 import config_loader
from handlers import game_handlers, user_handlers
import asyncio
from keybords.menu_commands import set_main_menu
import logging
from middlewares.inner_middlewares  import *
from middlewares.outer_middlewares import *


logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] #%(levelname) -8s%(filename)s:%(lineno)s:%(message)s')
logger=logging.getLogger(__name__)
config = config_loader('.env')



async def main() -> None:
    bot = Bot(token=config.tg_bot.token)
    superadmin = config.tg_bot.admin_ids[0]
    dp = Dispatcher()
    dp.startup.register(set_main_menu)
    dp.include_router(user_handlers.router)
    dp.include_router(game_handlers.router)
    dp.update.outer_middleware(FirstOuterMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
