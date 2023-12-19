from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import *
from main.commands import *
from keyboards.default.user import *
from keyboards.inline.user_shop import *
from loader import dp


@dp.message_handler(text="👤 Profil")
async def Profil_hendler(message: types.Message):
    user = await get_user(message.chat.id)
    for i in user:
        text = (f"ISM: {i['full_name']} \n"
                f"Telefon Raqam: {i['phone_number']}\n")
        await message.answer(text=text, reply_markup=upd_profile)


@dp.callback_query_handler(text="Update")
async def Profil_hendler(call: types.CallbackQuery):
    text = "Ismingizni kiriting!"
    await call.message.answer(text=text)
    await UpdProfilState.full_name.set()


@dp.message_handler(state=UpdProfilState.full_name)
async def ProfilUpdate_hendler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Telefon nomeringizni kiriting!"
    await UpdProfilState.phone_number.set()
    await message.answer(text=text, reply_markup=phone_number)


@dp.message_handler(state=UpdProfilState.phone_number, content_types=types.ContentType.CONTACT)
async def f_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await update_profil(data=data, chat_id=message.chat.id)
    text = "Profilingiz o'zgardi"
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()


@dp.message_handler(text="⬅️ Ortga")
async def start_hendler(message: types.Message, state: FSMContext):
    text = "Siz asosiy menyuga qaytdimngiz!"
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()


@dp.message_handler(text="🛒 Magazin")
async def start_hendler(message: types.Message):
    text = f"{message.from_user.full_name} magazinga xush kelibsiz!"
    await message.answer(text=text, reply_markup=shop_keyboard)


@dp.message_handler(text="➕ Account qo'shish")
async def f_handler(message: types.Message):
    text = "Qaysi o'yin Accounti"
    await message.answer(text=text, reply_markup=games_menu)
    await GameInfo.game_name.set()


@dp.message_handler(state=GameInfo.game_name)
async def f_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    text = "Account haqida qisqa ma'lumot bering"
    await GameInfo.game_about.set()
    await message.answer(text=text)


@dp.message_handler(state=GameInfo.game_about)
async def f_handler(message: types.Message, state: FSMContext):
    await state.update_data(about=message.text)
    text = "Accountingizmi narxini tashlang!(so'mda)"
    await GameInfo.game_price.set()
    await message.answer(text=text)


@dp.message_handler(state=GameInfo.game_price)
async def f_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    text = "Accountingizda haqida rasm tashlang!"
    await GameInfo.game_photo.set()
    await message.answer(text=text)


@dp.message_handler(state=GameInfo.game_photo, content_types=types.ContentType.PHOTO)
async def f_handler(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    cars = await add_account(data, message.chat.id)
    if cars:
        text = "Accountingiz Bozorga qo'shildi"
    else:
        text = "Botda nosozlik bor"
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()


@dp.message_handler(text="💻 Mening Accountlarim")
async def my_accountes_hendler(message: types.Message):
    text = "Harakatni tanlang!"
    await message.answer(text=text, reply_markup=my_accountes)


@dp.message_handler(text="👀 Accountlarimni ko'rish")
async def fa_handler(message: types.Message):
    all_accountes = await get_my_account(message.chat.id)
    if all_accountes:
        for i in all_accountes:
            text = (f"O'YIN NOMI: {i['name']} \n"
                    f"ACCOUNT HAQIDA: {i['about']}\n"
                    f"NARXI: {i['price']}\n"
                    f"HOLATI: {i['status']}\n"
                    f"TARTIB RAQAMI: {i['id']}")
            photo = f"{i['photo']}"
            await message.answer_photo(photo=photo, caption=text, reply_markup=shop_menu)
    else:
        text = "Siz hali Account qo'shmagansiz"
        await message.answer(text=text, reply_markup=shop_menu)


@dp.message_handler(text="🧑🏻‍💻 Adminga xabar yuborish")
async def fa_handler(message: types.Message):
    text = "Adminga xabaringizni yuboring!"
    await message.answer(text=text, reply_markup=shop_menu)
    await UserMessage.user_message.set()


@dp.message_handler(state=UserMessage.user_message)
async def fa_handler(message: types.Message, state: FSMContext):
    await state.update_data(msg=message.text, user_name=message.from_user.full_name)
    data = await state.get_data()
    text = (f"user: {data['user_name']}\n"
            f"xabar: {data['msg']}")
    await dp.bot.send_message(chat_id=5087681616, text=text)

    text = "Sizning ma'lumotingiz yoki habaringiz adminga yuborildi."
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()


@dp.message_handler(text="🎮 Accountlar")
async def fa_handler(message: types.Message, state: FSMContext):
    text = "O'yin tanlang!"
    await message.answer(text=text, reply_markup=games_menu)
    await state.set_state("user-game-account")


@dp.message_handler(state="user-game-account")
async def all_accountes_hendler(message: types.Message, state: FSMContext):
    await state.update_data(game=message.text)
    data = await state.get_data()
    all_accountes = await get_all_account(data['game'])
    if all_accountes:
        for i in all_accountes:
            text = (f"O'YIN NOMI: {i['name']} \n"
                    f"ACCOUNT HAQIDA: {i['about']}\n"
                    f"NARXI: {i['price']}\n")
            photo = f"{i['photo']}"
            await message.answer_photo(photo=photo, caption=text, reply_markup=shop_menu)
            await state.finish()
    else:
        text = "Bu o'yinga accountlar hali bozorda yo'q"
        await message.answer(text=text, reply_markup=shop_menu)
        await state.finish()


@dp.message_handler(text="❌ Bozordan olish")
async def fa_handler(message: types.Message, state: FSMContext):
    text = "Accountingiz tartib raqamini bering!(uni accountlarimni ko'rish tugmasi orqali ko'rsa bolad)"
    await message.answer(text=text)
    await state.set_state("user-inactive-account")


@dp.message_handler(state="user-inactive-account")
async def all_accountes_hendler(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    data = await state.get_data()
    await not_active_account(int(data['id']), message.chat.id)
    text = "Sizning Accountingiz inactive boldi!"
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()

@dp.message_handler(text="✅ Bozorga Qaytarish")
async def fa_handler(message: types.Message, state: FSMContext):
    text = "Accountingiz tartib raqamini bering!(uni accountlarimni ko'rish tugmasi orqali ko'rsa bolad)"
    await message.answer(text=text)
    await state.set_state("user-active-account")


@dp.message_handler(state="user-active-account")
async def all_accountes_hendler(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    data = await state.get_data()
    await active_account(int(data['id']), message.chat.id)
    text = "Sizning Accountingiz active boldi!"
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()

@dp.message_handler(text="🗑 Bozordan o'chirish")
async def fa_handler(message: types.Message, state: FSMContext):
    text = "Accountingiz tartib raqamini bering!(uni accountlarimni ko'rish tugmasi orqali ko'rsa bolad)"
    await message.answer(text=text)
    await state.set_state("user-delete-account")


@dp.message_handler(state="user-delete-account")
async def all_accountes_hendler(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    data = await state.get_data()
    await delete_accounts(int(data['id']), message.chat.id)
    text = "Sizning Accountingiz o'chirildi!"
    await message.answer(text=text, reply_markup=shop_menu)
    await state.finish()
