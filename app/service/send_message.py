from app.models.webhook import Webhook
import requests
import os
from dotenv import load_dotenv
from app.utils.config import env_path, bot_secret
from loguru import logger


async def send_message(message_text: str, ids: list[int]):
    try:
        load_dotenv(env_path())
        token = os.environ.get(bot_secret())
        for id in ids:
            response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={
                "chat_id": id, "text": message_text, "parse_mode": "Markdown", "disable_web_page_preview": "true"})
            response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.error(err)
