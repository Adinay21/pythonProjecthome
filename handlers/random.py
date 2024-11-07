from aiogram import Router, types
from aiogram.filters import Command
from random import choice
from handlers.recept import recepts


random_router = Router()

@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    await message.answer(f'{choice(recepts)}')
