

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot.routers.profile import profile_router
from src.bot.routers.faq import faq_router

my_router = Router()

my_router.include_router(profile_router)
my_router.include_router(faq_router)


def start_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text='Профиль', callback_data='profile')
    builder.button(text="🛍 Каталог", callback_data='catalog')
    builder.button(text="❓ Помощь", callback_data='help')
    builder.adjust(2)
    return builder.as_markup()

@my_router.message(Command("start"))
async def start_handler(message: types.Message):
    gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDk1aW14cWVkazIwM3hmNDRxZjlyMWxlZW8ydDFoeDVwYTJwbHpvaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/exUgjvyJF451IGaRpH/giphy.gif'
    await message.answer_animation(
        animation = gif_url,
        caption='Hello! I\'m your AI-SupportBot',
        reply_markup=start_menu()
    )

@my_router.callback_query(F.data == 'back_to_menu')
async def back_to_menu_handler(callback: types.CallbackQuery):
    gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDk1aW14cWVkazIwM3hmNDRxZjlyMWxlZW8ydDFoeDVwYTJwbHpvaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/exUgjvyJF451IGaRpH/giphy.gif'
    await callback.message.answer_animation(
        animation=gif_url,
        caption='Hello! I\'m your AI-SupportBot',
        reply_markup=start_menu()
    )

    await callback.message.delete()
    await callback.answer()

