from aiogram.types import InlineKeyboardButton, WebAppInfo, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

guest_user_button = {"form": "📝 Анкета"}

def guest_kb():
    kb = InlineKeyboardBuilder()
    form_button = InlineKeyboardButton(text=guest_user_button["form"], web_app=WebAppInfo(url="https://forms.yandex.ru/cloud/66ea89be50569028a9df13e3/"))
    kb.row(form_button)

    return kb.as_markup(resize_keyboard=True)