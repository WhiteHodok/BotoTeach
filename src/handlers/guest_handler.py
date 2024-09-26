from config import supabase
from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, WebAppData
from config import bot_settings
from src.keyboards.guest_keyboard import guest_kb
from src.repo.UserDataRepo import UserDataRepository
from src.states.guest_states import Guest
from src.phrases import START

guest_router = Router()


user_repo = UserDataRepository(supabase)


@guest_router.message(CommandStart())
async def guest_start(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await state.clear()
    user_repo.update_field(chat_id, "chat_id", chat_id)
    await message.answer(START, reply_markup=guest_kb())
    await state.set_state(Guest.guest_main_room)
