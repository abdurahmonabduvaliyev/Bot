from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    full_name = State()
    phone_number = State()


class GameInfo(StatesGroup):
    game_name = State()
    game_about = State()
    game_price = State()
    game_photo = State()


class UserMessage(StatesGroup):
    user_message = State()

class UpdProfilState(StatesGroup):
    full_name = State()
    phone_number = State()
