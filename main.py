import asyncio
from telebot.async_telebot import AsyncTeleBot
from config import token
from modules.BotHandler import BotHandler
from loguru import logger


async def main():
    try:
        bot = AsyncTeleBot(token)
        bot_handler = BotHandler()

        await bot_handler.register_handlers(bot)

        logger.info("Starting bot polling...")
        await bot.polling()
    except Exception as e:
        logger.error(f"Error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
