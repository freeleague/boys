from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_city():
    study_bt = [[KeyboardButton(text="Москва")],
                [KeyboardButton(text="Санкт-Петербург")],
                [KeyboardButton(text="Контакты")]]
    study = ReplyKeyboardMarkup(keyboard=study_bt, resize_keyboard=True)
    return study

def get_goods():
    goods_bt = [[KeyboardButton(text="Гречка бля")],
                [KeyboardButton(text="Рис бля")],
                [KeyboardButton(text="Макароны бля")],
                [KeyboardButton(text="НАЗАД")]]
    goods = ReplyKeyboardMarkup(keyboard=goods_bt, resize_keyboard=True)
    return goods

def get_weight():
    weight_bt = [[KeyboardButton(text="1 кг нах")],
                 [KeyboardButton(text="2 кг нах")],
                 [KeyboardButton(text="3 кг нах")],
                 [KeyboardButton(text="НАЗАД")]]
    weight = ReplyKeyboardMarkup(keyboard=weight_bt, resize_keyboard=True)
    return weight

def get_ship():
    ship_bt = [[KeyboardButton(text="Доставка")],
               [KeyboardButton(text="НАЗАД")]]
    ship = ReplyKeyboardMarkup(keyboard=ship_bt, resize_keyboard=True)
    return ship

def get_pay():
    pay_bt = [[KeyboardButton(text="ОПЛАТИТЬ!")],
               [KeyboardButton(text="НАЗАД")]]
    pay = ReplyKeyboardMarkup(keyboard=pay_bt, resize_keyboard=True)
    return pay

def get_check():
    check_bt = [[KeyboardButton(text="Проверить оплату епта")],
                [KeyboardButton(text="НАЗАД")]]
    check = ReplyKeyboardMarkup(keyboard=check_bt, resize_keyboard=True)
    return check

def get_home():
    home_bt = [[KeyboardButton(text="НАЗАД")]]
    home = ReplyKeyboardMarkup(keyboard=home_bt, resize_keyboard=True)
    return home