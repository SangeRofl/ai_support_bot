import aiohttp

from aiogram import types, Router, F
from aiogram.dispatcher.middlewares import data
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

faq_router = Router()


@faq_router.callback_query(F.data == "help")
async def faq_handler(callback: types.CallbackQuery):
    url = "http://127.0.0.1:8000/api/v1/faq/"
    builder = InlineKeyboardBuilder()


    #подумать как перенести логику

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    question = data[0]['question']
    text = data[0]['answer']

    await callback.message.delete()

    await callback.message.answer(
        text=text
    )

