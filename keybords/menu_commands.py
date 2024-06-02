from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

commands = {'/help': 'Справка по работе бота', '/support': 'Поддержка', '/contacts': 'Другие способы связи',
            '/payments': 'Платежи', '/mini_games': 'мини игры', '/games_stats': 'статистика по играм',
            '/open_list_of_instructions': 'Доступные инструкции', '/web_apps': 'доступные приложения'}


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command=command, description=description) for command, description in commands.items()]

    await bot.set_my_commands(main_menu_commands)
