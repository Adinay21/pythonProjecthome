from aiogram import Router, F, types
from aiogram.filters import Command
from datetime import timedelta

ban_router = Router()

bad_words = ["дурак", "тупой", "идиот"]



@ban_router.message(F.text)
async def check_bad_words(message: types.Message):
    for word in bad_words:
        if word in message.text.lower():
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id,
            )
            break

"ban 2d"
@ban_router.message(F.text.startswith("ban"))
async def ban_member(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Надо сделать реплай на чье-то сообщение")
    else:
        text = message.text
        id = message.reply_to_message.from_user.id
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=id,
            until_date=timedelta(hours=24)
        )



