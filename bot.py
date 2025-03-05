import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Укажите ваш токен, который получили от BotFather
TOKEN = "BOT_TOKEN"

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я эхо-бот. Отправь мне сообщение, и я повторю его!")

# Эхо-ответ на любое сообщение
@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

# Функция запуска бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

# Запускаем бота
if __name__ == "__main__":
    asyncio.run(main())
