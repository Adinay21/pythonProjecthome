import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
from aiogram.filters import Command
from random import choice

token = dotenv_values(".env")["TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
names = ['Борис', 'Арина', 'Айзирек', 'Даниель', 'Фатима', 'Том']



@dp.message(Command("start"))
async def start(message: types.Message):
    name = message.from_user.first_name
    msg = f"Привет, {name}"
    await message.answer(msg)

@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    await message.answer(f"Ваши данные: \n id: {message.from_user.id} "
                         f"\n username: {message.from_user.username}"
                         f"\n first_name: {message.from_user.first_name}")

@dp.message(Command("random"))
async def random(message: types.Message):
    await message.answer(f'{choice(names)}')



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
