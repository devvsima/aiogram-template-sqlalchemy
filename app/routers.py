from aiogram import Router

common_router = Router()  # Works with standard commands, such as: start, help, etc.
user_router = Router()  # Key features for users
admin_router = Router()  # Admin command, administrator verification

voide_router = Router()  # Works when others don't
