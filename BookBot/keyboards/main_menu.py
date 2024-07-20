from aiogram import Bot
from aiogram.types import BotCommand

from BookBot.lexicon.lexicon import LEXICON_COMMANDS


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command=i, description=j) for i, j in LEXICON_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)
