import aiohttp

from aiogram import types, Router, F

faq_router = Router()


@faq_router.callback_query(F.data == "help")
async def faq_handler(callback: types.CallbackQuery):
    url = "http://127.0.0.1:8000/api/faq/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()

    text = data[0]["answer"] if data else "Пока нет доступных ответов."

    await callback.message.delete()

    await callback.message.answer(text=text)
    await callback.answer()

