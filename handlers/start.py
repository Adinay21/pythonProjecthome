from aiogram import Router, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f"Здравствуйте, {name}, приглашлаем в наше заведение"
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наш сайт",
                    url="https://taplink.cc/yabooblik"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Наш инстаграм",
                    url="https://www.instagram.com/ya_booblik/"
                )
            ]
        ]
    )
    await message.answer(msg, reply_markup=kb)
