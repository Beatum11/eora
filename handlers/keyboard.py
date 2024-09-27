from telebot import types


class Keyboard:

    # Функция отвечает за рендер клавиатуры
    @staticmethod
    def get_main_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        start_key = types.KeyboardButton('/start')
        ask_key = types.KeyboardButton('/ask')
        markup.add(start_key, ask_key)
        return markup
