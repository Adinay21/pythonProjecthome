from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot_config import database

review_router = Router()



class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.callback_query(F.data == "review")
async def process(cb: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await cb.message.answer("Как вас зовут?")

@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Укажите свой номер:")

@review_router.message(RestourantReview.phone_number)
async def process_age(message: types.Message, state: FSMContext):
    number = message.text
    if number.isdigit():
        await message.answer("Вводите только цифры")
        return
    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.instagram_username)
    await message.answer("Укажите свой инстаграм:")

@review_router.message(RestourantReview.instagram_username)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(instagram_username=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Укажите свою дату почещения:")

@review_router.message(RestourantReview.visit_date)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestourantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1"),
                types.KeyboardButton(text="2"),
                types.KeyboardButton(text="3"),
                types.KeyboardButton(text="4"),
                types.KeyboardButton(text="5")
            ]
        ]
    )
    await message.answer("Как оцениваете качество еды?", reply_markup=kb)

@review_router.message(RestourantReview.food_rating, F.text.in_(["1", "2", "3", "4", "5"]))
async def process_gender(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await state.update_data(food_rating=message.text)
    await state.set_state(RestourantReview.cleanliness_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1"),
                types.KeyboardButton(text="2"),
                types.KeyboardButton(text="3"),
                types.KeyboardButton(text="4"),
                types.KeyboardButton(text="5"),
                types.KeyboardButton(text="6"),
                types.KeyboardButton(text="7"),
                types.KeyboardButton(text="8"),
                types.KeyboardButton(text="9"),
                types.KeyboardButton(text="10")
            ]
        ]
    )
    await message.answer("Как оцениваете чистоту заведения?", reply_markup=kb)

@review_router.message(RestourantReview.cleanliness_rating, F.text.in_(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]))
async def process_gender(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Дополнительные жалобы и комментарии:", reply_markup=kb)

@review_router.message(RestourantReview.extra_comments)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("Спасибо за оставленный отзыв!")
    data = await state.get_data()
    print(data)

    database.execute(
        query="""
        INSERT INTO survey_results (name, phone_number, instagram_username, visit_date, food_rating, cleanliness_rating, extra_comments)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        params=(data["name"], data["phone_number"], data["instagram_username"], data["visit_date"],
                data["food_rating"], data["cleanliness_rating"], data["extra_comments"]),
    )


    await state.clear()