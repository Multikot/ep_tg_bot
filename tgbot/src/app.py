import asyncio

from aiogram import types, executor
from aiogram.utils.exceptions import BadRequest
from aiogram.dispatcher.filters import Text

from services import services, BotService
from settings import bot, settings, dp

from logger import logger
from db import create_db
from markups import markups

class MainMenu():
    """Here is methods about main menu. If you include new method to main menu, do it here."""

    @dp.message_handler(commands=['start'])
    @dp.message_handler(Text(equals=['start', 'Start', 'Main']))
    async def handle_start(message: types.Message, services: BotService = services):
        await message.answer(await services.get_start_answer(), reply_markup=await markups.get_main_menu())

    @dp.message_handler(commands=['info'])
    @dp.message_handler(Text(equals=['INFO', 'Info', 'info']))
    async def handle_info(message: types.Message, services: BotService = services):
        await message.answer(await services.get_info_answer(), reply_markup=await markups.get_info_menu())

    @dp.message_handler(commands=['war'])
    @dp.message_handler(Text(equals=['WAR', 'War', 'war']))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_war_answer(), reply_markup=await markups.get_war_menu())

    @dp.message_handler(commands=['myth'])
    @dp.message_handler(Text(equals=['MYTH', 'Myth', 'myth']))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_myth_answer())

    @dp.message_handler(commands=['events'])
    @dp.message_handler(Text(equals=['EVENTS', 'Events', 'events']))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_event_answer())


class WarMenu():

    @dp.message_handler(commands=['mim'])
    @dp.message_handler(Text(equals=['MIM', 'mim', 'Mim']))
    async def handle_mim(message: types.Message, services: BotService = services):
        await message.answer(await services.get_mim_answer())


async def until_bo_start(dispatcher):
    await markups.set_default_commands(dispatcher=dispatcher)


def bot_start():
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=until_bo_start)
    except Exception as err:
        logger.critical(err)
    # await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logger.info('The bot start polling')
        bot_start()
    except Exception as err:
        logger.critical(err)
