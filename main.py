import asyncio

import logging
from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.recept import recept_router
from handlers.random import random_router
from handlers.info import info_router
from handlers.review_dialog import review_router
from handlers.add_dish import add_dish_router
from handlers.dishes import dishes_router




async def main():
    database.create_tables()
    dp.include_router(start_router)
    dp.include_router(recept_router)
    dp.include_router(random_router)
    dp.include_router(info_router)
    dp.include_router(review_router)
    dp.include_router(add_dish_router)
    dp.include_router(dishes_router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())