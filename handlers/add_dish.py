from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot_config import database


add_dish_router = Router()
# add_dish_router.message.filter(F.from_user.id == 780722431)

class Dishes(StatesGroup):
    name = State()
    ingredients = State()
    price = State()
    category = State()

class Categories(StatesGroup):
    name = State()

@add_dish_router.message(Command("newcategory"))
async def new_category(message: types.Message, state: FSMContext):
    await state.set_state(Categories.name)
    await message.answer("Напишите категорию блюда: ")

@add_dish_router.message(Categories.name)
async def new_category(message: types.Message, state: FSMContext):
    category = message.text
    database.execute(
        query="""
                    INSERT INTO categories(name)
                    VALUES (?)
                """,
        params=(category,)
    )

    await message.answer("Категория добавлена")
    await state.clear()

@add_dish_router.message(Command("newdish"))
async def new_dish(message: types.Message, state: FSMContext):
    await state.set_state(Dishes.name)
    await message.answer("Напишите название блюда")

@add_dish_router.message(Dishes.name)
async def new_dish(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Dishes.ingredients)
    await message.answer("Пропишите ингредиенты этого блюда")

@add_dish_router.message(Dishes.ingredients)
async def new_dish(message: types.Message, state: FSMContext):
    await state.update_data(ingredients=message.text)
    await state.set_state(Dishes.price)
    await message.answer("Задайте цену блюда")

@add_dish_router.message(Dishes.price)
async def new_dish(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    all_categories = database.fetch("SELECT * FROM categories")
    if not all_categories:
        await message.answer("Нет ни одной категории")
        state.clear()
        return
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text=categories["name"]) for categories in all_categories]
        ]
    )
    await state.set_state(Dishes.category)
    await message.answer("Задайте категорию блюда:", reply_markup=kb)

@add_dish_router.message(Dishes.category)
async def new_dish(message: types.Message, state: FSMContext):
    print(message.text)
    categories_id = database.fetch(
        query="SELECT id FROM categories WHERE name = ?",
        params=(message.text,)
    )
    if not categories_id:
        await message.answer("Вы напечатали неуществующую категорию")
        return
    await state.update_data(category=categories_id[0]["id"])
    data = await state.get_data()
    database.execute(
        query="""
            INSERT INTO dishes(name, ingredients, price, categories_id)
            VALUES (?, ?, ?, ?)
        """,
        params=(
            data["name"],
            data["ingredients"],
            data["price"],
            data["categories"]
        )
    )
    kb = types.ReplyKeyboardRemove()
    await message.answer("Блюдо добавлено", reply_markup=kb)



# @add_dish_router.message(Dishes.price)
# async def new_dish(message: types.Message, state: FSMContext):
#     await state.update_data(price=message.text)
#
#     data = await state.get_data()
#     print(data)
#     database.execute(
#         query="""
#                 INSERT INTO dishes(name, ingredients, price)
#                 VALUES (?, ?, ?)
#             """,
#         params=(
#             data["name"],
#             data["ingredients"],
#             data["price"]
#         )
#     )
#
#     await state.set_state()
#     await message.answer("Блюдо добавлено")