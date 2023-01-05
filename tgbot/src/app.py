from services import services, BotService
from settings import bot, settings, dp
import asyncio
from aiogram import types
from aiogram.utils.exceptions import BadRequest
from aiogram.dispatcher.filters import Text
from db import create_db
import markups

class MainBot():

    @dp.message_handler(commands=['start'])
    @dp.message_handler(Text(equals=['start', 'Start', 'Main']))
    async def handle_start(message: types.Message, services: BotService = services):
        await message.answer(await services.get_start_answer(), reply_markup=markups.main_menu)

    @dp.message_handler(Text(equals='Info'))
    async def handle_info(message: types.Message, services: BotService = services):
        await message.answer(await services.get_info_answer(), reply_markup=markups.info_menu)

    @dp.message_handler(Text(equals='WAR'))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_war_answer())

    @dp.message_handler(Text(equals='MYTH'))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_myth_answer())

    @dp.message_handler(Text(equals='EVENTS'))
    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_event_answer())


async def bot_start():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(bot_start())
