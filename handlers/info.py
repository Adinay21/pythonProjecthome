from aiogram import Router, types
from aiogram.filters import Command


info_router = Router()

@info_router.message(Command("myinfo"))
async def myinfo(message: types.Message):
    await message.answer(f"Ваши данные: \n id: {message.from_user.id} "
                         f"\n username: {message.from_user.username}"
                         f"\n first_name: {message.from_user.first_name}")