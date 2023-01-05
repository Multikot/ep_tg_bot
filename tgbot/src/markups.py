from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_info = KeyboardButton('Info')
btn_main = KeyboardButton('Main')

btn_war = KeyboardButton('WAR')
btn_events = KeyboardButton('EVENTS')
btn_myth_titan = KeyboardButton('MYTH')

btn_donation = KeyboardButton('Donation')
btn_feedback = KeyboardButton('Feedback')


info_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_feedback, btn_donation, btn_main)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btn_events, btn_war, btn_myth_titan, btn_info
)
