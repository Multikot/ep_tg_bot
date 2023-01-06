import asyncio
from aiogram import Dispatcher

from handlers import register_main_menu_handlers
from settings import bot, dp
from logger import logger
from markups import markups


async def generate_menu_until_to_start(dp: Dispatcher):
    await markups.set_default_commands(dispatcher=dp)


async def bot_start(dp: Dispatcher):
    try:
        await generate_menu_until_to_start(dp)
        await register_main_menu_handlers(dp)
        await dp.start_polling(bot)
    except Exception as err:
        logger.critical(err)


if __name__ == "__main__":
    dp: Dispatcher = dp
    try:
        logger.info('The bot start polling')
        asyncio.run(bot_start(dp))
    except KeyboardInterrupt:
        logger.error('you are stoped polling')
    except Exception as err:
        logger.critical(err)
