from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder


profile_router = Router()

@profile_router.callback_query(F.data == 'profile')
async def call_profile_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text='Вернуться назад', callback_data='back_to_menu')

    user_id = callback.message.from_user.id
    first_name = callback.from_user.first_name

    profile_text = (
        f"ℹ️ Информация о вашем профиле\n"
        f"👤 Имя: {first_name}\n"
        f"🆔 Твой ID: {user_id}"
    )
    await callback.message.delete()

    await callback.message.answer(
        text=profile_text,
        reply_markup=builder.as_markup()
    )


    await callback.answer()