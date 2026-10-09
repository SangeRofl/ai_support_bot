import asyncio
from aiogram import Dispatcher, Bot
from config import settings
from aiogram.filters import Command
from aiogram.types import Message


dp = Dispatcher()


@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm your AI-SupportBot")


async def main():
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())