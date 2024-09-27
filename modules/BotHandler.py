from telebot.async_telebot import AsyncTeleBot
from handlers.keyboard import Keyboard
from modules.communication import CommunicationHandler


class BotHandler:
    def __init__(self):
        self.keyboard = Keyboard()
        self.com_handler = CommunicationHandler()

    async def register_handlers(self, bot: AsyncTeleBot):
        @bot.message_handler(commands=['start'])
        async def handle_start(message):
            await bot.send_message(
                message.chat.id,
                'Здравствуйте! Я ИИ помощник компании EORA.\nВы можете задать мне любые вопросы по поводу работы '
                'компании, используя команду: /ask',
                reply_markup=self.keyboard.get_main_keyboard()
            )

        @bot.message_handler(commands=['ask'])
        async def handle_ask(message):
            await bot.send_message(message.chat.id, 'Что Вас интересует:')

        @bot.message_handler(content_types=['text'])
        async def handle_text(message):
            await self.com_handler.start_communication(bot=bot, message=message)
