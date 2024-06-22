# Импорт необходимых библиотек и модулей
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from config import *  # Не забудь записать токен в переменную TOKEN_BOT в файле config.py =)


# Включить логирование на уровне INFO
logging.basicConfig(level=logging.INFO)


# Создать объект бота
bot = Bot(token=TOKEN_BOT)

# Создать диспетчер
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Отправить приветствие с форматированным именем пользователя
    await message.answer(f"Привет <b>{message.from_user.username}</b>!", parse_mode=ParseMode.HTML)


# Функция для запуска процесса поллинга новых обновлений
async def main():
    # Запустить процесс поллинга новых обновлений
    await dp.start_polling(bot)


# Если файл запущен как главный
if __name__ == "__main__":
    # Запустить процесс обновления в асинхронном режиме
    asyncio.run(main())
