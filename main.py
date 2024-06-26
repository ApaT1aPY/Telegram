import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from config import *


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.delete()
    await message.answer(f"Привет <b>{message.from_user.username}</b>!", parse_mode=ParseMode.HTML)
    await asyncio.sleep(30)
    await bot.delete_message(message.chat.id, message.message_id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())