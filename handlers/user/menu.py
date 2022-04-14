from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("menu"))
async def shoew_menu(message: Message):
    await message.answer("choose one wine for order", reply_markup=menu)

@dp.message_handler(Text(equals=["Toukas", "Shavenil", "Tarantello"]))
async def get_food(message: Message):
    await message.answer(f"Choosen {message.text}. Thanks for order", reply_markup=ReplyKeyboardRemove())