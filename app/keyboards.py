from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Отзывы', callback_data='reviews'),
     InlineKeyboardButton(text='Контакты', callback_data='contact')]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/golenko.cake27/')]
])

confectionerys =['Торты', 'Пирожные', 'Зефир', 'Трайфлы']

async def inline_confectionery():
    keyboard = InlineKeyboardBuilder()
    for confectionery in confectionerys:
        keyboard.add(InlineKeyboardButton(text=confectionery, callback_data=f'confectionery_{confectionery}'))
    return keyboard.adjust(2).as_markup()