from aiogram import Router, types
from aiogram.filters import Command

my_router = Router()

@my_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hello! Alexander y tebya small diK")
