from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱 Telefon raqam ulashish', request_contact=True)
        ]
    ], resize_keyboard=True
)

games_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fortnite"),
            KeyboardButton(text="PUBG")
        ],
        [
            KeyboardButton(text="DOTA 2"),
            KeyboardButton(text="CS GO")
        ],
        [
            KeyboardButton(text="Standoff 2"),
            KeyboardButton(text="Car Parking")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ], resize_keyboard=True
)

shop_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒 Magazin")
        ],
        [
            KeyboardButton(text="👤 Profil"),
            KeyboardButton(text="🧑🏻‍💻 Adminga xabar yuborish")
        ],
    ], resize_keyboard=True
)

shop_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎮 Accountlar"),
            KeyboardButton(text="➕ Account qo'shish")
        ],
        [
            KeyboardButton(text="💻 Mening Accountlarim")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ], resize_keyboard=True
)

my_accountes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👀 Accountlarimni ko'rish"),
            KeyboardButton(text="🗑 Bozordan o'chirish")
        ],
[
            KeyboardButton(text="✅ Bozorga Qaytarish"),
            KeyboardButton(text="❌ Bozordan olish")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ], resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ], resize_keyboard=True
)

channel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kanalga a'zo bo'lish", url="https://t.me/uy_ishi_chop")
        ]
    ], resize_keyboard=True
)

