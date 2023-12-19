from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from states.user import *
from main.commands import *
from keyboards.default.user import *
from loader import dp
from utils.chacker import *

# @dp.message_handler(CommandStart())
# async def start_hendler(message: types.Message):
#     chanel = await check(user_id=message.chat.id)
#     if chanel:
#         if await get_user(message.chat.id):
#             text = "Xush kelibsiz"
#             await message.answer(text=text, reply_markup=shop_menu)
#         else:
#             text = "Assalomu Alaykum. Ismingizni kirirting"
#             await RegisterState.full_name.set()
#             await message.answer(text=text)
#     else:
#         text = "siz oldin bu botga a'zo bo'lishingiz kerak"
#         await message.answer(text=text, reply_markup=channel_keyboard)


@dp.message_handler(CommandStart())
async def start_hendler(message: types.Message):
    if await get_user(message.chat.id):
        text = "Xush kelibsiz"
        await message.answer(text=text, reply_markup=shop_menu)
    else:
        text = "Assalomu Alaykum. Ismingizni kirirting"
        await RegisterState.full_name.set()
        await message.answer(text=text)


@dp.message_handler(state=RegisterState.full_name)
async def f_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Telefon raqamingizni bering"
    await RegisterState.phone_number.set()
    await message.answer(text=text, reply_markup=phone_number)


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def f_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    user = await add_user(data=data,chat_id=message.chat.id)
    if user:
        text = "Accountshpga xush kelibsiz"
    else:
        text = "Botda nosozlik bor"
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()
