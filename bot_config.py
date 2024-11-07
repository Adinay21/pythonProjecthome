from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
from aiogram import Router, types
from aiogram.filters import Command

token = dotenv_values(".env")["TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

