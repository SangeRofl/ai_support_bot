import asyncio
from aiogram import Dispatcher, Bot
from src.config import settings
from routers.command_start import my_router as start


dp = Dispatcher()

dp.include_router(start)


async def main():
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())