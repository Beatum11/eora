from pathlib import Path
from dotenv import load_dotenv
import os
from loguru import logger

# Load environment variables
load_dotenv()

# Set up logger
app_root = Path(__file__).parent
log_file_path = app_root / "logs/application.log"
logger.add(log_file_path, rotation="30 MB")

token = os.environ.get('TELEGRAM_TOKEN')

url_list: list[str] = [
    "https://eora.ru/cases/promyshlennaya-bezopasnost",
    "https://eora.ru/cases/lamoda-systema-segmentacii-i-poiska-po-pohozhey-odezhde",
    "https://eora.ru/cases/navyki-dlya-golosovyh-assistentov/karas-golosovoy-assistent",
    "https://eora.ru/cases/assistenty-dlya-gorodov",
    "https://eora.ru/cases/avtomatizaciya-v-promyshlennosti/chemrar-raspoznovanie-molekul",
    "https://eora.ru/cases/zeptolab-skazki-pro-amnyama-dlya-sberbox",
    "https://eora.ru/cases/goosegaming-algoritm-dlya-ocenki-igrokov",
    "https://eora.ru/cases/dodo-pizza-robot-analitik-otzyvov",
    "https://eora.ru/cases/ifarm-nejroset-dlya-ferm",
    "https://eora.ru/cases/zhivibezstraha-navyk-dlya-proverki-rodinok",
    "https://eora.ru/cases/sportrecs-nejroset-operator-sportivnyh-translyacij",
    "https://eora.ru/cases/avon-chat-bot-dlya-zhenshchin",
    "https://eora.ru/cases/navyki-dlya-golosovyh-assistentov/navyk-dlya-proverki-loterejnyh-bileto",
    "https://eora.ru/cases/computer-vision/iss-analiz-foto-avtomobilej",
    "https://eora.ru/cases/purina-master-bot",
    "https://eora.ru/cases/skinclub-algoritm-dlya-ocenki-veroyatnostej",
    "https://eora.ru/cases/skolkovo-chat-bot-dlya-startapov-i-investorov",
    "https://eora.ru/cases/purina-podbor-korma-dlya-sobaki",
    "https://eora.ru/cases/purina-navyk-viktorina",
    "https://eora.ru/cases/dodo-pizza-pilot-po-avtomatizacii-kontakt-centra",
    "https://eora.ru/cases/dodo-pizza-avtomatizaciya-kontakt-centra",
    "https://eora.ru/cases/icl-bot-sufler-dlya-kontakt-centra",
    "https://eora.ru/cases/s7-navyk-dlya-podbora-aviabiletov",
    "https://eora.ru/cases/workeat-whatsapp-bot",
    "https://eora.ru/cases/absolyut-strahovanie-navyk-dlya-raschyota-strahovki",
    "https://eora.ru/cases/kazanexpress-poisk-tovarov-po-foto",
    "https://eora.ru/cases/kazanexpress-sistema-rekomendacij-na-sajte",
    "https://eora.ru/cases/intels-proverka-logotipa-na-plagiat",
    "https://eora.ru/cases/karcher-viktorina-s-voprosami-pro-uborku",
    "https://eora.ru/cases/chat-boty/purina-friskies-chat-bot-na-sajte",
    "https://eora.ru/cases/nejroset-segmentaciya-video",
    "https://eora.ru/cases/chat-boty/essa-nejroset-dlya-generacii-rolikov",
    "https://eora.ru/cases/qiwi-poisk-anomalij",
    'https://eora.ru/cases/frisbi-nejroset-dlya-raspoznavaniya-pokazanij-schetchikov',
    'https://eora.ru/cases/navyki-dlya-golosovyh-assistentov/skazki-dlya-gugl-assistenta',
    'https://eora.ru/cases/chat-boty/hr-bot-dlya-magnit-kotoriy-priglashaet-na-sobesedovanie',
    'https://eora.ru/'
]

# Чтобы не тратить время на подключение к БД, используем словарь
chat_histories: dict = {}

system_message = dict(role="system", content=f"""
        Ты - ИИ-ассистент компании Eora, помогающей бизнесу внедрять ИИ. Твои задачи:

        • Отвечать на вопросы о работе компании, используя ТОЛЬКО информацию с указанных ссылок: {url_list}
        • При упоминании конкретного подпроекта указывать ссылку на соответствующую подстраницу рядом с примером
        • Отвечать на каждый вопрос как на отдельное сообщение, сохраняя контекст предоставленной информации
        • Для вопросов о конкретной индустрии приводить как минимум 2, как максимум 3 кратких примера из релевантных проектов в портфолио
        • Давать краткие и четкие ответы

        Всегда придерживайся этих инструкций при ответе на вопросы пользователей.
        """)
