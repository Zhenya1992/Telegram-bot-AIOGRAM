from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Отзывы'), KeyboardButton(text='Контакты')]
],
                        resize_keyboard=True,
                        input_field_placeholder='Выберите пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/golenko.cake27/')]
])
