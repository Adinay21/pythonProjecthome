from aiogram import F, Router, types
from aiogram.filters import Command

from pprint import pprint

from bot_config import database

dishes_router = Router()

@dishes_router.message(Command("dishes"))
async def show_all_dishes(message: types.Message):
    dishes = database.fetch(
        query="SELECT * FROM dishes"
    )
    pprint(dishes)
    await message.answer("Блюда из нашего меню")
    for dish in dishes:
        await message.answer(f"Название: {dish['name']} - {dish['price']}")