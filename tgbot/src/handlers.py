from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from services import services, BotService
from markups import markups 

class MainMenu():
    """Here is methods about main menu. If you want include new method to main menu, do it here."""

    async def handle_start(message: types.Message, services: BotService = services):
        await message.answer(await services.get_start_answer(), reply_markup=await markups.get_main_menu())

    async def handle_info(message: types.Message, services: BotService = services):
        await message.answer(await services.get_info_answer(), reply_markup=await markups.get_info_menu())

    async def handle_war(message: types.Message, services: BotService = services):
        await message.answer(await services.get_war_answer(), reply_markup=await markups.get_war_menu())

    async def handle_myth(message: types.Message, services: BotService = services):
        await message.answer(await services.get_myth_answer())

    async def handle_events(message: types.Message, services: BotService = services):
        await message.answer(await services.get_event_answer())

class WarMenu():
    """Here is methods about war menu. If you want include new method to main menu, do it here."""

    async def handle_mim(message: types.Message, services: BotService = services):
        await message.answer(await services.get_mim_answer())


async def register_war_menu_handlers(dp: Dispatcher) -> None:
    """If you extended war menu services, include handlers here."""

    dp.register_message_handler(WarMenu.handle_mim, commands=['mim', 'Mim', 'MIM'])
    dp.register_message_handler(WarMenu.handle_mim, Text(equals=['mim', 'Mim', 'MIM']))


async def register_main_menu_handlers(dp: Dispatcher) -> None:
    """If you extended main menu services, include handlers here."""

    dp.register_message_handler(MainMenu.handle_start, commands=['start', 'Start', 'START'], state='*')
    dp.register_message_handler(MainMenu.handle_start, Text(equals=['start', 'Start', 'START', 'Main']), state='*')

    dp.register_message_handler(MainMenu.handle_info, commands=['info', 'Info', 'INFO'], state='*')
    dp.register_message_handler(MainMenu.handle_info, Text(equals=['info', 'Info', 'INFO']))

    dp.register_message_handler(MainMenu.handle_war, commands=['war', 'War', 'WAR'], state='*')
    dp.register_message_handler(MainMenu.handle_war, Text(equals=['war', 'War', 'WAR']))

    dp.register_message_handler(MainMenu.handle_myth, commands=['myth', 'Myth', 'MYTH'])
    dp.register_message_handler(MainMenu.handle_myth, Text(equals=['myth', 'Myth', 'MYTH']))

    dp.register_message_handler(MainMenu.handle_events, commands=['events', 'Events', 'EVENTS'])
    dp.register_message_handler(MainMenu.handle_events, Text(equals=['events', 'Events', 'EVENTS']))

