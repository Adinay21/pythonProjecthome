from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
from aiogram import Router, types
from aiogram.filters import Command

from database.database import Database

token = dotenv_values(".env")["TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

database = Database("database.sqlite")