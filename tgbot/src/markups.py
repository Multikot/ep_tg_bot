from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, BotCommand
from aiogram import Dispatcher


class MarkUp():

    def __init__(self) -> None:

        self.btn_info = KeyboardButton('Info')
        self.btn_main = KeyboardButton('Main')

        self.btn_war = KeyboardButton('WAR')
        self.btn_events = KeyboardButton('EVENTS')
        self.btn_myth_titan = KeyboardButton('MYTH')

        self.btn_donation = KeyboardButton('Donation')
        self.btn_feedback = KeyboardButton('Feedback')

        self.btn_mim_center = KeyboardButton('Mim')

    async def get_info_menu(self):
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            self.btn_feedback, self.btn_donation, self.btn_main
            )

    async def get_main_menu(self):
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            self.btn_events, self.btn_war, self.btn_myth_titan, self.btn_info
        )

    async def get_war_menu(self):
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            self.btn_mim_center, self.btn_main
        )

    async def set_default_commands(self, dispatcher: Dispatcher):
        
        commands = [
            BotCommand('start', 'run bot'),
            BotCommand('war', 'war menu'),
            BotCommand('events', 'events menu'),
            BotCommand('myth', 'myth titan menu'),
            BotCommand('info', 'about authors')
        ]
        return await dispatcher.bot.set_my_commands(commands=commands)


markups = MarkUp()
