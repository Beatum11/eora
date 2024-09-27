import asyncio
import os
import aiohttp
from handlers.keyboard import Keyboard
from config import chat_histories, system_message
from loguru import logger


class CommunicationHandler:
    def __init__(self):
        self.openai_key = os.environ.get('OPENAI_KEY')
        self.keyboard = Keyboard()

    async def start_communication(self, bot, message):

        if not message.text:
            await bot.send_message(message.chat.id, 'Похоже, что вы отправили пустое сообщение. Попробуйте еще раз.')
            return

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.openai_key}",
            "Content-Type": "application/json"
        }

        chat_id = message.chat.id

        if chat_id not in chat_histories:
            chat_histories[chat_id] = []

        if system_message not in chat_histories[chat_id]:
            chat_histories[chat_id].append(system_message)

        user_message = {
            "role": "user",
            "content": message.text
        }

        chat_histories[chat_id].append(user_message)

        data = {
            "model": "gpt-4o",
            "messages": chat_histories[chat_id],
            "temperature": 1,
            "max_tokens": 300,
            "top_p": 1,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.5
        }
        markup = self.keyboard.get_main_keyboard()

        await bot.send_chat_action(message.chat.id, 'typing')

        max_attempts = 3
        attempt = 0
        delay = 2

        while attempt < max_attempts:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, json=data, headers=headers) as response:
                        if response.status == 200:
                            answer = await response.json()
                            send_msg = answer['choices'][0]['message']['content']
                            chat_histories[chat_id].append({
                                "role": "assistant",
                                "content": send_msg
                            })

                            await bot.send_message(message.chat.id, send_msg, reply_markup=markup,
                                                   parse_mode='Markdown')
                            logger.info(f'Для {message.chat.id} было успешно сгенерированно сообщение')
                            break
                        else:
                            raise aiohttp.ClientResponseError(response.request_info,
                                                              response.history,
                                                              status=response.status)
            except (TimeoutError, aiohttp.ClientResponseError) as e:
                attempt += 1
                if attempt < max_attempts:
                    await asyncio.sleep(delay)  # Ждем перед следующей попыткой
                    delay *= 2  # Увеличиваем задержку для следующей попытки
                else:
                    await bot.send_message(message.chat.id,
                                           'Проблемы с соединением, попробуйте буквально через минуту.')
                    logger.error(f'Какие-то проблемы с соединением у {message.chat.id} - {e}')
            except Exception as e:
                await bot.send_message(message.chat.id, 'Неизвестная ошибка. Попробуй чуть позже.')
                logger.error(f'Необработанная ошибка у {message.chat.id} - {e}')
                break
