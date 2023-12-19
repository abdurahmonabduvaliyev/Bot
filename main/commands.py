from main.models import *
from main.database_set import database
from sqlalchemy import update


async def add_user(data: dict, chat_id):
    try:
        query = users.insert().values(
            full_name=data.get('full_name'),
            phone_number=data.get('phone_number'),
            chat_id=chat_id
        )

        new_user = await database.execute(query=query)
        return new_user
    except Exception as exs:
        print(exs)
        return False


async def get_user(chat_id: int):
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        user = await database.fetch_all(query=query)
        return user
    except Exception as exs:
        print(exs)
        return False


async def add_account(data: dict, chat_id):
    try:
        query = accountes.insert().values(
            name=data.get('name'),
            about=data.get('about'),
            price=data.get('price'),
            photo=data.get('photo'),
            status='active',
            chat_id=chat_id

        )

        new_account = await database.execute(query=query)
        return new_account
    except Exception as exs:
        print(exs)
        return False


async def get_my_account(chat_id: int):
    try:
        query = accountes.select().where(accountes.c.chat_id == chat_id)
        all_accounts = await database.fetch_all(query)
        return all_accounts
    except Exception as exs:
        print(exs)
        return False


async def get_all_account(name: str):
    try:
        query = accountes.select().where(accountes.c.name == name, accountes.c.status == "active")
        all_accounts = await database.fetch_all(query)

        return all_accounts
    except Exception as exs:
        print(exs)
        return False


async def not_active_account(id: int, chat_id):
    try:
        query = update(accountes).where(accountes.c.id == id, accountes.c.chat_id == chat_id).values(status='inactive')
        all_accounts = await database.execute(query)
        return all_accounts
    except Exception as exs:
        print(exs)
        return False


async def active_account(id: int, chat_id):
    try:
        query = update(accountes).where(accountes.c.id == id, accountes.c.chat_id == chat_id).values(status='active')
        all_accounts = await database.execute(query)
        return all_accounts
    except Exception as exs:
        print(exs)
        return False


async def update_profil(data, chat_id: int):
    try:
        query = update(users).where(users.c.chat_id == chat_id).values(
            full_name=data.get('full_name'),
            phone_number=data.get('phone_number')
        )
        all_accounts = await database.execute(query)
        return all_accounts
    except Exception as exs:
        print(exs)
        return False


async def delete_accounts(id: int, chat_id: int):
    try:
        query = accountes.delete().where(accountes.c.id == id, accountes.c.chat_id == chat_id)
        delete_account = await database.execute(query)
        return delete_account
    except Exception as exs:
        print(exs)
        return False
