from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot_config import database


add_dish_router = Router()
add_dish_router.message.filter(F.from_user.id.in_(780722431))

class Dishes(StatesGroup):
    name = State()
    ingredients = State()
    price = State()

@add_dish_router.message(Command("newdish"), default_state)
async def new_dish(message: types.Message, state: FSMContext):
    print(message.from_user.id)
    await state.set_state(Dishes.name)
    await message.answer("Напишите название блюда")

@add_dish_router.message(Dishes.name)
async def new_dish(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Dishes.ingredients)
    await message.answer("Пропишите ингредиенты этого блюда")

@add_dish_router.message(Dishes.ingredients)
async def new_dish(message: types.Message, state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(Dishes.price)
    await message.answer("Задайте цену блюда")

@add_dish_router.message(Dishes.price)
async def new_dish(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)

    data = await state.get_data()
    print(data)
    database.execute(
        query="""
                INSERT INTO dishes(name, indredients, price)
                VALUES (?, ?, ?)
            """,
        params=(
            data["name"],
            data["ingredients"],
            data["price"]
        )
    )

    await state.set_state()
    await message.answer("Блюдо добавлено")