from aiogram import F, Router, types
from aiogram.filters import Command

from pprint import pprint

from bot_config import database

dishes_router = Router()



@dishes_router.message(Command("dishes"))
async def show_all_books(message: types.Message):
    all_categories = database.fetch("SELECT * FROM categories")
    if not all_categories:
        await message.answer("Нет ни одной категории")
        return
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text=categories["name"]) for categories in all_categories]
        ]
    )
    await message.answer("Выберите категорию блюд", reply_markup=kb)

def check_categories(message: types.Message):
    print("inside categories filter")
    all_categories = database.fetch(
        query="SELECT name FROM categories WHERE name = ?", #
        params=(message.text,)
    )
    if all_categories:
        return True

    return False


@dishes_router.message(check_categories)
async def show_books_by_genre(message: types.Message):
    all_dishes = database.fetch(
        query="SELECT * FROM dishes JOIN categories ON dishes.categories_id = categories.id WHERE categories.name = ?",
        params=(message.text, )
    )
    pprint(all_dishes)
    if not all_dishes:
        await message.answer("Извините, нет данной категории")
        return
    await message.answer("Блюда из нашего меню:")
    for dish in all_dishes:
        await message.answer(f"Название: {dish['name']}\nЦена: {dish['price']}")






# @dishes_router.message(Command("dishes"))
# async def show_all_dishes(message: types.Message):
#     dishes = database.fetch(
#         query="SELECT * FROM dishes"
#     )
#     pprint(dishes)
#     await message.answer("Блюда из нашего меню")
#     for dish in dishes:
#         await message.answer(f"Название: {dish['name']} - {dish['price']}")