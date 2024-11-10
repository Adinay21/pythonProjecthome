from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

review_router = Router()

# fsm = finite state mashine - конечный автомат

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.message(Command('review'))
async def opros(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await message.answer("Как вас зовут?")

@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Укажите свой номер:")

@review_router.message(RestourantReview.phone_number)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(RestourantReview.instagram_username)
    await message.answer("Укажите свой инстаграм:")

@review_router.message(RestourantReview.instagram_username)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Укажите свою дату почещения:")

@review_router.message(RestourantReview.visit_date)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(RestourantReview.food_rating)
    await message.answer("Как оцениваете качество еды?")

@review_router.message(RestourantReview.food_rating)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(RestourantReview.cleanliness_rating)
    await message.answer("Как оцениваете чистоту заведения?")

@review_router.message(RestourantReview.cleanliness_rating)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Дополнительные жалобы и комментарии:")

@review_router.message(RestourantReview.extra_comments)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer("Спасибо за оставленный отзыв!")
    data = await state.get_data()
    print(data)
    await state.clear()