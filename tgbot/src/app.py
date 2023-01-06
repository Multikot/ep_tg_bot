import asyncio

from aiogram import types, executor
from aiogram.utils.exceptions import BadRequest
from aiogram.dispatcher.filters import Text

from services import services, BotService
from settings import bot, settings, dp

from logger import logger
from db import create_db
from markups import markups

class MainBot():

    @dp.message_handler(commands=['start'])
    @dp.message_handler(Text(equals=['start', 'Start', 'Main']))
    async def handle_start(message: types.Message, services: BotService = services):
        await message.answer(await services.get_start_answer(), reply_markup=await markups.get_main_menu())

    @dp.message_handler(Text(equals=['INFO', 'Info', 'info']))
    async def handle_info(message: types.Message, services: BotService = services):
        await message.answer(await services.get_info_answer(), reply_markup=await markups.get_info_menu())

    @dp.message_handler(Text(equals=['WAR', 'War', 'war']))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_war_answer())

    @dp.message_handler(Text(equals=['MYTH', 'Myth', 'myth']))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_myth_answer())

    @dp.message_handler(Text(equals=['EVENTS', 'Events', 'events']))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_event_answer())


def bot_start():
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as err:
        logger.critical(err)
    # await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logger.info('The bot start polling')
        bot_start()
    except Exception as err:
        logger.critical(err)
