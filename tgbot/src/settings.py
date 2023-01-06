from aiogram.utils.exceptions import ValidationError
from aiogram import Bot, Dispatcher
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from logger import logger

load_dotenv()


class Settings(BaseModel):
    token: str = os.getenv('TOKEN')
    db_name: str = os.getenv('DB_NAME')

    class Config:
        env_file_encoding = 'utf-8'


settings = Settings()


class BotSettings():

    def get_bot(self):
        try:
            return Bot(token=settings.token)
        except ValidationError:
            logger.error('Token is invalid, message sending mode is disabled')

bot: Bot = BotSettings().get_bot()
dp: Dispatcher = Dispatcher(bot)
