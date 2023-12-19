from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

next_back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ back", callback_data="back"),
            InlineKeyboardButton(text="➡️ next", callback_data="next")
        ]
    ]
)


upd_profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zgartirish", callback_data="Update")
        ]
    ]
)
